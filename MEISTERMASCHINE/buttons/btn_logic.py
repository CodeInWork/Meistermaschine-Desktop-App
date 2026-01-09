def btn_assign_playlist(
    musicBtn_lst, settingBtn_lst, weatherBtn_lst, specialBtn_lst, btn_occupancy: dict
):
    music_lst = btn_occupancy.get(0)
    for entry in music_lst:
        musicBtn_lst[entry[0]].addSongToPlaylist(entry[1])

    setting_lst = btn_occupancy.get(1)
    for entry in setting_lst:
        settingBtn_lst[entry[0]].addSongToPlaylist(entry[1])

    weather_lst = btn_occupancy.get(2)
    for entry in weather_lst:
        weatherBtn_lst[entry[0]].addSongToPlaylist(entry[1])

    special_lst = btn_occupancy.get(3)
    for entry in special_lst:
        specialBtn_lst[entry[0]].addSongToPlaylist(entry[1])


