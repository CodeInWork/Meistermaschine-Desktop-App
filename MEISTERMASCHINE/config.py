MAX_PLAYLIST_LENGTH = 16

# variables and settings
btn_rows = 5
channel_count = 4
# default icons
musicIcon_lst = ["icons\\smiley_star.png","icons\\smiley_grin.png","icons\\smiley_neutral.png","icons\\smiley_scary.png","icons\\smiley_death.png"]
settingIcon_lst = ["icons\\pub.png","icons\\dorf.png","icons\\landschaft.png","icons\\hohle.png","icons\\kampf.png"]
weatherIcon_lst = ["icons\\nacht.png","icons\\welle.png","icons\\wind.png","icons\\sturm.png","icons\\schnee.png"]
specialIcon_lst = ["icons\\icon_square.png","icons\\icon_plus.png","icons\\icon_triangle.png","icons\\icon_minus.png","icons\\icon_star.png"]

# channel configuration for default values
CHANNEL_CONFIG = {
    "music": {
        "loop": True,
        "audio_index": 0,
        "max_playlist_length": MAX_PLAYLIST_LENGTH,
    },
    "setting": {
        "loop": True,
        "audio_index": 1,
        "max_playlist_length": MAX_PLAYLIST_LENGTH,
    },
    "weather": {
        "loop": True,
        "audio_index": 2,
        "max_playlist_length": MAX_PLAYLIST_LENGTH,
    },
    "special": {
        "loop": False,
        "audio_index": 3,
        "max_playlist_length": MAX_PLAYLIST_LENGTH,
    },
}

# accepted audio and icon file types
AUDIO_EXTS = (".mp3", ".wav", ".ogg", ".flac", ".m4a")
ICON_EXTS = (".png", ".jpg", ".jpeg", ".svg")