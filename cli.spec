# -*- mode: python ; coding: utf-8 -*-
"""Windows one-folder build. Run through build.ps1 with the uv environment."""
from pathlib import Path

import imageio_ffmpeg
from PyInstaller.utils.hooks import collect_data_files

root = Path(SPECPATH)
package = root / "MEISTERMASCHINE"
datas = [(str(package / name), f"MEISTERMASCHINE/{name}")
         for name in ("icons", "sounds", "presets")]
datas += [(str(root / "LICENSE"), ".")]
# Preserve the additional sound collection in the portable distribution.
datas += [(str(root / "Sounds - Napoleon"), "Sounds - Napoleon")]
# Include the wheel's FFmpeg, never a developer-machine/PATH executable.
ffmpeg_dir = Path(imageio_ffmpeg.__file__).parent / "binaries"
if not list(ffmpeg_dir.glob("ffmpeg*.exe")):
    raise RuntimeError("Install the Windows imageio-ffmpeg wheel before building.")
datas += collect_data_files("imageio_ffmpeg", subdir="binaries")

# Qt hooks collect DLLs/plugins, including the QtMultimedia FFmpeg backend.
a = Analysis(
    [str(root / "cli.py")],
    pathex=[str(root)],
    binaries=[],
    datas=datas,
    hiddenimports=["imageio_ffmpeg.binaries"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Meistermaschine",
    console=False,
    debug=False,
    strip=False,
    upx=False,
    disable_windowed_traceback=False,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name="Meistermaschine",
)
