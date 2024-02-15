
from PyQt6 import QtGui, QtWidgets

import GUI_qtDesign as gui
import sys
import os

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowIcon(QtGui.QIcon(f"{os.getcwd()}\\icons\\icon_circle.png"))
    ui = gui.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
