# audio/volume.py
from PyQt6 import QtCore, QtGui, QtWidgets, QtMultimedia

def dependent_volume(master: float, sub: float) -> float:
    dep = sub * master / 100
    return QtMultimedia.QAudio.convertVolume(
        dep / 100,
        QtMultimedia.QAudio.VolumeScale.LogarithmicVolumeScale,
        QtMultimedia.QAudio.VolumeScale.LinearVolumeScale
    )

#deprecated in favor of dependent_volume
def calculateDependentVolume(self, masterValue: float, subValue: float)-> float:
        depValue = subValue*masterValue / 100
        linDepVal = QtMultimedia.QAudio.convertVolume(depValue / 100, QtMultimedia.QAudio.VolumeScale.LogarithmicVolumeScale, QtMultimedia.QAudio.VolumeScale.LinearVolumeScale)
        return linDepVal