import os
import sys

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(__file__)

default_soundpath = os.path.normpath('c:\\Users\\Paul\\OneDrive\\Documents\\Projekte\\Meistermaschine-Desktop-App\\MEISTERMASCHINE\\sounds')
print(default_soundpath)
splitPath = os.path.normpath("/sounds/Musik/medieval&fantasy/Medieval Music Wild Boar's Inn.mp3")
print(splitPath)


file = f"{os.path.dirname(default_soundpath)}{splitPath}"

print(file)

