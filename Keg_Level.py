# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Keg_Level.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

LevelStyle = "QProgressBar {background-color: rgb(79, 61, 25); border-radius:7px;} QProgressBar::chunk {background-color: rgb(255,198,83);}"
FrameStyle = "border-top:2px solid black; border-left:2px solid black; border-right:4px solid black; border-bottom:4px solid black; background-color: rgb(165, 147, 116);border-radius:7px;"

class _qprogressbar(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(218, 270, 33, 430))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet(LevelStyle)
        self.setProperty("value", 0)
        self.setTextVisible(False)
        self.setOrientation(QtCore.Qt.Vertical)

class _beerlabel(QtWidgets.QLabel):
    def __init__(self, parent=None, xpos=0, ypos=0, xsize=0, ysize=0, fontsize=0, ):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(xpos, ypos, xsize, ysize))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(fontsize)
        self.setFont(font)
        self.setTextFormat(QtCore.Qt.AutoText)
        self.setAlignment(QtCore.Qt.AlignCenter)

     

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(223, 217, 199);")
        MainWindow.setWindowTitle("Keg Leveler")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")

        # Set up some empty lists to contain objects later on
        self.Beer_Label1 = []
        self.Beer_Label2 = []
        self.Keg_Level_Back = []
        self.Keg_Level_Bar = []
        self.ABV_Label = []
        self.IBU_Label = []
        self.SRM_Label = []
        self.Brew_Date_Label = []
        self.Keg_Date_Label = []
        self.Keg_Volume_Label = []
        self.Keg_Qty_Label = []
        self.Mugs_Label = []
        
        # Create banner at top of Window
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1730, 0, 191, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Documents/Beer/Mad Spaniel.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(770, 10, 380, 120))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 140, 30))
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText("Welcome")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 35, 140, 30))
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("to")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 65, 340, 50))
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setText("Mad Spaniel Brewery")
        self.label_4.setObjectName("label_4")
        
        # Create frame to hold Keg displays
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(30, 170, 1860, 901))
        self.frame_main.setStyleSheet("background-color: rgb(205, 196, 170);")
        self.frame_main.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_main.setLineWidth(6)
        self.frame_main.setMidLineWidth(0)
        self.frame_main.setObjectName("frame_main")


        # Set up first Keg Widgets
        # Create tne Master frame for this keg
        self.frame_Keg_0 = QtWidgets.QFrame(self.frame_main) 
        self.frame_Keg_0.setGeometry(QtCore.QRect(10, 10, 460, 850))
        self.frame_Keg_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Keg_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Keg_0.setObjectName("frame_Keg_0")

        # Create a frame for the Beer Name display
        self.Name_Frame_0 = QtWidgets.QFrame(self.frame_Keg_0)
        self.Name_Frame_0.setGeometry(QtCore.QRect(30, 10, 400, 85))
        self.Name_Frame_0.setAutoFillBackground(False)
        self.Name_Frame_0.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.Name_Frame_0.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Name_Frame_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Name_Frame_0.setLineWidth(1)
        self.Name_Frame_0.setObjectName("Name_Frame_0")

        # Set up Beer Name
        self.Beer_Label1.append(_beerlabel(self.Name_Frame_0, 25, 10, 350, 35, 26))
        self.Beer_Label1[0].setObjectName("Beer_Label_1")
        self.Beer_Label2.append(_beerlabel(self.Name_Frame_0, 25, 45, 350, 35, 26))
        self.Beer_Label2[0].setObjectName("Beer_Label_2")

        # Create area for Beer Details (Above the Keg)
        self.frame_3 = QtWidgets.QFrame(self.frame_Keg_0)
        self.frame_3.setGeometry(QtCore.QRect(30, 100, 400, 80))
        self.frame_3.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(40, 10, 40, 25))
        font.setBold(False)
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setText("ABV:")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(160, 10, 40, 25))
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setText("IBU:")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(260, 10, 47, 25))
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setText("SRM:")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(25, 30, 100, 25))
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setText("Brew Date: ")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(25, 50, 100, 25))
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setText("Keg Date: ")
        self.label_11.setObjectName("label_11")

        # Display ABV
        self.ABV_Label.append(_beerlabel(self.frame_3, 80, 10, 35, 25, 12))
        self.ABV_Label[0].setObjectName("ABV_Label_0")

        # Display IBU
        self.IBU_Label.append(_beerlabel(self.frame_3, 200, 10, 35, 25, 12))
        self.IBU_Label[0].setObjectName("IBU_Label_0")

        # Display SRM
        self.SRM_Label.append(_beerlabel(self.frame_3, 300, 10, 35, 25, 12))
        self.SRM_Label[0].setObjectName("SRM_Label_0")
        
        # Display Brew Date
        self.Brew_Date_Label.append(_beerlabel(self.frame_3, 140, 30, 150, 25, 12))
        self.Brew_Date_Label[0].setObjectName("Brew_Date_Label_0")
          
        # Display Date beer was Kegged
        self.Keg_Date_Label.append(_beerlabel(self.frame_3, 140, 50, 150, 25, 12))        
        self.Keg_Date_Label[0].setObjectName("Keg_Date_Label_0")

        # Display Keg Image
        self.label_5 = QtWidgets.QLabel(self.frame_Keg_0)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        
        # Create Background for Fill Level Progress Bar
        self.Keg_Fill_Level = QtWidgets.QLabel(self.frame_Keg_0)
        self.Keg_Fill_Level.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.Keg_Fill_Level.setStyleSheet(FrameStyle)
        self.Keg_Fill_Level.setObjectName("Keg_Fill_Level")

        # Create Progress Bar
        self.Keg_Level_Bar.append(_qprogressbar(self.frame_Keg_0)) 
        self.Keg_Level_Bar[0].setObjectName("Keg_Level_Bar[0]")
        
        # Create Area to display Keg Level Details below Keg image
        self.frame_2 = QtWidgets.QFrame(self.frame_Keg_0)
        self.frame_2.setGeometry(QtCore.QRect(30, 740, 400, 60))
        self.frame_2.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 95, 25))
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setText("Keg Volume: ")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(225, 10, 75, 25))
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setText("Beer Left: ")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(160, 10, 25, 25))
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setText("gal")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(340, 10, 25, 25))
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setText("gal")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(75, 35, 65, 25))
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setText("Approx")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(180, 35, 135, 25))
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setText("mugs left to drink")
        self.label_17.setObjectName("label_17")

        # Display Keg Volume
        self.Keg_Volume_Label.append(_beerlabel(self.frame_2, 120, 10, 40, 25, 12))
        self.Keg_Volume_Label[0].setObjectName("Keg_Volume_Label_0")

        # Display Qty of Beer in the Keg
        self.Keg_Qty_Label.append(_beerlabel(self.frame_2, 300, 10, 40, 25, 12))
        self.Keg_Qty_Label[0].setObjectName("Keg_Qty_Label_0")

        # Display the number of 12 oz mugs left in the keg
        self.Mugs_Label.append(_beerlabel(self.frame_2, 140, 35, 40, 25, 12))
        self.Mugs_Label[0].setObjectName("Mugs_Label_0")
        
       
        # Set up second Keg Widgets
        # Create master frame for this keg
        self.frame_Keg_1 = QtWidgets.QFrame(self.frame_main)
        self.frame_Keg_1.setGeometry(QtCore.QRect(500, 10, 460, 850))
        self.frame_Keg_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Keg_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Keg_1.setObjectName("frame_Keg_1")

        # Create a frame for the Beer Name display
        self.Name_Frame_1 = QtWidgets.QFrame(self.frame_Keg_1)
        self.Name_Frame_1.setGeometry(QtCore.QRect(30, 10, 400, 85))
        self.Name_Frame_1.setAutoFillBackground(False)
        self.Name_Frame_1.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.Name_Frame_1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Name_Frame_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Name_Frame_1.setLineWidth(1)
        self.Name_Frame_1.setObjectName("Name_Frame_1")

        # Set up Beer Name
        self.Beer_Label1.append(_beerlabel(self.Name_Frame_1, 25, 10, 350, 35, 26))
        self.Beer_Label1[1].setObjectName("Beer_Label_3")
        self.Beer_Label2.append(_beerlabel(self.Name_Frame_1, 25, 45, 350, 35, 26))
        self.Beer_Label2[1].setObjectName("Beer_Label_4")
        
        # Create area for Beer Details
        self.frame_6 = QtWidgets.QFrame(self.frame_Keg_1)
        self.frame_6.setGeometry(QtCore.QRect(30, 100, 400, 80))
        self.frame_6.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.label_31 = QtWidgets.QLabel(self.frame_6)
        self.label_31.setGeometry(QtCore.QRect(40, 10, 40, 25))
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setText("ABV:")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_6)
        self.label_32.setGeometry(QtCore.QRect(160, 10, 40, 25))
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setText("IBU:")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_6)
        self.label_33.setGeometry(QtCore.QRect(260, 10, 47, 25))
        self.label_33.setFont(font)
        self.label_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setText("SRM:")
        self.label_33.setObjectName("label_33")
        self.label_35 = QtWidgets.QLabel(self.frame_6)
        self.label_35.setGeometry(QtCore.QRect(25, 30, 100, 25))
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setText("Brew Date:")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_6)
        self.label_36.setGeometry(QtCore.QRect(25, 50, 100, 25))
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setText("Keg Date:")
        self.label_36.setObjectName("label_36")

        # Display ABV
        self.ABV_Label.append(_beerlabel(self.frame_6, 80, 10, 35, 25, 12))
        self.ABV_Label[1].setObjectName("ABV_Label_1")

        # Display IBU
        self.IBU_Label.append(_beerlabel(self.frame_6, 200, 10, 35, 25, 12))
        self.IBU_Label[1].setObjectName("IBU_Label_1")

        # Display SRM
        self.SRM_Label.append(_beerlabel(self.frame_6, 300, 10, 35, 25, 12))
        self.SRM_Label[1].setObjectName("SRM_Label_1")
        
        # Display Brew Date
        self.Brew_Date_Label.append(_beerlabel(self.frame_6, 140, 30, 150, 25, 12))
        self.Brew_Date_Label[1].setObjectName("Brew_Date_Label_1")
          
        # Display Date beer was Kegged
        self.Keg_Date_Label.append(_beerlabel(self.frame_6, 140, 50, 150, 25, 12))        
        self.Keg_Date_Label[1].setObjectName("Keg_Date_Label_1")

        # Display Keg Image
        self.label_37 = QtWidgets.QLabel(self.frame_Keg_1)
        self.label_37.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")

        #Create backgound for Keg Level progress bar
        self.Keg_Fill_Level_3 = QtWidgets.QLabel(self.frame_Keg_1)
        self.Keg_Fill_Level_3.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.Keg_Fill_Level_3.setStyleSheet(FrameStyle)
        self.Keg_Fill_Level_3.setObjectName("Keg_Fill_Level_3")

        # Create Keg Level Progress Bar
        self.Keg_Level_Bar.append(_qprogressbar(self.frame_Keg_1))
        self.Keg_Level_Bar[1].setObjectName("Keg_Level_Bar[1]")

        # Create area to display keg level details below the keg image
        self.frame_7 = QtWidgets.QFrame(self.frame_Keg_1)
        self.frame_7.setGeometry(QtCore.QRect(30, 740, 400, 60))
        self.frame_7.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.label_38 = QtWidgets.QLabel(self.frame_7)
        self.label_38.setGeometry(QtCore.QRect(20, 10, 95, 25))
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setText("Keg Volume:")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame_7)
        self.label_39.setGeometry(QtCore.QRect(225, 10, 75, 25))
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setText("Beer Left:")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_7)
        self.label_40.setGeometry(QtCore.QRect(160, 10, 25, 25))
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setText("gal")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_7)
        self.label_41.setGeometry(QtCore.QRect(340, 10, 25, 25))
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setText("gal")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_7)
        self.label_42.setGeometry(QtCore.QRect(75, 35, 65, 25))
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setText("Approx")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_7)
        self.label_43.setGeometry(QtCore.QRect(180, 35, 135, 25))
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_43.setText("mugs left to drink")
        self.label_43.setObjectName("label_43")

        # Display Keg Volume
        self.Keg_Volume_Label.append(_beerlabel(self.frame_7, 120, 10, 40, 25, 12))
        self.Keg_Volume_Label[1].setObjectName("Keg_Volume_Label_1")

        # Display Qty of Beer in the Keg
        self.Keg_Qty_Label.append(_beerlabel(self.frame_7, 300, 10, 40, 25, 12))
        self.Keg_Qty_Label[1].setObjectName("Keg_Qty_Label_1")

        # Display the number of 12 oz mugs left in the keg
        self.Mugs_Label.append(_beerlabel(self.frame_7, 140, 35, 40, 25, 12))
        self.Mugs_Label[1].setObjectName("Mugs_Label_1")
       
        
        # Set up third keg widgets.
        # Create Master frame for this keg
        self.frame_Keg_2 = QtWidgets.QFrame(self.frame_main)
        self.frame_Keg_2.setGeometry(QtCore.QRect(990, 10, 460, 850))
        self.frame_Keg_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Keg_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Keg_2.setObjectName("frame_Keg_2")

        # Create frame for Beer Name Display
        self.Name_Frame_2 = QtWidgets.QFrame(self.frame_Keg_2)
        self.Name_Frame_2.setGeometry(QtCore.QRect(30, 10, 400, 85))
        self.Name_Frame_2.setAutoFillBackground(False)
        self.Name_Frame_2.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.Name_Frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Name_Frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Name_Frame_2.setLineWidth(1)
        self.Name_Frame_2.setObjectName("Name_Frame_2")

        # Set up Beer Name
        self.Beer_Label1.append(_beerlabel(self.Name_Frame_2, 25, 10, 350, 35, 26))
        self.Beer_Label1[2].setObjectName("Beer_Label_5")
        self.Beer_Label2.append(_beerlabel(self.Name_Frame_2, 25, 45, 350, 35, 26))
        self.Beer_Label2[2].setObjectName("Beer_Label_5")
        
        # Create area for Beer Details
        self.frame_8 = QtWidgets.QFrame(self.frame_Keg_2)
        self.frame_8.setGeometry(QtCore.QRect(30, 100, 400, 80))
        self.frame_8.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_8.setObjectName("frame_8")
        self.label_44 = QtWidgets.QLabel(self.frame_8)
        self.label_44.setGeometry(QtCore.QRect(40, 10, 40, 25))
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_44.setText("ABV:")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_8)
        self.label_45.setGeometry(QtCore.QRect(160, 10, 40, 25))
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setText("IBU:")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame_8)
        self.label_46.setGeometry(QtCore.QRect(260, 10, 47, 25))
        self.label_46.setFont(font)
        self.label_46.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setText("SRM:")
        self.label_46.setObjectName("label_46")
        self.label_48 = QtWidgets.QLabel(self.frame_8)
        self.label_48.setGeometry(QtCore.QRect(25, 30, 100, 25))
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_48.setText("Brew Date:")
        self.label_48.setObjectName("label_48")
        self.Brew_Date_Label_4 = QtWidgets.QLabel(self.frame_8)
        self.Brew_Date_Label_4.setGeometry(QtCore.QRect(140, 30, 150, 25))
        self.label_49 = QtWidgets.QLabel(self.frame_8)
        self.label_49.setGeometry(QtCore.QRect(25, 50, 100, 25))
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_49.setText("Keg Date:")
        self.label_49.setObjectName("label_49")


        
        # Display ABV
        self.ABV_Label.append(_beerlabel(self.frame_8, 80, 10, 35, 25, 12))
        self.ABV_Label[2].setObjectName("ABV_Label_2")

        # Display IBU
        self.IBU_Label.append(_beerlabel(self.frame_8, 200, 10, 35, 25, 12))
        self.IBU_Label[2].setObjectName("IBU_Label_2")
 
        # Display SRM
        self.SRM_Label.append(_beerlabel(self.frame_8, 300, 10, 35, 25, 12))
        self.SRM_Label[2].setObjectName("SRM_Label_2")
        
        # Display Brew Date
        self.Brew_Date_Label.append(_beerlabel(self.frame_8, 140, 30, 150, 25, 12))
        self.Brew_Date_Label[2].setObjectName("Brew_Date_Label_2")
          
        # Display Date beer was Kegged
        self.Keg_Date_Label.append(_beerlabel(self.frame_8, 140, 50, 150, 25, 12))        
        self.Keg_Date_Label[2].setObjectName("Keg_Date_Label_2")

        # Display Keg Image
        self.label_50 = QtWidgets.QLabel(self.frame_Keg_2)
        self.label_50.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_50.setText("")
        self.label_50.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")

        # Create background for Keg Level progress bar
        self.Keg_Fill_Level_4 = QtWidgets.QLabel(self.frame_Keg_2)
        self.Keg_Fill_Level_4.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.Keg_Fill_Level_4.setStyleSheet(FrameStyle)
        self.Keg_Fill_Level_4.setObjectName("Keg_Fill_Level_4")

        # Create Keg Level progress bar
        self.Keg_Level_Bar.append(_qprogressbar(self.frame_Keg_2))
        self.Keg_Level_Bar[2].setObjectName("Keg_Level_Bar[2]")

        # Create area to display keg qty details below keg image
        self.frame_9 = QtWidgets.QFrame(self.frame_Keg_2)
        self.frame_9.setGeometry(QtCore.QRect(30, 740, 400, 60))
        self.frame_9.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_9.setObjectName("frame_9")
        self.label_51 = QtWidgets.QLabel(self.frame_9)
        self.label_51.setGeometry(QtCore.QRect(20, 10, 95, 25))
        self.label_51.setFont(font)
        self.label_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_51.setText("Keg Volume")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame_9)
        self.label_52.setGeometry(QtCore.QRect(225, 10, 75, 25))
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_52.setText("Beer Left:")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.frame_9)
        self.label_53.setGeometry(QtCore.QRect(160, 10, 25, 25))
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_53.setText("gal")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.frame_9)
        self.label_54.setGeometry(QtCore.QRect(340, 10, 25, 25))
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_54.setText("gal")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.frame_9)
        self.label_55.setGeometry(QtCore.QRect(75, 35, 65, 25))
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_55.setText("Approx")
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.frame_9)
        self.label_56.setGeometry(QtCore.QRect(180, 35, 135, 25))
        self.label_56.setFont(font)
        self.label_56.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_56.setText("mugs to drink")
        self.label_56.setObjectName("label_56")

        # Display Keg Volume
        self.Keg_Volume_Label.append(_beerlabel(self.frame_9, 120, 10, 40, 25, 12))
        self.Keg_Volume_Label[2].setObjectName("Keg_Volume_Label_2")

        # Display Qty of Beer in the Keg
        self.Keg_Qty_Label.append(_beerlabel(self.frame_9, 300, 10, 40, 25, 12))
        self.Keg_Qty_Label[2].setObjectName("Keg_Qty_Label_2")

        # Display the number of 12 oz mugs left in the keg
        self.Mugs_Label.append(_beerlabel(self.frame_9, 140, 35, 40, 25, 12))
        self.Mugs_Label[2].setObjectName("Mugs_Label_2")
       
        
        
        

        self.button = QtWidgets.QPushButton(self.frame_main)
        self.button.setGeometry(QtCore.QRect(450, 700, 75, 23))
        self.button.setText("Push Me")
        self.button.setObjectName("button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBeer_Names = QtWidgets.QAction(MainWindow)
        self.actionBeer_Names.setObjectName("actionBeer_Names")
        self.actionSetup = QtWidgets.QAction(MainWindow)
        self.actionSetup.setObjectName("actionSetup")
        self.menuSetup.addAction(self.actionBeer_Names)
        self.menuSetup.addSeparator()
        self.menuSetup.addAction(self.actionSetup)
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
   
        self.button.setText(_translate("MainWindow", "PushButton"))

        self.Beer_Label1[0].setText("Hop Slam")
        self.Beer_Label2[0].setText("Imperial IPA")
        self.Beer_Label1[1].setText("Magnum Force")
        self.Beer_Label2[1].setText("IPA")
        self.Beer_Label1[2].setText("Cream of the Crop")
        self.Beer_Label2[2].setText("Vanilla Cream Ale")

        self.ABV_Label[0].setText("10.0")
        self.ABV_Label[1].setText("7.5")
        self.ABV_Label[2].setText("6.1")

        self.IBU_Label[0].setText("100")
        self.IBU_Label[1].setText("75")
        self.IBU_Label[2].setText("40")

        self.SRM_Label[0].setText("10")
        self.SRM_Label[1].setText("32")
        self.SRM_Label[2].setText("48")

        self.Brew_Date_Label[0].setText("January 31, 2020")
        self.Brew_Date_Label[1].setText("December 23, 2020")
        self.Brew_Date_Label[2].setText("May 15, 2021")

        self.Keg_Date_Label[0].setText("January 31, 2020")
        self.Keg_Date_Label[1].setText("January 15, 2021")
        self.Keg_Date_Label[2].setText("Jume 5, 2021")

        self.Keg_Volume_Label[0].setText("5.0")
        self.Keg_Volume_Label[1].setText("3.0")
        self.Keg_Volume_Label[2].setText("1.3")

        self.Keg_Qty_Label[0].setText("4.95")
        self.Keg_Qty_Label[1].setText("2.75")
        self.Keg_Qty_Label[2].setText("0.5")

        self.Mugs_Label[0].setText("52")
        self.Mugs_Label[1].setText("29")
        self.Mugs_Label[2].setText("5")


        
       
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.actionBeer_Names.setText(_translate("MainWindow", "Beer Names"))
        self.actionSetup.setText(_translate("MainWindow", "Setup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())