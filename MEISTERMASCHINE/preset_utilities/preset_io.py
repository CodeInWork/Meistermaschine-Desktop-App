# presets/preset_io.py

def save_mms(file, music, setting, weather, special):
    with open(file, "w", encoding="utf-8") as f:
        for t, group in enumerate([music, setting, weather, special]):
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
