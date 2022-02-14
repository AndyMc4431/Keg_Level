
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
        MainWindow.resize(1900, 1000)
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
        self.Keg_Press_Label = []
        self.Keg_Temp_Label = []
        
        # Create banner at top of Window
        self.Logo_R = QtWidgets.QLabel(self.centralwidget)
        self.Logo_R.setGeometry(QtCore.QRect(1168, 0, 100, 100))
        self.Logo_R.setText("")
        self.Logo_R.setPixmap(QtGui.QPixmap("Mad_Spaniel2.gif"))
        self.Logo_R.setScaledContents(True)
        self.Logo_R.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo_R.setObjectName("Logo_R")
        self.Logo_L = QtWidgets.QLabel(self.centralwidget)
        self.Logo_L.setGeometry(QtCore.QRect(630, 0, 100, 100))
        self.Logo_L.setText("")
        self.Logo_L.setPixmap(QtGui.QPixmap("Mad_Spaniel1.gif"))
        self.Logo_L.setScaledContents(True)
        self.Logo_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo_L.setObjectName("Logo_L")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(770, 0, 380, 90))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 5, 140, 20))
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText("Welcome")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 25, 140, 20))
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("to")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 45, 340, 40))
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setText("Mad Spaniel Brewery")
        self.label_4.setObjectName("label_4")
        
        # Create frame to hold Keg displays
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(30, 115, 1860, 900))
        self.frame_main.setStyleSheet("background-color: rgb(205, 196, 170);")
        self.frame_main.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_main.setLineWidth(6)
        self.frame_main.setMidLineWidth(0)
        self.frame_main.setObjectName("frame_main")


        # Set up first Keg Widgets
        # Create the Master frame for this keg
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
        self.Keg_Fill_Level_0 = QtWidgets.QLabel(self.frame_Keg_0)
        self.Keg_Fill_Level_0.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.Keg_Fill_Level_0.setStyleSheet(FrameStyle)
        self.Keg_Fill_Level_0.setObjectName("Keg_Fill_Level_0")

        # Create Progress Bar
        self.Keg_Level_Bar.append(_qprogressbar(self.frame_Keg_0)) 
        self.Keg_Level_Bar[0].setObjectName("Keg_Level_Bar[0]")
        
        # Create Area to display Keg Level Details below Keg image
        self.frame_2 = QtWidgets.QFrame(self.frame_Keg_0)
        self.frame_2.setGeometry(QtCore.QRect(30, 740, 400, 90))
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
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(20, 60, 181, 25))
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setText("Keg Pressure and Temp:")      
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(235, 60, 30, 25))
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setText("psi")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(313, 60, 30, 25))
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setText("°F")
        self.label_20.setObjectName("label_20")

        # Display Keg Volume
        self.Keg_Volume_Label.append(_beerlabel(self.frame_2, 120, 10, 40, 25, 12))
        self.Keg_Volume_Label[0].setObjectName("Keg_Volume_Label_0")

        # Display Qty of Beer in the Keg
        self.Keg_Qty_Label.append(_beerlabel(self.frame_2, 300, 10, 40, 25, 12))
        self.Keg_Qty_Label[0].setObjectName("Keg_Qty_Label_0")

        # Display the number of 12 oz mugs left in the keg
        self.Mugs_Label.append(_beerlabel(self.frame_2, 140, 35, 40, 25, 12))
        self.Mugs_Label[0].setObjectName("Mugs_Label_0")

        # Display the Keg Pressure
        self.Keg_Press_Label.append(_beerlabel(self.frame_2,200, 60, 30, 25, 12))
        self.Keg_Press_Label[0].setObjectName("Keg_Press_Level_0")

        #Display Keg Temperature
        self.Keg_Temp_Label.append(_beerlabel(self.frame_2, 270, 60, 40, 25, 12))
        self.Keg_Temp_Label[0].setObjectName("Keg_Temp_Label_0")

        '''# Create Background frame and objects for when keg is disabled
        # Create the Master frame for this disabled keg
        self.frame_noKeg_0 = QtWidgets.QFrame(self.frame_main) 
        self.frame_noKeg_0.setGeometry(QtCore.QRect(10, 10, 460, 850))
        self.frame_noKeg_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noKeg_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noKeg_0.setObjectName("frame_noKeg_0")

         # Display Keg Image
        self.label_n0 = QtWidgets.QLabel(self.frame_noKeg_0)
        self.label_n0.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_n0.setText("")
        self.label_n0.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_n0.setScaledContents(True)
        self.label_n0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_n0.setObjectName("label_n0")
        
        # Create Background for Fill Level Progress Bar
        self.nKeg_Fill_Level_0 = QtWidgets.QLabel(self.frame_noKeg_0)
        self.nKeg_Fill_Level_0.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.nKeg_Fill_Level_0.setStyleSheet(FrameStyle)
        self.nKeg_Fill_Level_0.setObjectName("nKeg_Fill_Level_0")'''


        
       
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
        self.label_106 = QtWidgets.QLabel(self.frame_6)
        self.label_106.setGeometry(QtCore.QRect(40, 10, 40, 25))
        self.label_106.setFont(font)
        self.label_106.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_106.setText("ABV:")
        self.label_106.setObjectName("label_106")
        self.label_107 = QtWidgets.QLabel(self.frame_6)
        self.label_107.setGeometry(QtCore.QRect(160, 10, 40, 25))
        self.label_107.setFont(font)
        self.label_107.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_107.setText("IBU:")
        self.label_107.setObjectName("label_107")
        self.label_108 = QtWidgets.QLabel(self.frame_6)
        self.label_108.setGeometry(QtCore.QRect(260, 10, 47, 25))
        self.label_108.setFont(font)
        self.label_108.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_108.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_108.setText("SRM:")
        self.label_108.setObjectName("label_108")
        self.label_110 = QtWidgets.QLabel(self.frame_6)
        self.label_110.setGeometry(QtCore.QRect(25, 30, 100, 25))
        self.label_110.setFont(font)
        self.label_110.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_110.setText("Brew Date:")
        self.label_110.setObjectName("label_110")
        self.label_111 = QtWidgets.QLabel(self.frame_6)
        self.label_111.setGeometry(QtCore.QRect(25, 50, 100, 25))
        self.label_111.setFont(font)
        self.label_111.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_111.setText("Keg Date:")
        self.label_111.setObjectName("label_111")

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
        self.label_105 = QtWidgets.QLabel(self.frame_Keg_1)
        self.label_105.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_105.setText("")
        self.label_105.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_105.setScaledContents(True)
        self.label_105.setAlignment(QtCore.Qt.AlignCenter)
        self.label_105.setObjectName("label_105")

        #Create backgound for Keg Level progress bar
        self.Keg_Fill_Level_1 = QtWidgets.QLabel(self.frame_Keg_1)
        self.Keg_Fill_Level_1.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.Keg_Fill_Level_1.setStyleSheet(FrameStyle)
        self.Keg_Fill_Level_1.setObjectName("Keg_Fill_Level_1")

        # Create Keg Level Progress Bar
        self.Keg_Level_Bar.append(_qprogressbar(self.frame_Keg_1))
        self.Keg_Level_Bar[1].setObjectName("Keg_Level_Bar[1]")

        # Create area to display keg level details below the keg image
        self.frame_7 = QtWidgets.QFrame(self.frame_Keg_1)
        self.frame_7.setGeometry(QtCore.QRect(30, 740, 400, 90))
        self.frame_7.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.label_112 = QtWidgets.QLabel(self.frame_7)
        self.label_112.setGeometry(QtCore.QRect(20, 10, 95, 25))
        self.label_112.setFont(font)
        self.label_112.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_112.setText("Keg Volume:")
        self.label_112.setObjectName("label_112")
        self.label_113 = QtWidgets.QLabel(self.frame_7)
        self.label_113.setGeometry(QtCore.QRect(225, 10, 75, 25))
        self.label_113.setFont(font)
        self.label_113.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_113.setText("Beer Left:")
        self.label_113.setObjectName("label_113")
        self.label_114 = QtWidgets.QLabel(self.frame_7)
        self.label_114.setGeometry(QtCore.QRect(160, 10, 25, 25))
        self.label_114.setFont(font)
        self.label_114.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_114.setText("gal")
        self.label_114.setObjectName("label_114")
        self.label_115 = QtWidgets.QLabel(self.frame_7)
        self.label_115.setGeometry(QtCore.QRect(340, 10, 25, 25))
        self.label_115.setFont(font)
        self.label_115.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_115.setText("gal")
        self.label_115.setObjectName("label_115")
        self.label_116 = QtWidgets.QLabel(self.frame_7)
        self.label_116.setGeometry(QtCore.QRect(75, 35, 65, 25))
        self.label_116.setFont(font)
        self.label_116.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_116.setText("Approx")
        self.label_116.setObjectName("label_116")
        self.label_117 = QtWidgets.QLabel(self.frame_7)
        self.label_117.setGeometry(QtCore.QRect(180, 35, 135, 25))
        self.label_117.setFont(font)
        self.label_117.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_117.setText("mugs left to drink")
        self.label_117.setObjectName("label_117")
        self.label_118 = QtWidgets.QLabel(self.frame_7)
        self.label_118.setGeometry(QtCore.QRect(20, 60, 181, 25))
        self.label_118.setFont(font)
        self.label_118.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_118.setText("Keg Pressure and Temp:")      
        self.label_118.setObjectName("label_118")
        self.label_119 = QtWidgets.QLabel(self.frame_7)
        self.label_119.setGeometry(QtCore.QRect(235, 60, 30, 25))
        self.label_119.setFont(font)
        self.label_119.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_119.setText("psi")
        self.label_119.setObjectName("label_119")
        self.label_120 = QtWidgets.QLabel(self.frame_7)
        self.label_120.setGeometry(QtCore.QRect(313, 60, 30, 25))
        self.label_120.setFont(font)
        self.label_120.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_120.setText("°F")
        self.label_120.setObjectName("label_120")

        # Display Keg Volume
        self.Keg_Volume_Label.append(_beerlabel(self.frame_7, 120, 10, 40, 25, 12))
        self.Keg_Volume_Label[1].setObjectName("Keg_Volume_Label_1")

        # Display Qty of Beer in the Keg
        self.Keg_Qty_Label.append(_beerlabel(self.frame_7, 300, 10, 40, 25, 12))
        self.Keg_Qty_Label[1].setObjectName("Keg_Qty_Label_1")

        # Display the number of 12 oz mugs left in the keg
        self.Mugs_Label.append(_beerlabel(self.frame_7, 140, 35, 40, 25, 12))
        self.Mugs_Label[1].setObjectName("Mugs_Label_1")

        # Display the Keg Pressure
        self.Keg_Press_Label.append(_beerlabel(self.frame_7,200, 60, 30, 25, 12))
        self.Keg_Press_Label[1].setObjectName("Keg_Press_Level_1")

        #Display Keg Temperature
        self.Keg_Temp_Label.append(_beerlabel(self.frame_7, 270, 60, 40, 25, 12))
        self.Keg_Temp_Label[1].setObjectName("Keg_Temp_Label_1")       

        '''# Create Background frame and objects for when keg is disabled
        # Create the Master frame for this disabled keg
        self.frame_noKeg_1 = QtWidgets.QFrame(self.frame_main) 
        self.frame_noKeg_1.setGeometry(QtCore.QRect(500, 10, 460, 850))
        self.frame_noKeg_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noKeg_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noKeg_1.setObjectName("frame_noKeg_1")

         # Display Keg Image
        self.label_n1 = QtWidgets.QLabel(self.frame_noKeg_1)
        self.label_n1.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_n1.setText("")
        self.label_n1.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_n1.setScaledContents(True)
        self.label_n1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_n1.setObjectName("label_n1")
        
        # Create Background for Fill Level Progress Bar
        self.nKeg_Fill_Level_1 = QtWidgets.QLabel(self.frame_noKeg_1)
        self.nKeg_Fill_Level_1.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.nKeg_Fill_Level_1.setStyleSheet(FrameStyle)
        self.nKeg_Fill_Level_1.setObjectName("nKeg_Fill_Level_1")'''
       
        
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
        self.label_206 = QtWidgets.QLabel(self.frame_8)
        self.label_206.setGeometry(QtCore.QRect(40, 10, 40, 25))
        self.label_206.setFont(font)
        self.label_206.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_206.setText("ABV:")
        self.label_206.setObjectName("label_206")
        self.label_207 = QtWidgets.QLabel(self.frame_8)
        self.label_207.setGeometry(QtCore.QRect(160, 10, 40, 25))
        self.label_207.setFont(font)
        self.label_207.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_207.setText("IBU:")
        self.label_207.setObjectName("label_207")
        self.label_208 = QtWidgets.QLabel(self.frame_8)
        self.label_208.setGeometry(QtCore.QRect(260, 10, 47, 25))
        self.label_208.setFont(font)
        self.label_208.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_208.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_208.setText("SRM:")
        self.label_208.setObjectName("label_208")
        self.label_210 = QtWidgets.QLabel(self.frame_8)
        self.label_210.setGeometry(QtCore.QRect(25, 30, 100, 25))
        self.label_210.setFont(font)
        self.label_210.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_210.setText("Brew Date:")
        self.label_210.setObjectName("label_210")
        self.label_211 = QtWidgets.QLabel(self.frame_8)
        self.label_211.setGeometry(QtCore.QRect(25, 50, 100, 25))
        self.label_211.setFont(font)
        self.label_211.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_211.setText("Keg Date:")
        self.label_211.setObjectName("label_211")


        
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
        self.label_205 = QtWidgets.QLabel(self.frame_Keg_2)
        self.label_205.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_205.setText("")
        self.label_205.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_205.setScaledContents(True)
        self.label_205.setAlignment(QtCore.Qt.AlignCenter)
        self.label_205.setObjectName("label_205")

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
        self.frame_9.setGeometry(QtCore.QRect(30, 740, 400, 90))
        self.frame_9.setStyleSheet("background-color: rgb(240, 237, 229);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_9.setObjectName("frame_9")
        self.label_212 = QtWidgets.QLabel(self.frame_9)
        self.label_212.setGeometry(QtCore.QRect(20, 10, 95, 25))
        self.label_212.setFont(font)
        self.label_212.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_212.setText("Keg Volume")
        self.label_212.setObjectName("label_212")
        self.label_213 = QtWidgets.QLabel(self.frame_9)
        self.label_213.setGeometry(QtCore.QRect(225, 10, 75, 25))
        self.label_213.setFont(font)
        self.label_213.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_213.setText("Beer Left:")
        self.label_213.setObjectName("label_213")
        self.label_214 = QtWidgets.QLabel(self.frame_9)
        self.label_214.setGeometry(QtCore.QRect(160, 10, 25, 25))
        self.label_214.setFont(font)
        self.label_214.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_214.setText("gal")
        self.label_214.setObjectName("label_214")
        self.label_215 = QtWidgets.QLabel(self.frame_9)
        self.label_215.setGeometry(QtCore.QRect(340, 10, 25, 25))
        self.label_215.setFont(font)
        self.label_215.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_215.setText("gal")
        self.label_215.setObjectName("label_215")
        self.label_216 = QtWidgets.QLabel(self.frame_9)
        self.label_216.setGeometry(QtCore.QRect(75, 35, 65, 25))
        self.label_216.setFont(font)
        self.label_216.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_216.setText("Approx")
        self.label_216.setObjectName("label_216")
        self.label_217 = QtWidgets.QLabel(self.frame_9)
        self.label_217.setGeometry(QtCore.QRect(180, 35, 135, 25))
        self.label_217.setFont(font)
        self.label_217.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_217.setText("mugs to drink")
        self.label_217.setObjectName("label_217")
        self.label_218 = QtWidgets.QLabel(self.frame_9)
        self.label_218.setGeometry(QtCore.QRect(20, 60, 181, 25))
        self.label_218.setFont(font)
        self.label_218.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_218.setText("Keg Pressure and Temp:")      
        self.label_218.setObjectName("label_218")
        self.label_219 = QtWidgets.QLabel(self.frame_9)
        self.label_219.setGeometry(QtCore.QRect(235, 60, 30, 25))
        self.label_219.setFont(font)
        self.label_219.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_219.setText("psi")
        self.label_219.setObjectName("label_219")
        self.label_220 = QtWidgets.QLabel(self.frame_9)
        self.label_220.setGeometry(QtCore.QRect(313, 60, 30, 25))
        self.label_220.setFont(font)
        self.label_220.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_220.setText("°F")
        self.label_220.setObjectName("label_220")

        # Display Keg Volume
        self.Keg_Volume_Label.append(_beerlabel(self.frame_9, 120, 10, 40, 25, 12))
        self.Keg_Volume_Label[2].setObjectName("Keg_Volume_Label_2")

        # Display Qty of Beer in the Keg
        self.Keg_Qty_Label.append(_beerlabel(self.frame_9, 300, 10, 40, 25, 12))
        self.Keg_Qty_Label[2].setObjectName("Keg_Qty_Label_2")

        # Display the number of 12 oz mugs left in the keg
        self.Mugs_Label.append(_beerlabel(self.frame_9, 140, 35, 40, 25, 12))
        self.Mugs_Label[2].setObjectName("Mugs_Label_2")

        # Display the Keg Pressure
        self.Keg_Press_Label.append(_beerlabel(self.frame_9,200, 60, 30, 25, 12))
        self.Keg_Press_Label[2].setObjectName("Keg_Press_Level_2")

        #Display Keg Temperature
        self.Keg_Temp_Label.append(_beerlabel(self.frame_9, 270, 60, 40, 25, 12))
        self.Keg_Temp_Label[2].setObjectName("Keg_Temp_Label_2")        
       
        '''# Create Background frame and objects for when keg is disabled
        # Create the Master frame for this disabled keg
        self.frame_noKeg_2 = QtWidgets.QFrame(self.frame_main) 
        self.frame_noKeg_2.setGeometry(QtCore.QRect(990, 10, 460, 850))
        self.frame_noKeg_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noKeg_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noKeg_2.setObjectName("frame_noKeg_2")

         # Display Keg Image
        self.label_n2 = QtWidgets.QLabel(self.frame_noKeg_2)
        self.label_n2.setGeometry(QtCore.QRect(30, 200, 400, 530))
        self.label_n2.setText("")
        self.label_n2.setPixmap(QtGui.QPixmap("Keg.png"))
        self.label_n2.setScaledContents(True)
        self.label_n2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_n2.setObjectName("label_n2")
        
        # Create Background for Fill Level Progress Bar
        self.nKeg_Fill_Level_2 = QtWidgets.QLabel(self.frame_noKeg_2)
        self.nKeg_Fill_Level_2.setGeometry(QtCore.QRect(215, 267, 40, 434))
        self.nKeg_Fill_Level_2.setStyleSheet(FrameStyle)
        self.nKeg_Fill_Level_2.setObjectName("nKeg_Fill_Level_2")'''      
        
        

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
        self.menuExit.setTitle("File")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuSetup.setTitle("Setup")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBeer_Names = QtWidgets.QAction(MainWindow)
        self.actionBeer_Names.setObjectName("actionBeer_Names")
        self.actionBeer_Names.setText("Beer Info")
        """self.actionSetup = QtWidgets.QAction(MainWindow)
        self.actionSetup.setObjectName("actionSetup")
        self.actionSetup.setText("Setup")"""
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText("Exit")
        self.actionExit.setShortcut("Ctrl+X")
        self.menuExit.addAction(self.actionExit)
        self.menuSetup.addAction(self.actionBeer_Names)
        """self.menuSetup.addSeparator()
        self.menuSetup.addAction(self.actionSetup)"""
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.button.setText("PushButton")
            
        

        """self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        

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
        self.Mugs_Label[2].setText("5")"""


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
