import ctypes
import os
from dataclasses import dataclass


DRIVE_REMOVABLE = 2


@dataclass
class RemovableDrive:
    path: str
    label: str


def find_removable_drives() -> list[RemovableDrive]:
    """
    Find all removable drives currently available on Windows.
    """

    drives = []

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        path = f"{letter}:\\"

        drive_type = ctypes.windll.kernel32.GetDriveTypeW(path)

        if drive_type != DRIVE_REMOVABLE:
            continue

        if not os.path.exists(path):
            continue

        label = _get_volume_label(path)

        drives.append(
            RemovableDrive(
                path=path,
                label=label,
            )
        )

    return drives


def _get_volume_label(path: str) -> str:
    """
    Return the Windows volume label of a drive.
    """

    volume_name = ctypes.create_unicode_buffer(261)

    success = ctypes.windll.kernel32.GetVolumeInformationW(
        path,
        volume_name,
        len(volume_name),
        None,
        None,
        None,
        None,
        0,
    )

    if success:
        return volume_name.value

    return ""