[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT') {
    throw 'Build the Windows distribution on Windows.'
}

Push-Location $PSScriptRoot
try {
    # Fail if pyproject.toml and uv.lock disagree; never update the lock.
    & uv sync --locked --group dev
    if ($LASTEXITCODE -ne 0) { throw 'uv sync failed.' }

    & uv run --no-sync python -m PyInstaller --noconfirm --clean cli.spec
    if ($LASTEXITCODE -ne 0) { throw 'PyInstaller build failed.' }

    Write-Host "Build complete: $PSScriptRoot/dist/Meistermaschine/Meistermaschine.exe"
    Write-Host 'Distribute the entire Meistermaschine folder, including _internal.'
}
finally {
    Pop-Location
}
