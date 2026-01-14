from PyQt6 import QtCore, QtMultimedia
import os

class PlayerChannel:
    def __init__(self, name: str, player: QtMultimedia.QMediaPlayer, buttons: list):
        self.name = name
        self.player = player
        self.buttons = buttons
        self.active_button = None
        self.paused = False

class PlayerController:
    def __init__(self):
        self.channels: dict[str, PlayerChannel] = {}
        self._switching = False

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
        if self._switching:
            return

        self._switching = True
        
        try:
            player = channel.player
            path = os.path.join(app_path, songFile[0])
            player.setSource(QtCore.QUrl.fromLocalFile(path))
            if fromBeginning:
                player.setPosition(0)
            player.play()
        finally:
            self._switching = False
            

    def stop_channel(self, channel):
        if channel.active_button:
            btn = channel.active_button

            channel.player.stop()

            btn.blockSignals(True)
            btn.setChecked(False)
            btn.blockSignals(False)

            channel.active_button = None
            channel.paused = False

    def stop_all_channels(self):
        for channel in self.channels.values():
            self.stop_channel(channel)

    def stop_button(self, btn):
        channel = self.find_channel_for_button(btn)
        if channel.active_button is btn:
            self.stop_channel(channel)

    def pause_channel(self, channel):
        if channel.player.playbackState() == channel.player.PlaybackState.PlayingState:
            channel.player.pause()
            channel.paused = True

    def resume_channel(self, channel):
        if channel.paused:
            channel.player.play()
            channel.paused = False

    def reorder_playlist(self, channel, old_index, new_index, app_path: str):
        was_playing = channel.player.playbackState() == QtMultimedia.QMediaPlayer.PlaybackState.PlayingState

        activeBtn = channel.active_button
        self.stop_channel(channel)

        if not activeBtn:
            return

        activeBtn.playlist.move(old_index, new_index)

        if was_playing:
            track = channel.active_button.playlist.current()
            if track:
                self.play_channel(channel, track, app_path, fromBeginning=False)




