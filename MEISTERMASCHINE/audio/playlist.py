class Playlist:
    def __init__(self):
        self.tracks = []
        self.active = -1

    def add(self, path):
        self.tracks.append(path)

    def next(self):
        if not self.tracks:
            return None
        self.active = (self.active + 1) % len(self.tracks)
        return self.tracks[self.active]

# make buttons simply reference the playlist instead of making it part of the class
# btn.playlist = Playlist()