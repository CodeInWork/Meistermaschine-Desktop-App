"""Validate the curated distribution boundary; never discover local libraries."""
import json
from pathlib import Path, PureWindowsPath


def validate_examples(package_path):
    package = Path(package_path).resolve()
    examples = package / "assets/examples"
    audio = examples / "audio"
    presets = sorted((examples / "presets").glob("*.json"))
    if not presets:
        raise ValueError("No example presets found")
    references = set()
    for preset in presets:
        data = json.loads(preset.read_text(encoding="utf-8-sig"))
        for channel in data["channels"].values():
            for button in channel["buttons"]:
                for stored in button.get("playlist", []):
                    if not isinstance(stored, str) or not stored:
                        raise ValueError(f"Invalid example audio reference: {stored!r}")
                    normalized = stored.replace("\\", "/")
                    path = Path(normalized)
                    if path.is_absolute() or PureWindowsPath(stored).drive or PureWindowsPath(stored).root:
                        raise ValueError(f"Absolute example audio reference: {stored}")
                    target = (package / path).resolve()
                    if not target.is_relative_to(audio) or not target.is_file():
                        raise ValueError(f"Missing or escaping example audio reference: {stored}")
                    references.add(target)
    # Directory bundling must not follow links out of the curated boundary.
    for entry in examples.rglob("*"):
        if not entry.resolve().is_relative_to(examples):
            raise ValueError(f"Example asset escapes distribution boundary: {entry}")
    return references
