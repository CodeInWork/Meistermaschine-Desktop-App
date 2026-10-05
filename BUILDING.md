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
- `assets/examples/audio`: the 24 audio files used by the Medieval example.
- `assets/examples/presets`: only `Medieval.json`.

The project license is included under `_internal`. The curated
`MEISTERMASCHINE/assets/examples/` directory is the explicit distribution boundary:
the spec bundles that directory, not a file list generated from the preset.
Before packaging, `example_assets.py` validates that every example audio reference
exists below `assets/examples/audio/`; absolute paths, escaped paths, missing files,
and links escaping the example directory fail the build.

`MEISTERMASCHINE/sounds/`, `MEISTERMASCHINE/presets/`, `Sounds - Napoleon/`, and
the root `sounds/` directory are personal, ignored directories. They are never
included by the spec. Keep distributable assets only inside `assets/examples/`;
anything added there will be bundled, so review its contents before a release.
Git ignore rules do not control PyInstaller inclusion.

Development defaults to the existing local sound library when present. The frozen
app (or a fresh checkout without local sounds) defaults to example audio. Use the
existing folder picker to browse any other library, including `Sounds - Napoleon`.
The development preset list includes local JSON presets and `Medieval (Example)`.
Only the example is supplied in a fresh checkout or distribution.

Playback and SD-export path resolution remain unchanged: relative paths resolve
against `MEISTERMASCHINE`, independently of the working directory, and absolute
user paths remain supported. The example stores `assets/examples/audio/...` paths;
existing local presets keep their `sounds/...` paths. Personal files were copied
where needed and removed from Git's index with `git rm --cached`, not deleted.
Untracking does not remove earlier committed copies from Git history.

Extract the portable folder to a writable location, such as a folder under your
user profile. Presets retain the existing behavior: the default preset folder
lives alongside the bundled resources, and the last selected preset is remembered
through QSettings. This build does not migrate presets to AppData. Back up edited
presets before replacing a distribution. External audio paths stored in a preset
still need to exist on the recipient's machine; packaging cannot restore missing
source files or make machine-specific absolute paths portable.

## Smoke test

The opt-in diagnostic starts Qt offscreen, creates all 20 sound buttons, checks
icons/resource folders, loads the Medieval preset, and opens every one of its 24
tracks through the application's playback code with silent output. It checks the
SD-export source paths and, when available, the original local Medieval preset.
It finds bundled FFmpeg without relying on PATH and converts a
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

## Asset verification and migration build

Run the path-validation and local-preset compatibility tests:

```powershell
.venv/Scripts/python.exe -m unittest discover -s tests -v
```

The migration build uses separate output to preserve previous build artifacts:

```powershell
.venv/Scripts/python.exe -m PyInstaller --noconfirm --clean --distpath dist/example-release --workpath build/example-release cli.spec
.venv/Scripts/python.exe tools/audit_example_distribution.py dist/example-release/Meistermaschine build/audio-migration/distribution-inventory.json
```

The audit compares every bundled example and icon by SHA-256, requires exactly the
audio referenced by the example, rejects local-library directories, and writes a
complete distribution file inventory with sizes and hashes. This is a release
check; it does not change the spec's directory-based inclusion policy.

Migration reports are in `build/audio-migration/`: development and packaged smoke
reports, the distribution inventory, local-file integrity report, build log, and
`history-audio.md` listing all 95 removed audio paths and their Git blob IDs.
All 109 local library/preset files retain their original contents. The 95 audio
files remain in Git history: 24 also have curated example copies, while 71 are
excluded from the new distribution. No history rewrite was performed.

The previous `dist/Meistermaschine` output may still contain personal audio.
Use only the newly audited `dist/example-release/Meistermaschine` for this migration.
Ordinary `build.ps1` builds use the updated spec but retain their usual output path.
Staged Git deletion entries record untracking and remain visible until committed;
the ignored local files themselves are no longer tracked or listed as untracked.

Audible playback and operation on a separate clean Windows machine remain manual
release checks. Existing unrelated local presets with missing or machine-specific
paths are preserved; this migration does not repair those references.
