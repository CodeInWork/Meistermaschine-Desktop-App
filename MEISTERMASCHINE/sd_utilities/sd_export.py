from pathlib import Path
import shutil

from MEISTERMASCHINE.preset_utilities.preset_io import save_mms


def collect_audio_files(button_groups, application_path: str) -> list[Path]:
    """
    Return all unique audio files referenced by the supplied button groups.
    """

    application_dir = Path(application_path)
    audio_files: list[Path] = []
    seen_paths: set[Path] = set()

    for group in button_groups:
        for button in group:
            for track in button.playlist:
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
) -> Path:
    """
    Export an MMS file and all required audio files into a preset folder
    on the selected SD card.

    Returns the created preset directory.
    """

    safe_name = sanitize_folder_name(preset_name)

    if not safe_name:
        raise ValueError("The preset name is empty or invalid.")

    sd_path = Path(sd_root)
    export_dir = sd_path / safe_name

    export_dir.mkdir(parents=True, exist_ok=True)

    button_groups = [
        music_buttons,
        setting_buttons,
        weather_buttons,
        special_buttons,
    ]

    audio_files = collect_audio_files(
        button_groups=button_groups,
        application_path=application_path,
    )

    _validate_audio_files(audio_files)
    _validate_unique_filenames(audio_files)

    mms_path = export_dir / f"{safe_name}.mms"

    save_mms(
        str(mms_path),
        music_buttons,
        setting_buttons,
        weather_buttons,
        special_buttons,
        filenames_only=True,
    )

    for source_path in audio_files:
        destination_path = export_dir / source_path.name
        shutil.copy2(source_path, destination_path)

    return export_dir

def _validate_audio_files(audio_files: list[Path]) -> None:
    missing_files = [
        str(path)
        for path in audio_files
        if not path.is_file()
    ]

    if missing_files:
        formatted = "\n".join(missing_files)
        raise FileNotFoundError(
            f"The following audio files could not be found:\n{formatted}"
        )


def _validate_unique_filenames(audio_files: list[Path]) -> None:
    filenames: dict[str, Path] = {}

    for path in audio_files:
        normalized_name = path.name.casefold()

        previous_path = filenames.get(normalized_name)

        if previous_path is not None and previous_path != path:
            raise ValueError(
                "Two different audio files have the same filename:\n"
                f"{previous_path}\n"
                f"{path}"
            )

        filenames[normalized_name] = path


def sanitize_folder_name(name: str) -> str:
    invalid_characters = '<>:"/\\|?*'

    sanitized = "".join(
        "_" if character in invalid_characters else character
        for character in name.strip()
    )

    return sanitized.rstrip(". ")