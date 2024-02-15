import pygame
import time


class MusicPlayer:
    def __init__(self) -> None:
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = None
        self.playlist = []
        # Declaring Status Variable
        self.status = "-Stopped"
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
       
       """ while True:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    track_idx = self.getCurrenTrackIndex()
                    playlist_len = len(self.playlist)
                    if track_idx+1 >= playlist_len:
                        self.track = self.playlist[0]
                        pygame.mixer.music.queue(self.playlist[0])
                    else:
                        self.track = self.playlist[track_idx+1]
                        pygame.mixer.music.queue(self.playlist[track_idx+1])

            time.sleep(0.5)
"""
    def getCurrenTrackIndex(self)->int:
        return self.playlist.index(self.track) 

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

    def addToPlaylist(self, playlist: list)->None:
        for soundFile in playlist:
            self.playlist.append(soundFile)

    def clearPlayList(self)->None:
        self.playlist.clear()

    def deleteSongFromPlaylist(self, idx)->None:
        self.playlist.pop(idx)

