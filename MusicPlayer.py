import pygame
import os
from PyQt6 import QtCore, QtGui, QtWidgets

class MusicPlayer:
    def __init__(self, root) -> None:
        self.root = root
        self.playlist = root.currentSoundFilesListWidget
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = ""
        # Declaring Status Variable
        self.status = ""


    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        # It will Display the  Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()

