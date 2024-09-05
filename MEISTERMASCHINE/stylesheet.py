# app colors
green = "rgb(97, 195, 144)"
pale_green = "rgb(153, 255, 202)"
pale_blue = "rgb(53, 238, 255)"
blue = "rgb(3, 175, 255)"
yellow = "rgb(255, 205, 88)"
pale_pink = "rgb(255, 152, 231)"

black = "rgb(0,0,0)"
dark_gray = "rgb(80, 80, 80)"
gray = "rgb(149, 149, 149)"
white = "rgb(255,255,255)"

musicBtn_color = pale_green
settingBtn_color = yellow
weatherBtn_color = pale_blue
specialBtn_color = [pale_pink, pale_blue, yellow, pale_green, pale_pink]

# frames
CSS_Sound_Frame = f"background-color: {black}"
CSS_Utility_Frame = f"background-color:{black}"
CSS_Interface_Frame = f"background-color: {gray}"


# menu bar style sheet
CSS_menubar = f"""QMenuBar::item{{
        color: {white};
        background-color: transparent;
    }}
    QMenuBar {{
        background: {dark_gray};
    }}
"""
# status bar style sheet
CSS_statusbar = f"background-color: {dark_gray}"

# tool bar style sheet
CSS_toolbar = f"""QToolBar{{
        color: {white};
        border: 0px;
        background-color: {dark_gray};
    }}"""

# Sound control Buttons
CSS_Sound_Control_Btns = f"background-color:{green}"

# Root Folder Button
CSS_Root_Folder_Btn = f"background-color:{green}"

# Refresh SD Cards Button
CSS_Refresh_SD_Btn = f"background-color:{green}"

# Save To SD Button
CSS_Save_SD_Btn = f"background-color: {blue}"

# Clear Sum Button
CSS_Clear_Sum_Btn = f"""QPushButton{{
    background-color: {dark_gray};
    color:{white};
    }}"""

# List of found SD cards Combo Box
CSS_Found_SD_Combobox = f"background-color: {dark_gray}"

# Label
CSS_Label = f"color: {white}"

# slider style sheet
CSS_Slider = f"""QSlider::handle:horizontal {{
    background: {blue};
    border: 1px solid #565a5e;
    width: 24px;
    height: 8px;
    border-radius: 4px;
}}"""

# List View Style sheet
CSS_List = f"""QListWidget::item{{
    color: {white};
    background-color: transparent;
}}
QListWidget {{
    background-color: {dark_gray};
}}
QListWidget::item:selected {{
    background-color: {blue};
}}
"""

# List View Style sheet
CSS_ListView = f"""QTreeView::item{{
    color: {white};
    background-color: transparent;
}}
QTreeView {{
    background-color: {dark_gray};
    show-decoration-selected: 1;
}}
QTreeView::QScrollBar:horizontal {{
    border: 2px solid {gray};
    background: {dark_gray};
}}
"""

# ComboBox Style sheet
CSS_ComboBox = f"""QComboBox {{
    background-color: {dark_gray};
    color: {white};
}}
QListView::item {{
    color: {white};
    background-color: transparent;
}}
QComboBox QAbstractItemView {{
    background-color: {dark_gray};
    color = {white}
}}
"""

# Interface Buttons Style Sheets
# music button
CSS_PB_music = f"""QPushButton {{
    background-color: {musicBtn_color};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""

CSS_PB_setting = f"""QPushButton {{
    background-color: {settingBtn_color};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""

CSS_PB_weather = f"""QPushButton {{
    background-color: {weatherBtn_color};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""

CSS_PB_special_0 = f"""QPushButton {{
    background-color: {specialBtn_color[0]};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""
CSS_PB_special_1 = f"""QPushButton {{
    background-color: {specialBtn_color[1]};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""
CSS_PB_special_2 = f"""QPushButton {{
    background-color: {specialBtn_color[2]};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""
CSS_PB_special_3 = f"""QPushButton {{
    background-color: {specialBtn_color[3]};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""
CSS_PB_special_4 = f"""QPushButton {{
    background-color: {specialBtn_color[4]};
}}
QPushButton:checked{{
            background-color: {dark_gray};
            border: none; 
        }}
"""
CSS_PB_special_lst=[CSS_PB_special_0,CSS_PB_special_1,CSS_PB_special_2,CSS_PB_special_3,CSS_PB_special_4]

# sound slider
CSS_soundSlider = f"""QSlider::groove:horizontal {{
        background: {white};
        height: 40px;
    }}

    QSlider::sub-page:horizontal {{
        background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
            stop: 0 #66e, stop: 1 #bbf);
        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
            stop: 0 #bbf, stop: 1 #55f);
        height: 40px;
    }}

    QSlider::add-page:horizontal {{
        background: #fff;
        height: 40px;
    }}

    QSlider::handle:horizontal {{
        background: {dark_gray};
        border: 1px;
        width: 16px;
        margin-top: 0px;
        margin-bottom: 0px;
        border-radius: 0px;
    }}
"""

# tab widget style sheet
CSS_tabwidget = f"""QTabWidget::tab-bar{{
        border: 1px {dark_gray};
    }}
    QTabWidget{{
        background: {dark_gray}
    }}
    QTabBar::tab{{
        background: {dark_gray};
        color: {white};
        padding: 10 px;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        min-width: 20ex;
    }}
    QTabBar::tab::selected{{
        background: {dark_gray};
        margin-left: 4px;
        margin-right: 4px;
    }}
    QTabBar::tab:!selected {{
        margin-top: 6px; 
        
    }}
    QTabWidget::pane{{
        border: 2px solid {dark_gray};
    }}

    QTabBar::tab:first:selected {{
        margin-left: 0; 
    }}

    QTabBar::tab:last:selected {{
        margin-right: 0; 
    }}

    QTabBar::tab:only-one {{
        margin: 0;     
    }}
"""
# Dice Roll results style sheet
CSS_Dice_Roll_Text = f"""QLabel{{
        color: {white};
        border: 1px solid {white}; 
        font-size: 20px;
    }}
"""
CSS_Dice_Roll_Sum = f"""QLabel{{
        color: {white};
        border: 1px solid {dark_gray}; 
        font-size: 20px;
    }}
"""
CSS_Dice_Roll_Text_Big = f"""QLabel{{
        color: {white};
        border: 1px solid {white}; 
        font-size: 30px;
    }}
"""
CSS_Dice_Roll_Text_Blue= f"""QLabel{{
        color: {pale_blue};
        border: 1px solid {white}; 
        font-size: 30px;
    }}
"""
CSS_Dice_Roll_Text_Yellow= f"""QLabel{{
        color: {yellow};
        border: 1px solid {white}; 
        font-size: 30px;
    }}
"""
CSS_Dice_Roll_Text_Pink= f"""QLabel{{
        color: {pale_pink};
        border: 1px solid {white}; 
        font-size: 30px;
    }}
"""
# Dice QPushButton Stylesheets
CSS_Dice_Button_0 = f"""QPushButton {{
    background-color: {pale_pink};
    font-size: 20px;
}}
"""
CSS_Dice_Button_1 = f"""QPushButton {{
    background-color: {pale_blue};
    font-size: 20px;
}}
"""
CSS_Dice_Button_2 = f"""QPushButton {{
    background-color: {yellow};
    font-size: 20px;
}}
"""
CSS_Dice_Button_3 = f"""QPushButton {{
    background-color: {pale_green};
    font-size: 20px
}}
"""
CSS_Dice_Button_4 = f"""QPushButton {{
    background-color: {dark_gray};
    color: {white};
    font-size: 20px;
}}
"""