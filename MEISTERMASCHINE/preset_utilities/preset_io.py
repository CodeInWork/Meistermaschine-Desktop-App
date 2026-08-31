# presets/preset_io.py

import json
from pathlib import Path

# *.mms files are for SD cards used in the physical Meistermaschine
def save_mms(
    file,
    musicBtn_lst,
    settingBtn_lst,
    weatherBtn_lst,
    specialBtn_lst,
    path_transform=None,
):
    groups = [
        musicBtn_lst,
        settingBtn_lst,
        weatherBtn_lst,
        specialBtn_lst,
    ]

    with open(file, "w", encoding="utf-8") as f:
        for channel_idx, group in enumerate(groups):
            for button_idx, button in enumerate(group):
                for song in button.playlist.tracks:
                    track_path = song[0]

                    if path_transform is not None:
                        track_path = path_transform(track_path)

                    f.write(
                        f"{channel_idx} {button_idx}\t"
                        f"{track_path}\n"
                    )

def load_mms(file):
    result = {0: [], 1: [], 2: [], 3: []}
    
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            ids, path = line.split("\t")
            t, idx = map(int, ids.split())
            result[t].append((idx, path.strip()))
    return result

# *.json presets hold audio and icon information needed by the App
def save_preset_json(controller, path):
    data = {"version": 1, "channels": {}}

    for name, channel in controller.channels.items():
        buttons = []
        for idx, btn in enumerate(channel.buttons):
            buttons.append({
                "index": idx,
                "icon": getattr(btn, "icon_path", None),
                "playlist": [p for (p, _t) in btn.playlist.tracks],
            })
        data["channels"][name] = {"buttons": buttons}

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_preset_json(controller, path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for name, ch_data in data["channels"].items():
        channel = controller.channels.get(name)
        if not channel:
            continue

        for btn_data in ch_data["buttons"]:
            idx = btn_data["index"]
            if idx >= len(channel.buttons):
                continue

            btn = channel.buttons[idx]

            btn.playlist.clear()
            for item in btn_data.get("playlist", []):
                track_path = _track_path_from_json(item)
                btn.playlist.add(track_path)

            icon = btn_data.get("icon")
            if icon:
                btn.set_button_icon(icon)

def _track_path_from_json(item):
    # Accept "path" as str
    if isinstance(item, str):
        return item

    # Accept ["path", "title"] or ("path", "title")
    if isinstance(item, (list, tuple)) and item:
        if isinstance(item[0], str):
            return item[0]

    # Accept {"path": "..."} (or {"file": "..."})
    if isinstance(item, dict):
        p = item.get("path") or item.get("file")
        if isinstance(p, str):
            return p

    return None


def get_sd_audio_filename(source_path: str | Path) -> str:
    return Path(source_path).with_suffix(".mp3").name