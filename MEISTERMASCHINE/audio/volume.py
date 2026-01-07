# audio/volume.py
from PyQt6.QtMultimedia import QAudio

def dependent_volume(master: float, sub: float) -> float:
    dep = sub * master / 100
    return QAudio.convertVolume(
        dep / 100,
        QAudio.VolumeScale.LogarithmicVolumeScale,
        QAudio.VolumeScale.LinearVolumeScale
    )