# Form implementation generated from reading ui file 'GUI_qtDesign.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

# app colors
green = "rgb(97, 195, 144)"
pale_green = "rgb(153, 255, 202)"
pale_blue = "rgb(53, 238, 255)"
blue = "rgb(3, 175, 255)"
yellow = "rgb(255, 205, 88)"
pale_pink = "rgb(255, 152, 231)"



black = "rgb(0,0,0)"
dark_gray = "rgb(88, 88, 88)"
gray = "rgb(149, 149, 149)"
white = "rgb(255,255,255)"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ########################################################################################################
        # variables and settings
        self.btn_rows = 5
        self.musicIcon_lst = ["star-struck","grinning","expressionless","scream","skull_and_crossbones"]
        self.musicBtn_color = pale_green
        self.settingIcon_lst = ["pub","dorf","landschaft","hohle","kampf"]
        self.settingBtn_color = yellow
        self.wheatherIcon_lst = ["nacht","welle","wind","sturm","schnee"]
        self.wheatherBtn_color = pale_blue
        #self.specialIcon_lst = ["sonne","nacht","wind","sturm","schnee"]
        self.specialBtn_color = [pale_pink, pale_blue, yellow, pale_green, pale_pink]
        
        # slider style sheet
        CSS = f"""QSlider::handle:horizontal {{
            background: {blue};
            border: 1px solid #565a5e;
            width: 24px;
            height: 8px;
            border-radius: 4px;
        }}"""

        # ComboBox Style sheet
        CSS2 = f"""QListWidget::item{{
            color: {white};
            background-color: {dark_gray};
        }}"""

        # main window 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")

        ########################################################################################################
        # Sound Control Frame

        self.Sound_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.Sound_frame.setGeometry(QtCore.QRect(0, 449, 800, 151))
        self.Sound_frame.setStyleSheet(f"background-color: {black}")
        self.Sound_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Sound_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Sound_frame.setObjectName("Sound_frame")
        
        self.pauseButton = QtWidgets.QPushButton(parent=self.Sound_frame)
        self.pauseButton.setGeometry(QtCore.QRect(170, 30, 75, 51))
        self.pauseButton.setStyleSheet(f"background-color:{green}")
        self.pauseButton.setObjectName("pauseButton")
        
        self.stopButton = QtWidgets.QPushButton(parent=self.Sound_frame)
        self.stopButton.setGeometry(QtCore.QRect(290, 30, 75, 51))
        self.stopButton.setStyleSheet(f"background-color:{green}")
        self.stopButton.setObjectName("stopButton")

        self.playButton = QtWidgets.QPushButton(parent=self.Sound_frame)
        self.playButton.setGeometry(QtCore.QRect(50, 30, 75, 51))
        self.playButton.setStyleSheet(f"background-color:{green}")
        self.playButton.setObjectName("playButton")

        self.masterVolumeSlider = QtWidgets.QSlider(parent=self.Sound_frame)
        self.masterVolumeSlider.setGeometry(QtCore.QRect(390, 60, 160, 18))
        self.masterVolumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.masterVolumeSlider.setStyleSheet(CSS)
        self.masterVolumeSlider.setObjectName("masterVolumeSlider")
        self.masterVolumeSlider.setValue(self.masterVolumeSlider.maximum())   #initial setting = max
        self.masterVolumeSlider.valueChanged[int].connect(self.sliderTest)

        self.masterVolumeLabel = QtWidgets.QLabel(parent=self.Sound_frame)
        self.masterVolumeLabel.setGeometry(QtCore.QRect(420, 80, 91, 16))
        self.masterVolumeLabel.setStyleSheet(f"color: {white}")
        self.masterVolumeLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.masterVolumeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.masterVolumeLabel.setObjectName("masterVolumeLabel")

        self.currentSoundFilesListWidget = QtWidgets.QListWidget(parent=self.Sound_frame)
        self.currentSoundFilesListWidget.setGeometry(QtCore.QRect(620, 20, 141, 71))
        #self.currentSoundFilesListWidget.setStyleSheet(f"background-color:{dark_gray}")
        self.currentSoundFilesListWidget.setStyleSheet(CSS2)
        self.currentSoundFilesListWidget.setObjectName("currentSoundFilesListWidget")

        self.soundProgressBar = QtWidgets.QProgressBar(parent=self.Sound_frame)
        self.soundProgressBar.setGeometry(QtCore.QRect(390, 27, 160, 16))
        self.soundProgressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.soundProgressBar.setProperty("value", 24)
        self.soundProgressBar.setObjectName("progressBar")

        ########################################################################################################
        # SD card frame

        self.SDframe = QtWidgets.QFrame(parent=self.centralwidget)
        self.SDframe.setGeometry(QtCore.QRect(800, 0, 200, 600))
        self.SDframe.setStyleSheet(f"background-color:{black}")
        self.SDframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.SDframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.SDframe.setObjectName("SDframe")

        self.fileTreeListView = QtWidgets.QListView(parent=self.SDframe)
        self.fileTreeListView.setGeometry(QtCore.QRect(10, 50, 180, 361))
        self.fileTreeListView.setStyleSheet(f"background-color:{dark_gray}")
        self.fileTreeListView.setObjectName("fileTreeListView")

        self.getRootFolderButton = QtWidgets.QPushButton(parent=self.SDframe)
        self.getRootFolderButton.setGeometry(QtCore.QRect(10, 10, 111, 24))
        self.getRootFolderButton.setStyleSheet(f"background-color:{green}")
        self.getRootFolderButton.setObjectName("getRootFolderButton")

        self.saveToSDButton = QtWidgets.QPushButton(parent=self.SDframe)
        self.saveToSDButton.setGeometry(QtCore.QRect(110, 500, 81, 24))
        self.saveToSDButton.setStyleSheet(f"background-color: {blue}")
        self.saveToSDButton.setObjectName("saveToSDButton")

        self.listOfFoundSDCardsCombobox = QtWidgets.QComboBox(parent=self.SDframe)
        self.listOfFoundSDCardsCombobox.setGeometry(QtCore.QRect(10, 470, 180, 22))
        self.listOfFoundSDCardsCombobox.setStyleSheet(f"background-color: {dark_gray}")
        self.listOfFoundSDCardsCombobox.setObjectName("listOfFoundSDCardsCombobox")

        self.SDcardsLabel = QtWidgets.QLabel(parent=self.SDframe)
        self.SDcardsLabel.setGeometry(QtCore.QRect(10, 450, 49, 16))
        self.SDcardsLabel.setStyleSheet(f"color: {white}")
        self.SDcardsLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.SDcardsLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SDcardsLabel.setObjectName("SDcardsLabel")

        self.refreshButton = QtWidgets.QPushButton(parent=self.SDframe)
        self.refreshButton.setGeometry(QtCore.QRect(10, 500, 51, 24))
        self.refreshButton.setStyleSheet(f"background-color: {green}")
        self.refreshButton.setObjectName("refreshButton")

        #########################################################################################################
        # main interface frame (Audio Buttons)
        
        self.interfaceFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.interfaceFrame.setGeometry(QtCore.QRect(0, 0, 800, 450))
        self.interfaceFrame.setStyleSheet(f"background-color: {gray}")
        self.interfaceFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.interfaceFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.interfaceFrame.setObjectName("interfaceFrame")

        self.layoutWidget = QtWidgets.QWidget(parent=self.interfaceFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 360))
        self.layoutWidget.setObjectName("layoutWidget")

        self.mainButtonGridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.mainButtonGridLayout.setContentsMargins(0, 20, 0, 0)
        self.mainButtonGridLayout.setObjectName("mainButtonGridLayout")

        # Button configurations 
        font = QtGui.QFont()
        font.setPointSize(16)     
          
        # music Buttons
        self.musicBtn_lst = [QtWidgets.QPushButton(parent=self.layoutWidget) for b in range(self.btn_rows)]
        for btn in self.musicBtn_lst:
            btn.setMaximumSize(QtCore.QSize(75, 75))
            btn.setFont(font)
            btn.setStyleSheet(f"background-color:{self.musicBtn_color}")
            btn.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f"icons/{self.musicIcon_lst[self.musicBtn_lst.index(btn)]}.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            btn.setIcon(icon)
            btn.setIconSize(QtCore.QSize(50, 50))
            btn.setObjectName(f"musicBtn_{self.musicBtn_lst.index(btn)+1}")
            self.mainButtonGridLayout.addWidget(btn, self.musicBtn_lst.index(btn), 0, 1, 1)

        # setting Buttons
        self.settingBtn_lst = [QtWidgets.QPushButton(parent=self.layoutWidget) for b in range(self.btn_rows)]
        for btn in self.settingBtn_lst:
            btn.setMaximumSize(QtCore.QSize(75, 75))
            btn.setFont(font)
            btn.setStyleSheet(f"background-color:{self.settingBtn_color}")
            btn.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f"icons/{self.settingIcon_lst[self.settingBtn_lst.index(btn)]}.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            btn.setIcon(icon)
            btn.setIconSize(QtCore.QSize(50, 50))
            btn.setObjectName(f"settingBtn_{self.settingBtn_lst.index(btn)+1}")
            self.mainButtonGridLayout.addWidget(btn, self.settingBtn_lst.index(btn), 1, 1, 1)

        # wheather Buttons
        self.wheatherBtn_lst = [QtWidgets.QPushButton(parent=self.layoutWidget) for b in range(self.btn_rows)]
        for btn in self.wheatherBtn_lst:
            btn.setMaximumSize(QtCore.QSize(75, 75))
            btn.setFont(font)
            btn.setStyleSheet(f"background-color:{self.wheatherBtn_color}")
            btn.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f"icons/{self.wheatherIcon_lst[self.wheatherBtn_lst.index(btn)]}.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            btn.setIcon(icon)
            btn.setIconSize(QtCore.QSize(50, 50))
            btn.setObjectName(f"wheatherBtn_{self.wheatherBtn_lst.index(btn)+1}")
            self.mainButtonGridLayout.addWidget(btn, self.wheatherBtn_lst.index(btn), 2, 1, 1)

        # special Buttons
        self.specialBtn_lst = [QtWidgets.QPushButton(parent=self.layoutWidget) for b in range(self.btn_rows)]
        for btn in self.specialBtn_lst:
            btn.setMaximumSize(QtCore.QSize(75, 75))
            btn.setFont(font)
            btn.setStyleSheet(f"background-color:{self.specialBtn_color[self.specialBtn_lst.index(btn)]}")
            btn.setText(f"{self.specialBtn_lst.index(btn)+1}")
            #icon = QtGui.QIcon()
            #icon.addPixmap(QtGui.QPixmap(f"icons/{self.specialIcon_lst[self.specialBtn_lst.index(btn)]}.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            #btn.setIcon(icon)
            #btn.setIconSize(QtCore.QSize(50, 50))
            btn.setObjectName(f"specialBtn_{self.specialBtn_lst.index(btn)+1}")
            self.mainButtonGridLayout.addWidget(btn, self.specialBtn_lst.index(btn), 3, 1, 1)    

        # individual volume sliders
        self.musicVolumeSlider = QtWidgets.QSlider(parent=self.interfaceFrame)
        self.musicVolumeSlider.setGeometry(QtCore.QRect(79, 380, 111, 20))
        self.musicVolumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.musicVolumeSlider.setStyleSheet(CSS)
        self.musicVolumeSlider.setObjectName("musicVolumeSlider")
        self.musicVolumeSlider.setValue(self.musicVolumeSlider.maximum())   #initial setting = max

        self.settingVolumeSlider = QtWidgets.QSlider(parent=self.interfaceFrame)
        self.settingVolumeSlider.setGeometry(QtCore.QRect(260, 380, 111, 20))
        self.settingVolumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.settingVolumeSlider.setStyleSheet(CSS)
        self.settingVolumeSlider.setObjectName("settingVolumeSlider")
        self.settingVolumeSlider.setValue(self.settingVolumeSlider.maximum())   #initial setting = max

        self.weatherVolumeSlider = QtWidgets.QSlider(parent=self.interfaceFrame)
        self.weatherVolumeSlider.setGeometry(QtCore.QRect(430, 380, 111, 20))
        self.weatherVolumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.weatherVolumeSlider.setStyleSheet(CSS)
        self.weatherVolumeSlider.setObjectName("weatherVolumeSlider")
        self.weatherVolumeSlider.setValue(self.weatherVolumeSlider.maximum())   #initial setting = max

        self.specialVolumeSlider = QtWidgets.QSlider(parent=self.interfaceFrame)
        self.specialVolumeSlider.setGeometry(QtCore.QRect(610, 380, 111, 20))
        self.specialVolumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.specialVolumeSlider.setStyleSheet(CSS)
        self.specialVolumeSlider.setObjectName("specialVolumeSlider")
        self.specialVolumeSlider.setValue(self.specialVolumeSlider.maximum())   #initial setting = max

        self.musicMuffleButton = QtWidgets.QPushButton(parent=self.interfaceFrame)
        self.musicMuffleButton.setGeometry(QtCore.QRect(115, 410, 31, 24))
        self.musicMuffleButton.setStyleSheet(f"background-color: {dark_gray}")
        self.musicMuffleButton.setText("")
        self.musicMuffleButton.setObjectName("musicMuffleButton")

        self.settingMuffleButton = QtWidgets.QPushButton(parent=self.interfaceFrame)
        self.settingMuffleButton.setGeometry(QtCore.QRect(295, 410, 31, 24))
        self.settingMuffleButton.setStyleSheet(f"background-color: {dark_gray}")
        self.settingMuffleButton.setText("")
        self.settingMuffleButton.setObjectName("settingMuffleButton")

        self.weatherMuffleButton = QtWidgets.QPushButton(parent=self.interfaceFrame)
        self.weatherMuffleButton.setGeometry(QtCore.QRect(470, 410, 31, 24))
        self.weatherMuffleButton.setStyleSheet(f"background-color: {dark_gray}")
        self.weatherMuffleButton.setText("")
        self.weatherMuffleButton.setObjectName("weatherMuffleButton")

        self.specialMuffleButton = QtWidgets.QPushButton(parent=self.interfaceFrame)
        self.specialMuffleButton.setGeometry(QtCore.QRect(650, 410, 31, 24))
        self.specialMuffleButton.setStyleSheet(f"background-color: {dark_gray}")
        self.specialMuffleButton.setText("")
        self.specialMuffleButton.setObjectName("specialMuffleButton")

        self.muffle_label = QtWidgets.QLabel(parent=self.interfaceFrame)

        self.muffle_label.setGeometry(QtCore.QRect(48, 410, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.muffle_label.setFont(font)
        self.muffle_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.muffle_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.muffle_label.setObjectName("label_3")

        qss = """
        QMenuBar {
            background-color: red;
        }
        QMenuBar::item {
            background-color: black;
        }
        QMenuBar::item:selected {    
            background-color: rgb(244,164,96);
        }
        QMenuBar::item:pressed {
            background: rgb(128,0,0);
        }"""
        qss2= """
        QMenuBar {
            background-color: rgb(49,49,49);
            color: rgb(255,255,255);
            border: 1px solid #000;
        }

        QMenuBar::item {
            background-color: rgb(49,49,49);
            color: rgb(255,255,255);
        }

        QMenuBar::item::selected {
            background-color: rgb(30,30,30);
        }

        QMenu {
            background-color: rgb(49,49,49);
            color: rgb(255,255,255);
            border: 1px solid #000;           
        }

        QMenu::item::selected {
            background-color: rgb(30,30,30);
        }
        """
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setStyleSheet(f"background-color: {dark_gray}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # button action definitions

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Meistermaschine "))
        # audio control (sound_frame)
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.masterVolumeLabel.setText(_translate("MainWindow", "Master Volume"))
        
        # SD card control (SD_frame)
        self.getRootFolderButton.setText(_translate("MainWindow", "Change Folder"))
        self.saveToSDButton.setText(_translate("MainWindow", "Save to SD"))
        self.SDcardsLabel.setText(_translate("MainWindow", "SD cards"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))

        # main interface buttons (interface_fram)
        #self.musicBtn_3.setText(_translate("MainWindow", "3"))
        #self.musicBtn_4.setText(_translate("MainWindow", "4"))
        #self.musicBtn_5.setText(_translate("MainWindow", "5"))

        #self.settingBtn_1.setText(_translate("MainWindow", "6"))
        #self.musicBtn_7.setText(_translate("MainWindow", "7"))
        #self.musicBtn_8.setText(_translate("MainWindow", "8"))
        #self.musicBtn_9.setText(_translate("MainWindow", "9"))
        #self.musicBtn_10.setText(_translate("MainWindow", "10"))

        #self.musicBtn_11.setText(_translate("MainWindow", "11"))
        #self.musicBtn_12.setText(_translate("MainWindow", "12"))
        #self.musicBtn_13.setText(_translate("MainWindow", "13"))
        #self.musicBtn_14.setText(_translate("MainWindow", "14"))
        #self.musicBtn_15.setText(_translate("MainWindow", "15"))
        
        #self.musicBtn_16.setText(_translate("MainWindow", "16"))
        #self.musicBtn_17.setText(_translate("MainWindow", "17"))
        #self.musicBtn_18.setText(_translate("MainWindow", "18"))
        #self.musicBtn_19.setText(_translate("MainWindow", "19"))
        #self.musicBtn_20.setText(_translate("MainWindow", "20"))
        
        self.muffle_label.setText(_translate("MainWindow", "Muffle:"))

    def sliderTest(self, value):
        self.currentSoundFilesListWidget.addItem(str(value))

