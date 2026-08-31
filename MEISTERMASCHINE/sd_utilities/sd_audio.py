from pathlib import Path
import re

# get a hardware safe filename for an audio file, based on its original name and path
def get_sd_audio_filename(source_path: str | Path) -> str:
    stem = Path(source_path).stem

    safe_stem = re.sub(
        r"[^A-Za-z0-9_]+",
        "_",
        stem,
    )

    safe_stem = re.sub(
        r"_+",
        "_",
        safe_stem,
    ).strip("_")

    if not safe_stem:
        safe_stem = "audio"

    return f"{safe_stem}.mp3"