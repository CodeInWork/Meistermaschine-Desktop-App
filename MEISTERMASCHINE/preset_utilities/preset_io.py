# presets/preset_io.py

def save_mms(file, musicBtn_lst, settingBtn_lst, weatherBtn_lst, specialBtn_lst):
    with open(file, "w", encoding="utf-8") as f:
        for t, group in enumerate([musicBtn_lst, settingBtn_lst, weatherBtn_lst, specialBtn_lst]):
            for btn_idx, btn in enumerate(group):
                for song in btn.playlist:
                    f.write(f"{t} {btn_idx}\t{song[0]}\n")

def load_mms(file):
    result = {0: [], 1: [], 2: [], 3: []}
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            ids, path = line.split("\t")
            t, idx = map(int, ids.split())
            result[t].append((idx, path.strip()))
    return result

