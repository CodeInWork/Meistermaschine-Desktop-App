from pathlib import Path
import shutil
import time
from collections.abc import Callable
import os
import subprocess
import imageio_ffmpeg
import tempfile
import re

from MEISTERMASCHINE.preset_utilities.preset_io import save_mms
from MEISTERMASCHINE.sd_utilities.sd_audio import get_sd_audio_filename

# Constants for MP3 conversion
MP3_BITRATE = "192k"
MP3_SAMPLE_RATE = 44100
MP3_CHANNELS = 2

ProgressCallback = Callable[[int, int, Path], None]
StatusCallback = Callable[[str], None]


def collect_audio_files(button_groups, application_path: str) -> list[Path]:
    """
    Return all unique audio files referenced by the supplied button groups.
    """
    application_dir = Path(application_path)

    audio_files = []
    seen_paths = set()

    for group in button_groups:
        for button in group:
            for track in button.playlist.tracks:
                stored_path = Path(track[0])

                if stored_path.is_absolute():
                    source_path = stored_path
                else:
                    source_path = application_dir / stored_path

                source_path = source_path.resolve()

                if source_path not in seen_paths:
                    seen_paths.add(source_path)
                    audio_files.append(source_path)

    return audio_files


def export_preset_to_sd(
    sd_root: str,
    preset_name: str,
    application_path: str,
    music_buttons,
    setting_buttons,
    weather_buttons,
    special_buttons,
    progress_callback: ProgressCallback | None = None,
    status_callback: StatusCallback | None = None,
    replace_existing: bool = False,
) -> Path:

    safe_name = sanitize_folder_name(preset_name)

    if not safe_name:
        raise ValueError("The preset name is empty or invalid.")

    sd_path = Path(sd_root)
    export_dir = sd_path / safe_name

    button_groups = [
        music_buttons,
        setting_buttons,
        weather_buttons,
        special_buttons,
    ]

    audio_files = collect_audio_files(
        button_groups,
        application_path,
    )

    _validate_audio_files(audio_files)
    _validate_unique_export_filenames(audio_files)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        converted_files = []

        if status_callback is not None:
            status_callback("Converting audio files to MP3...")

        for source_path in audio_files:
            destination_name = get_sd_audio_filename(source_path)
            converted_path = temp_path / destination_name

            _convert_to_mp3(
                source_path=source_path,
                destination_path=converted_path,
            )

            converted_files.append(converted_path)

        _prepare_export_directory(
            sd_root=sd_path,
            export_dir=export_dir,
            replace_existing=replace_existing,
        )

        mms_path = export_dir / f"{safe_name}.mms"

        save_mms(
            str(mms_path),
            music_buttons,
            setting_buttons,
            weather_buttons,
            special_buttons,
            path_transform=get_sd_audio_filename,
        )

        total_bytes = sum(
            path.stat().st_size
            for path in converted_files
        )

        copied_bytes = 0

        if status_callback is not None:
            status_callback("Copying files to SD card...")

        for source_path in converted_files:
            destination_path = export_dir / source_path.name

            copied_bytes = _copy_file_with_progress(
                source_path=source_path,
                destination_path=destination_path,
                copied_bytes=copied_bytes,
                total_bytes=total_bytes,
                progress_callback=progress_callback,
            )

    return export_dir


def _copy_file_with_progress(
    source_path: Path,
    destination_path: Path,
    copied_bytes: int,
    total_bytes: int,
    progress_callback: ProgressCallback | None,
) -> int:
    """
    Copy one file in chunks and report byte-level progress.

    Returns the updated total number of copied bytes.
    """

    chunk_size = 1024 * 1024  # 1 MB

    with source_path.open("rb") as source_file:
        with destination_path.open("wb") as destination_file:

            while True:
                chunk = source_file.read(chunk_size)

                if not chunk:
                    break

                destination_file.write(chunk)

                copied_bytes += len(chunk)

                if progress_callback is not None:
                    progress_callback(
                        copied_bytes,
                        total_bytes,
                        source_path,
                    )

    shutil.copystat(
        source_path,
        destination_path,
    )

    return copied_bytes


def _validate_audio_files(audio_files: list[Path]) -> None:
    missing_files = [
        str(path)
        for path in audio_files
        if not path.is_file()
    ]

    if missing_files:
        formatted = "\n".join(missing_files)

        raise FileNotFoundError(
            "The following audio files could not be found:\n"
            f"{formatted}"
        )


def _validate_unique_export_filenames(
    audio_files: list[Path],
) -> None:

    filenames = {}

    for path in audio_files:
        export_name = get_sd_audio_filename(path)
        normalized_name = export_name.casefold()

        previous_path = filenames.get(normalized_name)

        if previous_path is not None and previous_path != path:
            raise ValueError(
                "Two audio files would have the same filename "
                "after MP3 conversion:\n\n"
                f"{previous_path}\n"
                f"{path}\n\n"
                f"Both would become:\n{export_name}"
            )

        filenames[normalized_name] = path


def sanitize_folder_name(name: str) -> str:
    invalid_characters = '<>:"/\\|?*'

    sanitized = "".join(
        "_"
        if character in invalid_characters
        else character
        for character in name.strip()
    )

    return sanitized.rstrip(". ")



def _prepare_export_directory(
    sd_root: Path,
    export_dir: Path,
    replace_existing: bool,
) -> None:

    if not export_dir.exists():
        export_dir.mkdir(
            parents=True,
            exist_ok=False,
        )
        return

    if not replace_existing:
        raise FileExistsError(
            f"The preset folder already exists:\n{export_dir}"
        )

    _validate_safe_export_path(
        sd_root=sd_root,
        export_dir=export_dir,
    )

    shutil.rmtree(export_dir)

    _create_directory_with_retry(export_dir)


def _validate_safe_export_path(
    sd_root: Path,
    export_dir: Path,
) -> None:
    """
    Ensure that only a direct child directory of the selected SD root
    can be removed.
    """

    sd_root = sd_root.resolve()
    export_dir = export_dir.resolve()

    if export_dir == sd_root:
        raise ValueError(
            "Refusing to delete the root directory of the SD card."
        )

    if export_dir.parent != sd_root:
        raise ValueError(
            "Refusing to delete an unexpected directory:\n"
            f"{export_dir}"
        )



def _create_directory_with_retry(
    directory: Path,
    timeout: float = 2.0,
) -> None:

    start_time = time.monotonic()

    while True:
        try:
            directory.mkdir(
                parents=True,
                exist_ok=False,
            )
            return

        except PermissionError:
            if time.monotonic() - start_time > timeout:
                raise

            time.sleep(0.05)


def _convert_to_mp3(
    source_path: Path,
    destination_path: Path,
) -> None:
    """
    Convert an audio file to a standardized MP3 for the physical
    Meistermaschine.
    """

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    command = [
        ffmpeg_exe,
        "-y",
        "-i", str(source_path),
        "-vn",
        "-codec:a", "libmp3lame",
        "-b:a", MP3_BITRATE,
        "-ar", str(MP3_SAMPLE_RATE),
        "-ac", str(MP3_CHANNELS),
        str(destination_path),
    ]

    kwargs = {}

    if os.name == "nt":
        kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        **kwargs,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Could not convert audio file:\n"
            f"{source_path}\n\n"
            f"FFmpeg error:\n{result.stderr}"
        )
