import os

def btn_assign_playlist(
    musicBtn_lst, settingBtn_lst, weatherBtn_lst, specialBtn_lst, btn_occupancy: dict
):
    music_lst = btn_occupancy.get(0)
    for entry in music_lst:
        title = os.path.splitext(os.path.basename(entry[1]))[0]
        musicBtn_lst[entry[0]].playlist.add(entry[1], title)

    setting_lst = btn_occupancy.get(1)
    for entry in setting_lst:
        title = os.path.splitext(os.path.basename(entry[1]))[0]
        settingBtn_lst[entry[0]].playlist.add(entry[1], title)

    weather_lst = btn_occupancy.get(2)
    for entry in weather_lst:
        title = os.path.splitext(os.path.basename(entry[1]))[0]
        weatherBtn_lst[entry[0]].playlist.add(entry[1], title)

    special_lst = btn_occupancy.get(3)
    for entry in special_lst:
        title = os.path.splitext(os.path.basename(entry[1]))[0]
        specialBtn_lst[entry[0]].playlist.add(entry[1], title)

def handle_playlist_cleared(btn, active_btn):
    """
    Returns instructions for what the UI/controller should do.
    """
    actions = []

    if btn.is_active:
        actions.append("stop_player")

    if btn is active_btn:
        actions.append("clear_playlist_view")

    return actions


