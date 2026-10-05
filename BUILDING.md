# Windows portable build

Build on Windows with uv and Python 3.12 or newer (as required by
`pyproject.toml`). Python and uv are needed only on the build machine.

From PowerShell in the repository root:

```powershell
.\build.ps1
```

The script runs `uv sync --locked --group dev`, then
`uv run --no-sync python -m PyInstaller --noconfirm --clean cli.spec`.
It stops on either failure. The lockfile fixes dependency versions; it is not
regenerated during a build. Use the same Python version and Windows architecture
when reproducing a release. This does not promise byte-identical executables.
The script uses its own directory, so it can also be invoked from another folder.
Rebuilding replaces the generated `dist/Meistermaschine` folder; keep user presets
and other personal files outside the build output before rebuilding.

## Output and resources

Launch `dist/Meistermaschine/Meistermaschine.exe`. Distribute the **entire**
`dist/Meistermaschine` directory, usually as a ZIP. `_internal` is required.
Recipients do not need Python, Qt, or a separate FFmpeg installation.

The spec uses `cli.py` as its entry point and creates a windowed, one-folder
application. PyInstaller's Qt hooks collect the imported PyQt6 modules, platform
plugins, image plugins, multimedia backend, and codec DLLs. The imageio-ffmpeg
wheel's executable is bundled for SD-export conversion; Qt also has its own
FFmpeg playback libraries. UPX is disabled.

Resources under `_internal/MEISTERMASCHINE` mirror the source package:

- `icons`: all button and control images.
- `sounds`: the full bundled sound library, including subdirectories.
- `presets`: existing JSON and MMS presets.

The additional `Sounds - Napoleon` collection and project license are included
under `_internal`. The top-level source `sounds` directory is empty; the app uses
`MEISTERMASCHINE/sounds`. Resource paths resolve relative to the package, independent
of the process working directory, in both development and the frozen app.

Extract the portable folder to a writable location, such as a folder under your
user profile. Presets retain the existing behavior: the default preset folder
lives alongside the bundled resources, and the last selected preset is remembered
through QSettings. This build does not migrate presets to AppData. Back up edited
presets before replacing a distribution. External audio paths stored in a preset
still need to exist on the recipient's machine; packaging cannot restore missing
source files or make machine-specific absolute paths portable.

## Smoke test

The opt-in diagnostic starts Qt offscreen, creates all 20 sound buttons, checks
icons/resource folders, finds bundled FFmpeg without relying on PATH, converts a
generated WAV to MP3 using the application's conversion function, and loads that
MP3 through QtMultimedia. It skips saved-preset restoration and removable-drive
scanning. It writes a JSON report and returns a nonzero exit code on failure.

```powershell
$exe = (Resolve-Path '.\dist\Meistermaschine\Meistermaschine.exe').Path
$report = Join-Path $env:TEMP 'meistermaschine-smoke.json'
$process = Start-Process -FilePath $exe -WindowStyle Hidden -Wait -PassThru `
    -WorkingDirectory $env:TEMP `
    -ArgumentList @('--smoke-test', ('"' + $report + '"'))
Get-Content -LiteralPath $report
if ($process.ExitCode -ne 0) { throw 'Packaged smoke test failed.' }
```

The same check is available in development:
`uv run python cli.py --smoke-test <absolute-report-path>`.
For manual release validation, launch the executable on a clean Windows machine
without Python/FFmpeg installed, verify audible playback, assign audio and icons,
save/reload a preset, resize the window, and export to a test folder.

## Build diagnostics

PyInstaller writes analysis warnings to `build/cli/warn-cli.txt` and the dependency
graph to `build/cli/xref-cli.html`. Missing optional modules for other platforms
are not necessarily failures; investigate missing application dependencies.
The PowerShell output contains build errors. The windowed executable retains
PyInstaller's traceback dialog for startup exceptions.

References: [PyInstaller spec files](https://pyinstaller.org/en/stable/spec-files.html),
[resource paths](https://pyinstaller.org/en/stable/runtime-information.html),
[imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg).

## Validation of this build

Built on Windows 11 x64 with Python 3.12.0, uv 0.11.21, PyInstaller 6.21.0,
and hooks 2026.6 using the existing lockfile. The output contains 378 files
(approximately 1,001 MiB). All source icons, sounds, and presets were checked
against the distribution for presence and file size.

Both development and frozen smoke tests passed. The executable was tested with
the temporary directory as its working directory, found its own bundled FFmpeg,
created 20 buttons, found 96 sound files, and converted/loaded a 1,044 ms MP3.
Reports are in `build/development-smoke.json` and `build/packaged-smoke.json`.
Audible playback and operation on a separate clean Windows machine remain manual
release checks.

There were no PyInstaller build errors. The initial sandboxed invocation could
not access uv's user cache; rerunning with permission resolved it. Analysis warnings
concern optional/platform-specific modules and PyInstaller/Python runtime modules;
none prevented the frozen smoke test.

Existing presets contain some unavailable relative sound paths and machine-specific
absolute paths (including paths on `G:`). Those presets were preserved unchanged.
Bundling the available sound library does not repair those references.
