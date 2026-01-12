import os

# audio/playlist.py
class Playlist:
    def __init__(self, max_length=40):
        self.max_length = max_length
        self.tracks: list[tuple[str, str]] = []
        self.active = -1

    def add(self, path: str):
        title = self.extractTitle(path)
        if len(self.tracks) >= self.max_length:
            self.tracks[0] = (path, title)
        else:
            self.tracks.append((path, title))

    def clear(self):
        self.tracks.clear()
        self.active = -1

    def current(self):
        if not self.tracks:
            return None
        if self.active == -1:
            self.active = 0
        return self.tracks[self.active]

    def next(self):
        if not self.tracks:
            return None
        self.active = (self.active + 1) % len(self.tracks)
        return self.current()

    def previous(self):
        if not self.tracks:
            return None
        self.active = (self.active - 1) % len(self.tracks)
        return self.current()

    def remove(self, index):
        track = self.tracks.pop(index)
        if not self.tracks:
            self.active = -1
        else:
            self.active = min(index, len(self.tracks) - 1)
        return track
    
    def extractTitle(self, path: str) -> str:
        return os.path.splitext(os.path.basename(path))[0]


# make buttons simply reference the playlist instead of making it part of the class
# btn.playlist = Playlist()