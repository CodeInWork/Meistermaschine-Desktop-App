
from PyQt6 import QtGui, QtWidgets
from MEISTERMASCHINE import GUI_qtDesign as gui
import sys
from pathlib import Path

def main():

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowIcon(QtGui.QIcon(str(Path(__file__).resolve().parent / "icons" / "icon_circle.png")))
    ui = gui.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
