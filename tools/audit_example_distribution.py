"""Compare a built distribution with the curated examples and write its inventory."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from MEISTERMASCHINE.example_assets import validate_examples
from MEISTERMASCHINE.config import AUDIO_EXTS


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def audit(distribution, report):
    distribution = distribution.resolve()
    source = ROOT / "MEISTERMASCHINE"
    packaged = distribution / "_internal/MEISTERMASCHINE"
    references = validate_examples(source)
    validate_examples(packaged)
    expected = {p.relative_to(source).as_posix() for p in references}
    actual = {p.relative_to(packaged).as_posix()
              for p in distribution.rglob("*") if p.is_file() and p.suffix.lower() in AUDIO_EXTS}
    if actual != expected:
        raise ValueError(f"Audio mismatch: extra={actual - expected}, missing={expected - actual}")
    for folder in ("assets/examples", "icons"):
        originals = {p.relative_to(source).as_posix(): digest(p)
                     for p in (source / folder).rglob("*") if p.is_file()}
        copies = {p.relative_to(packaged).as_posix(): digest(p)
                  for p in (packaged / folder).rglob("*") if p.is_file()}
        if copies != originals:
            raise ValueError(f"Resource hash mismatch: {folder}")
    for forbidden in (packaged / "sounds", packaged / "presets",
                      distribution / "_internal/Sounds - Napoleon", distribution / "_internal/sounds"):
        if forbidden.exists():
            raise ValueError(f"Local library included: {forbidden}")
    presets = [p.relative_to(packaged).as_posix() for p in distribution.rglob("*")
               if p.suffix.lower() in (".json", ".mms") and "presets" in p.parts]
    if presets != ["assets/examples/presets/Medieval.json"]:
        raise ValueError(f"Unexpected preset inventory: {presets}")
    inventory = [{"path": p.relative_to(distribution).as_posix(), "bytes": p.stat().st_size,
                  "sha256": digest(p)} for p in sorted(distribution.rglob("*")) if p.is_file()]
    result = {"ok": True, "audio_count": len(actual), "audio": sorted(actual), "presets": presets,
              "file_count": len(inventory), "total_bytes": sum(p["bytes"] for p in inventory),
              "files": inventory}
    report.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in ("files", "audio")}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("distribution", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    audit(args.distribution, args.report)
