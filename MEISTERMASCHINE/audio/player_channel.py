from PyQt6 import QtCore, QtMultimedia
import os

class PlayerChannel:
    def __init__(self, name: str, player: QtMultimedia.QMediaPlayer, audio_output, loop=False, max_playlist_length=40):
        self.name = name
        self.player = player
        self.audio_output = audio_output
        self.loop = loop
        self.max_playlist_length = max_playlist_length

        self.buttons = []
        self.active_button = None
        self.paused = False

    def get_next_track(self):
        if not self.active_button:
            return None

        playlist = self.active_button.playlist

        # Normal forward
        if playlist.has_next():
            return playlist.next()

        # End reached → loop?
        if self.loop and playlist.tracks:
            playlist.active = 0
            return playlist.current()

        # End reached, no loop
        return None

    def play_track_at_index(self, index, app_path, controller):
        if not self.active_button:
            return

        playlist = self.active_button.playlist
        playlist.set_active(index)
        song = playlist.current()
        if song:
            controller.switch_track(self, song, app_path)



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

    def switch_track(self, channel, track, app_path, fromBeginning=True):
        channel.player.stop()
        channel.paused = False
        QtCore.QTimer.singleShot(
            0,
            lambda: self.play_channel(channel, track, app_path, fromBeginning)
        )

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

    def deactivate_channel(self, channel):
        btn = channel.active_button
        if not btn:
            return

        # 🔒 Clear logical state FIRST
        channel.active_button = None
        channel.paused = False

        # 🔕 Block UI feedback
        btn.blockSignals(True)
        btn.setChecked(False)
        btn.blockSignals(False)

        # 🛑 Stop last (may emit signals, but state is already clean)
        channel.player.stop()



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

    def remove_track_from_channel(self, channel, index, app_path):
        btn = channel.active_button
        if not btn:
            return

        playlist = btn.playlist
        was_active = index == playlist.active

        playlist.remove_at(index)

        if playlist.current() is None:
            self.stop_channel(channel)
            btn.setChecked(False)
            return

        if was_active:
            self.switch_track(channel, playlist.current(), app_path)




