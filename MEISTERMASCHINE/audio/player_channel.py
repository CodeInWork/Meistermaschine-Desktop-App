from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6 import QtCore
import os

class PlayerChannel:
    def __init__(self, name: str, player: QMediaPlayer, buttons: list):
        self.name = name
        self.player = player
        self.buttons = buttons
        self.active_button = None

class PlayerController:
    def __init__(self):
        self.channels: dict[str, PlayerChannel] = {}

    def add_channel(self, channel):
        for btn in channel.buttons:
            if any(btn in ch.buttons for ch in self.channels.values()):
                raise ValueError("Button assigned to multiple channels")
        self.channels[channel.name] = channel


    def all_buttons(self):
        for ch in self.channels.values():
            yield from ch.buttons

    def clear_all_playlists(self):
        for btn in self.all_buttons():
            btn.playlist.clear()
            btn.playlist.active = -1

    def find_channel_for_button(self, btn):
        for ch in self.channels.values():
            if btn in ch.buttons:
                return ch
        raise RuntimeError("Button not assigned to any channel")
    
    def play_channel(self, channel, songFile, app_path, fromBeginning=True):
        player = channel.player
        path = os.path.join(app_path, songFile[0])
        player.setSource(QtCore.QUrl.fromLocalFile(path))
        if fromBeginning:
            player.setPosition(0)
        player.play()

    def stop_channel(self, channel):
        if channel.active_button:
            channel.player.stop()
            channel.active_button.setChecked(False)
            channel.active_button = None

    def stop_all_channels(self):
        for channel in self.channels.values():
            self.stop_channel(channel)

    def pause_channel(self, channel):
        if channel.player.playbackState() == channel.player.PlaybackState.PlayingState:
            channel.player.pause()

    def stop_button(self, btn):
        channel = self.find_channel_for_button(btn)
        if channel.active_button is btn:
            self.stop_channel(channel)

