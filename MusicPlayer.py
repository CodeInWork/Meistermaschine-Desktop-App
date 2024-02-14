import pygame


class MusicPlayer:
    def __init__(self) -> None:
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = None
        # Declaring Status Variable
        self.status = "-Stopped"


    def playsong(self, track):
        # Displaying Selected Song title
        self.track = track
        # Displaying Status
        self.status = "-Playing"
        # Loading Selected Song
        pygame.mixer.music.load(track)
        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
        # Displaying Status
        self.status = "-Stopped"
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        # Displaying Status
        self.status = "-Paused"
        # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        # It will Display the  Status
        self.status = "-Playing"
        # Playing back Song
        pygame.mixer.music.unpause()

