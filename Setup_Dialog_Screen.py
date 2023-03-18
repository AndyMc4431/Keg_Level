from PyQt5 import QtCore, QtGui, QtWidgets

class _beerlineedit(QtWidgets.QLineEdit):
    def __init__(self, parent=None, xpos=0, ypos=0, xsize=0, ysize=0, fontsize=0, maxlength=1 ):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(xpos, ypos, xsize, ysize))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(fontsize)
        self.setFont(font)
        self.setMaxLength(maxlength)
       
class _beercombo(QtWidgets.QComboBox):
    def __init__(self, parent=None, xpos=0, ypos=0, xsize=0, ysize=0, fontsize=0, ):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(xpos, ypos, xsize, ysize))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(fontsize)
        self.setFont(font)
        
class _beerdate(QtWidgets.QDateEdit):
    def __init__(self, parent=None, xpos=0, ypos=0, xsize=0, ysize=0, fontsize=0, ):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(xpos, ypos, xsize, ysize))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(fontsize)
        self.setFont(font)
        self.setStyleSheet("color: rgb(0, 0, 0);")
        self.setCalendarPopup(True)
        self.setDate(QtCore.QDate(2022, 1, 1))
    
class Ui_Setup_Dialog(object):

    def Enable_Keg(self, Keg_Num = 0, Keg_State = False):
        if Keg_Num == 0:
            if Keg_State == True:
                self.frame0.setEnabled(True)
                self.frame0.show()
            else:
                self.frame0.setEnabled(False)
                self.frame0.hide()
        elif Keg_Num == 1:
            if Keg_State == True:
                self.frame1.setEnabled(True)
                self.frame1.show()
            else:
                self.frame1.setEnabled(False)
                self.frame1.hide()
        elif Keg_Num == 2:
            if Keg_State == True:
                self.frame2.setEnabled(True)
                self.frame2.show()
            else:
                self.frame2.setEnabled(False)
                self.frame2.hide()


    def setupUi(self, Setup_Dialog):
        # Create object for this Dialog Box
        Setup_Dialog.setObjectName("Setup_Dialog")
        Setup_Dialog.resize(730, 525)
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        Setup_Dialog.setFont(font)
        Setup_Dialog.setStyleSheet("background-color: rgb(223, 217, 199);")
        Setup_Dialog.setModal(True)
        Setup_Dialog.setWindowTitle("Keg Setup")

        # Create OK/Cancel Buttons
        self.buttonBox = QtWidgets.QDialogButtonBox(Setup_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(285, 485, 160, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(Setup_Dialog.accept)
        self.buttonBox.rejected.connect(Setup_Dialog.reject)


        # Create Title block
        self.label = QtWidgets.QLabel(Setup_Dialog)
        self.label.setGeometry(QtCore.QRect(285, 10, 160, 45))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Keg Setup")

        # Set up some empty lists to contain objects later on
        self.Beer_Name1 = []
        self.Beer_Name2 = []
        self.ABV = []
        self.IBU = []
        self.SRM = []
        self.Brew_Date = []
        self.Keg_Date = []
        self.Keg_Size = []


        # Create 1st Keg Widgets
        # Create Frame to hold first Keg Data
        self.mframe1 = QtWidgets.QFrame(Setup_Dialog)
        self.mframe1.setGeometry(QtCore.QRect(10, 80, 230, 400))
        self.mframe1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mframe1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mframe1.setObjectName("mframe1")

        # Create label and Checkbox to enable 1st Keg
        self.label_3 = QtWidgets.QLabel(self.mframe1)
        self.label_3.setGeometry(QtCore.QRect(5, 10, 220, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Keg #1")

        self.checkBox0 = QtWidgets.QCheckBox(self.mframe1)
        self.checkBox0.setGeometry(QtCore.QRect(80, 30, 80, 17))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(12)
        self.checkBox0.setFont(font)
        self.checkBox0.setObjectName("checkBox0")
        self.checkBox0.setText("In Use?")
       

        # Create Frame to hold Keg Details
        self.frame0 = QtWidgets.QFrame(self.mframe1)
        self.frame0.setEnabled(True)
        self.frame0.setGeometry(QtCore.QRect(10, 50, 210, 330))
        self.frame0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame0.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame0.setObjectName("frame0")

        # Create static Labels
        self.label_2 = QtWidgets.QLabel(self.frame0)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Keg Size")
        self.label_4 = QtWidgets.QLabel(self.frame0)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Beer Name")
        self.label_5 = QtWidgets.QLabel(self.frame0)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("ABV:")
        self.label_6 = QtWidgets.QLabel(self.frame0)
        self.label_6.setGeometry(QtCore.QRect(85, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("IBU:")
        self.label_7 = QtWidgets.QLabel(self.frame0)
        self.label_7.setGeometry(QtCore.QRect(150, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setText("SRM:")
        self.label_8 = QtWidgets.QLabel(self.frame0)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("Brew Date")
        self.label_9 = QtWidgets.QLabel(self.frame0)
        self.label_9.setGeometry(QtCore.QRect(20, 260, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.setText("Keg Date")

        # Set up 1st Keg Data Entry Fields.
        # Set up Beer Size
        self.Keg_Size.append(_beercombo(self.frame0, 100, 10, 81, 31, 11))
        self.Keg_Size[0].setObjectName("Keg1_Size")
        self.Keg_Size[0].setMaxVisibleItems(3)

         # Set up Beer Name Entry Field
        self.Beer_Name1.append(_beerlineedit(self.frame0, 20, 70, 170, 31, 11, 16))
        self.Beer_Name1[0].setObjectName("Beer1_Name1")
        self.Beer_Name2.append(_beerlineedit(self.frame0, 20, 105, 170, 31, 11, 16))
        self.Beer_Name2[0].setObjectName("Beer1_Name_2")
        
         # Set up Beer ABV Entry Field
        self.ABV.append(_beerlineedit(self.frame0, 20, 160, 40, 25, 11, 4))
        self.ABV[0].setObjectName("Beer1_ABV")

        # Set up Beer IBU Entry Field
        self.IBU.append(_beerlineedit(self.frame0, 85, 160, 40, 25, 11, 4))
        self.IBU[0].setObjectName("Beer1_IBU")
       
        # Set up Beer SRM Entry Field
        self.SRM.append(_beerlineedit(self.frame0, 150, 160, 40, 25, 11, 4))
        self.SRM[0].setObjectName("Beer1_SRM")

        # Set up Brew Date Entry Field
        self.Brew_Date.append(_beerdate(self.frame0, 20, 220, 171, 31, 11))
        self.Brew_Date[0].setObjectName("Beer1_BrewDate")
        
        # Set up Keg Date Entry Field
        self.Keg_Date.append(_beerdate(self.frame0, 20, 280, 171, 31, 11))
        self.Keg_Date[0].setObjectName("Beer1_KegDate")

        # Create 2nd Keg Widgets
        # Create Frame to hold 2nd Keg Data
        self.mframe2 = QtWidgets.QFrame(Setup_Dialog)
        self.mframe2.setGeometry(QtCore.QRect(250, 80, 230, 400))
        self.mframe2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mframe2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mframe2.setObjectName("mframe2")

         # Create label and Checkbox to enable 2nd Keg
        self.label_17 = QtWidgets.QLabel(self.mframe2)
        self.label_17.setGeometry(QtCore.QRect(5, 10, 220, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_17.setText("Keg #2")
        self.checkBox1 = QtWidgets.QCheckBox(self.mframe2)
        self.checkBox1.setGeometry(QtCore.QRect(80, 30, 80, 17))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(12)
        self.checkBox1.setFont(font)
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox1.setText("In Use?")        

        # Create Frame to hold Keg Details
        self.frame1 = QtWidgets.QFrame(self.mframe2)
        self.frame1.setEnabled(True)
        self.frame1.setGeometry(QtCore.QRect(10, 50, 210, 330))
        self.frame1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame1.setObjectName("frame1")

        # Create static Labels
        self.label_10 = QtWidgets.QLabel(self.frame1)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setText("Keg Size")
        self.label_11 = QtWidgets.QLabel(self.frame1)
        self.label_11.setGeometry(QtCore.QRect(20, 50, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("Beer Name")
        self.label_12 = QtWidgets.QLabel(self.frame1)
        self.label_12.setGeometry(QtCore.QRect(20, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_12.setText("ABV:")
        self.label_13 = QtWidgets.QLabel(self.frame1)
        self.label_13.setGeometry(QtCore.QRect(85, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_13.setText("IBU:")
        self.label_14 = QtWidgets.QLabel(self.frame1)
        self.label_14.setGeometry(QtCore.QRect(150, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_14.setText("SRM:")
        self.label_15 = QtWidgets.QLabel(self.frame1)
        self.label_15.setGeometry(QtCore.QRect(20, 200, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_15.setText("Brew Date")
        self.label_16 = QtWidgets.QLabel(self.frame1)
        self.label_16.setGeometry(QtCore.QRect(20, 260, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_16.setText("Keg Date")

        # Set up 2nd Keg Data Entry Fields
        # Set up Beer Size
        self.Keg_Size.append(_beercombo(self.frame1, 100, 10, 81, 31, 11))
        self.Keg_Size[1].setObjectName("Keg2_Size")
        self.Keg_Size[1].setMaxVisibleItems(3)

         # Set up Beer Name Entry Field
        self.Beer_Name1.append(_beerlineedit(self.frame1, 20, 70, 170, 31, 11, 16))
        self.Beer_Name1[1].setObjectName("Beer2_Name1")
        self.Beer_Name2.append(_beerlineedit(self.frame1, 20, 105, 170, 31, 11, 16))
        self.Beer_Name2[1].setObjectName("Beer2_Name_2")
        
         # Set up Beer ABV Entry Field
        self.ABV.append(_beerlineedit(self.frame1, 20, 160, 40, 25, 11, 4))
        self.ABV[1].setObjectName("Beer2_ABV")

        # Set up Beer IBU Entry Field
        self.IBU.append(_beerlineedit(self.frame1, 85, 160, 40, 25, 11, 4))
        self.IBU[1].setObjectName("Beer2_IBU")
       
        # Set up Beer SRM Entry Field
        self.SRM.append(_beerlineedit(self.frame1, 150, 160, 40, 25, 11, 4))
        self.SRM[1].setObjectName("Beer2_SRM")

        # Set up Brew Date Entry Field
        self.Brew_Date.append(_beerdate(self.frame1, 20, 220, 171, 31, 11))
        self.Brew_Date[1].setObjectName("Beer2_BrewDate")
        
        # Set up Keg Date Entry Field
        self.Keg_Date.append(_beerdate(self.frame1, 20, 280, 171, 31, 11))
        self.Keg_Date[1].setObjectName("Beer2_KegDate")       

        # Create 3rd Keg Widgets
        # Create Frame to hold 3rd Keg Data
        self.mframe3 = QtWidgets.QFrame(Setup_Dialog)
        self.mframe3.setGeometry(QtCore.QRect(490, 80, 230, 400))
        self.mframe3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mframe3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mframe3.setObjectName("mframe3")

         # Create label and Checkbox to enable 3rd Keg        
        self.label_25 = QtWidgets.QLabel(self.mframe3)
        self.label_25.setGeometry(QtCore.QRect(5, 10, 220, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_25.setText("Keg #3")
        self.checkBox2 = QtWidgets.QCheckBox(self.mframe3)
        self.checkBox2.setGeometry(QtCore.QRect(80, 30, 80, 17))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(12)
        self.checkBox2.setFont(font)
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox2.setText("In Use?")

        # Create Frame to hold Keg Details
        self.frame2 = QtWidgets.QFrame(self.mframe3)
        self.frame2.setEnabled(True)
        self.frame2.setGeometry(QtCore.QRect(10, 50, 210, 330))
        self.frame2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame2.setObjectName("frame2")

        # Create static Labels             
        self.label_18 = QtWidgets.QLabel(self.frame2)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_18.setText("Keg Size")
        self.label_19 = QtWidgets.QLabel(self.frame2)
        self.label_19.setGeometry(QtCore.QRect(20, 50, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_19.setText("Beer Name")
        self.label_20 = QtWidgets.QLabel(self.frame2)
        self.label_20.setGeometry(QtCore.QRect(20, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_20.setText("ABV:")
        self.label_21 = QtWidgets.QLabel(self.frame2)
        self.label_21.setGeometry(QtCore.QRect(85, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_21.setText("IBU:")   
        self.label_22 = QtWidgets.QLabel(self.frame2)
        self.label_22.setGeometry(QtCore.QRect(150, 140, 40, 20))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_22.setText("SRM:")
        self.label_23 = QtWidgets.QLabel(self.frame2)
        self.label_23.setGeometry(QtCore.QRect(20, 200, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_23.setText("Brew Date")       
        self.label_24 = QtWidgets.QLabel(self.frame2)
        self.label_24.setGeometry(QtCore.QRect(20, 260, 170, 16))
        font = QtGui.QFont()
        font.setFamily("GrilledCheese BTN")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_24.setText("Keg Date")

        # Set up 3rd Keg Data Entry Fields
        # Set up Beer Size
        self.Keg_Size.append(_beercombo(self.frame2, 100, 10, 81, 31, 11))
        self.Keg_Size[2].setObjectName("Keg3_Size")
        self.Keg_Size[2].setMaxVisibleItems(3)

         # Set up Beer Name Entry Field
        self.Beer_Name1.append(_beerlineedit(self.frame2, 20, 70, 170, 31, 11, 16))
        self.Beer_Name1[2].setObjectName("Beer3_Name1")
        self.Beer_Name2.append(_beerlineedit(self.frame2, 20, 105, 170, 31, 11, 16))
        self.Beer_Name2[2].setObjectName("Beer3_Name_2")
        
         # Set up Beer ABV Entry Field
        self.ABV.append(_beerlineedit(self.frame2, 20, 160, 40, 25, 11, 4))
        self.ABV[2].setObjectName("Beer3_ABV")

        # Set up Beer IBU Entry Field
        self.IBU.append(_beerlineedit(self.frame2, 85, 160, 40, 25, 11, 4))
        self.IBU[2].setObjectName("Beer3_IBU")
       
        # Set up Beer SRM Entry Field
        self.SRM.append(_beerlineedit(self.frame2, 150, 160, 40, 25, 11, 4))
        self.SRM[2].setObjectName("Beer3_SRM")

        # Set up Brew Date Entry Field
        self.Brew_Date.append(_beerdate(self.frame2, 20, 220, 171, 31, 11))
        self.Brew_Date[2].setObjectName("Beer3_BrewDate")
        
        # Set up Keg Date Entry Field
        self.Keg_Date.append(_beerdate(self.frame2, 20, 280, 171, 31, 11))
        self.Keg_Date[2].setObjectName("Beer3_KegDate")       

           
        QtCore.QMetaObject.connectSlotsByName(Setup_Dialog)
        Setup_Dialog.setTabOrder(self.checkBox0, self.checkBox1)
        Setup_Dialog.setTabOrder(self.checkBox1, self.checkBox2)
        Setup_Dialog.setTabOrder(self.checkBox2, self.Keg_Size[0])
        


    """def retranslateUi(self, Setup_Dialog):
        _translate = QtCore.QCoreApplication.translate
        
        
        for count in range(3):
            print(count)
            # Set keg size for each keg
            self.Keg_Size[count].addItem("1.75 gal")
            self.Keg_Size[count].addItem("3 gal")
            self.Keg_Size[count].addItem("5 gal")
            self.Keg_Size[count].setCurrentIndex(0)

            # Set Beer Name1 for each keg
            self.Beer_Name1[count].setText(_Keg_Data[count]._Name1)
            print(_Keg_Data[count]._Name1)
            self.Beer_Name2[count].setText(_Keg_Data[count]._Name2)

            # Set ABV, IBU and SRM for each beer
            self.ABV[count].setText(_Keg_Data[count]._ABV)
            self.IBU[count].setText(_Keg_Data[count]._IBU)
            self.SRM[count].setText(_Keg_Data[count]._SRM)
            self.Brew_Date[count].setText(_Keg_Data[count]._BrewDate)
            self.BrewDate[count].setDisplayFormat("MMMM d yyyy")
            self.Keg_Date[count].setText(_Keg_Data[count]._KegDate)
            self.KegDate[count].setDisplayFormat("MMMM d yyyy")"""
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Setup_Dialog = QtWidgets.QDialog()
    ui = Ui_Setup_Dialog()
    ui.setupUi(Setup_Dialog)
    Setup_Dialog.show()
    sys.exit(app.exec_())
