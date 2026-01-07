# presets/preset_io.py

def save_mms(file, music, setting, weather, special):
    with open(file, "w", encoding="utf-8") as f:
        for t, group in enumerate([music, setting, weather, special]):
            for btn_idx, btn in enumerate(group):
                for song in btn.playlist:
                    f.write(f"{t} {btn_idx}\t{song[0]}\n")

def loadFile_mms(file):
    result = {0: [], 1: [], 2: [], 3: []}
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            ids, path = line.split("\t")
            t, idx = map(int, ids.split())
            result[t].append((idx, path.strip()))
    return result

def loadFile_mms(file: str):
        try:
            f = open(file, 'r',  encoding="utf-8")
        except FileNotFoundError:
            print('File not found') # ToDo: display error in status bar
        else:
            with f:
                data = f.readlines()
                self.clearAllPlaylists()
                for line in data:
                    splitLine = line.split("\t")
                    idLst = splitLine[0].split()
                    soundFile = splitLine[1].rstrip()
                    if int(idLst[0])==0:
                        self.musicBtn_lst[int(idLst[1])].addSongToPlaylist(soundFile) 
                    if int(idLst[0])==1:
                        self.settingBtn_lst[int(idLst[1])].addSongToPlaylist(soundFile)
                    if int(idLst[0])==2:
                        self.weatherBtn_lst[int(idLst[1])].addSongToPlaylist(soundFile)
                    if int(idLst[0])==3:
                        self.specialBtn_lst[int(idLst[1])].addSongToPlaylist(soundFile)