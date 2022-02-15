import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate
# 

from Keg_Level import Ui_MainWindow
from Setup_Dialog import Ui_Setup_Dialog

class Beer_Data:
	def __init__(self, kegnum, active, name1, name2, abv, ibu, srm, brewdate, kegdate, kegsize):
		self._Keg = kegnum
		self._Active = active
		self._Name1 = name1
		self._Name2 = name2
		self._ABV = abv
		self._IBU = ibu
		self._SRM = srm
		self._BrewDate = brewdate
		self._KegDate = kegdate
		self._KegSize = kegsize

#	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	Set up Main Window
#	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Window(QMainWindow, Ui_MainWindow):
	# Create structure to hold Keg Data
	Keg_Data = []

	# Intialize the Main Window
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)

		# Connect buttons and menus with routines
		self.connectSignalSlots()

		# Load the Keg data from the file
		self.load_File(self.Keg_Data)

		# Load the screen fields with the file data
		self.load_Fields(self.Keg_Data)

		# Determine if each keg is being used
		self.Display_Kegs(self.Keg_Data)
		
	
	def load_File(Self, _Keg_Data):
		# Initialize Keg Data Structure with data from the file
		try:
			with open('BeerData.csv', 'r') as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=',')
				line = 0
				
				for row in csv_reader:
					if row[1] == "1":
						_Active = True
					else:
						_Active = False
					_Keg_Data.append(Beer_Data(row[0],_Active,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
					line += 1
					
		except IOError:
			print('File not found')
			for count in range(3):
				_Keg_Data.append(Beer_Data(count,False," "," "," "," "," "," "," ",0))

			with open('BeerData.csv', mode = 'w', newline='') as beerfile:
				beer_writer = csv.writer(beerfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
				for count in range(3):
					beer_writer.writerow([_Keg_Data[count]._Keg, _Keg_Data[count]._Active, _Keg_Data[count]._Name1, _Keg_Data[count]._Name2, _Keg_Data[count]._ABV, 
					_Keg_Data[count]._IBU, _Keg_Data[count]._SRM, _Keg_Data[count]._BrewDate, _Keg_Data[count]._KegDate, _Keg_Data[count]._KegSize])


	def load_Fields(self, _Keg_Data):
		# Load data from Keg Data Structure into screen labels
		for count in range(3):
			self.Beer_Label1[count].setText(_Keg_Data[count]._Name1)
			self.Beer_Label2[count].setText(_Keg_Data[count]._Name2)
			self.ABV_Label[count].setText(_Keg_Data[count]._ABV)
			self.IBU_Label[count].setText(_Keg_Data[count]._IBU)
			self.SRM_Label[count].setText(_Keg_Data[count]._SRM)
			self.Brew_Date_Label[count].setText(_Keg_Data[count]._BrewDate)
			self.Keg_Date_Label[count].setText(_Keg_Data[count]._KegDate)
			if _Keg_Data[count]._KegSize == "0":
				self.Keg_Volume_Label[count].setText("1.3")
			elif _Keg_Data[count]._KegSize == "1":
				self.Keg_Volume_Label[count].setText("3.0")
			elif _Keg_Data[count]._KegSize == "2":
				self.Keg_Volume_Label[count].setText("5.0")

		# Zero out a couple for labels that will be dynamic based on Keg levels, pressure and temperature
			self.Keg_Qty_Label[count].setText("0")
			self.Mugs_Label[count].setText("0")
			self.Keg_Press_Label[count].setText("0")
			self.Keg_Temp_Label[count].setText("0")
			self.Keg_Level_Bar[count].setValue(0)

	def Display_Kegs(self,_Keg_Data):
		# Check _Active status of each keg and show or hide keg data accordingly
		if _Keg_Data[0]._Active:
			self.frame_Keg_0.show()
			self.Beer_Label1[0].setText(_Keg_Data[0]._Name1)
			self.Beer_Label2[0].setText(_Keg_Data[0]._Name2)
			self.frame_2.show()
			self.frame_3.show()
		else:
			self.Beer_Label1[0].setText("Empty")
			self.Beer_Label2[0].setText("Keg")
			self.frame_2.hide()
			self.frame_3.hide()
		if _Keg_Data[1]._Active:
			self.frame_Keg_1.show()
			self.Beer_Label1[1].setText(_Keg_Data[1]._Name1)
			self.Beer_Label2[1].setText(_Keg_Data[1]._Name2)
			self.frame_6.show()
			self.frame_7.show()
		else:
			self.Beer_Label1[1].setText("Empty")
			self.Beer_Label2[1].setText("Keg")
			self.frame_6.hide()
			self.frame_7.hide()
		if _Keg_Data[2]._Active:
			self.frame_Keg_2.show()
			self.Beer_Label1[2].setText(_Keg_Data[2]._Name1)
			self.Beer_Label2[2].setText(_Keg_Data[2]._Name2)
			self.frame_8.show()
			self.frame_9.show()
		else:
			self.Beer_Label1[2].setText("Empty")
			self.Beer_Label2[2].setText("Keg")
			self.frame_8.hide()
			self.frame_9.hide()
		
		
	
	def connectSignalSlots(self):
	# Connect objects with routines when triggered
		self.button.clicked.connect(self.change_Value)
		self.actionExit.triggered.connect(self.Exit_Program)
		self.actionBeer_Names.triggered.connect(self.open_Setup)

	# Dummy test routine
	def change_Value(self):
		if self.Keg_Level_Bar[0].value() == 0:
			self.Keg_Level_Bar[0].setValue(50)
		else:
			self.Keg_Level_Bar[1].setValue(25)


	#  ++++++++++++++++++++++++++++++++++++++++++++++++++++
	#  Dialog window routines
	#  ++++++++++++++++++++++++++++++++++++++++++++++++++++		
	
	def open_Setup(self):
	# Open the Dialog to enter Keg data
		# Intialize the Dialog Window
		self.dwindow = QtWidgets.QDialog()
		self.UI = Ui_Setup_Dialog()
		self.UI.setupUi(self.dwindow)

		# Load the Dialog fields with the current Keg data
		# Load fields from Data File
		self.load_Dialog_Fields()
		        
		# Determine which Kegs are active and display/hide accordingly
		self.UI.checkBox0.setChecked(self.Keg_Data[0]._Active)
		if self.UI.checkBox0.isChecked() == True:
			self.UI.frame0.show()
		else:
			self.UI.frame0.hide()
		self.UI.checkBox1.setChecked(self.Keg_Data[1]._Active)
		if self.UI.checkBox1.isChecked() == True:
			self.UI.frame1.show()
		else:
			self.UI.frame1.hide()
		self.UI.checkBox2.setChecked(self.Keg_Data[2]._Active)
		if self.UI.checkBox2.isChecked() == True:
			self.UI.frame2.show()
		else:
			self.UI.frame2.hide()

		# Connect widget signals with appropriate slots
		self.dconnectSignalSlots()

		# Show the Window
		self.dwindow.exec()

		# Reload the Main Window fields with data returned from the dialog
		self.load_Fields(self.Keg_Data)
		self.Display_Kegs(self.Keg_Data)

	def dconnectSignalSlots(self):
	#	Connect the widget signals with handler routines
		self.UI.checkBox0.stateChanged.connect(lambda:self.UI.Enable_Keg(0, self.UI.checkBox0.isChecked()))
		self.UI.checkBox1.stateChanged.connect(lambda:self.UI.Enable_Keg(1, self.UI.checkBox1.isChecked()))
		self.UI.checkBox2.stateChanged.connect(lambda:self.UI.Enable_Keg(2, self.UI.checkBox2.isChecked()))
		self.UI.buttonBox.accepted.connect(lambda:self.Save_Setup_Changes())
	 

	def load_Dialog_Fields(self):
	#	Load the labels in the dialog with the information in the Keg Data Structure from the Main Window
		for count in range(3):
			# Set keg size for each keg
			self.UI.Keg_Size[count].addItem("1.75 gal")
			self.UI.Keg_Size[count].addItem("3 gal")
			self.UI.Keg_Size[count].addItem("5 gal")
			self.UI.Keg_Size[count].setCurrentIndex(int(self.Keg_Data[count]._KegSize))
			

			# Set Beer Name1 for each keg
			self.UI.Beer_Name1[count].setText(self.Keg_Data[count]._Name1)
			self.UI.Beer_Name2[count].setText(self.Keg_Data[count]._Name2)

			# Set ABV, IBU and SRM for each beer
			self.UI.ABV[count].setText(self.Keg_Data[count]._ABV)
			self.UI.IBU[count].setText(self.Keg_Data[count]._IBU)
			self.UI.SRM[count].setText(self.Keg_Data[count]._SRM)

			tempDate = QDate.currentDate()
			tempDate = QDate.fromString(self.Keg_Data[count]._BrewDate, "MMM dd yyyy")
			self.UI.Brew_Date[count].setDate(tempDate)
			self.UI.Brew_Date[count].setDisplayFormat("MMM d yyyy")
			tempDate = QDate.fromString(self.Keg_Data[count]._KegDate, "MMM dd yyyy")
			self.UI.Keg_Date[count].setDate(tempDate)
			self.UI.Keg_Date[count].setDisplayFormat("MMM d yyyy")

	def Save_Setup_Changes(self):
	#	Save the information entered by the User into the Main Window's Keg Data Structure and save to the data file.
		# Save the entry fields in the Setup Dialog into the Keg Data List
		for count in range(3):
			# Set Active Status
			if count == 0:
				self.Keg_Data[count]._Active = self.UI.checkBox0.isChecked()
			elif count == 1:
				self.Keg_Data[count]._Active = self.UI.checkBox1.isChecked()
			elif count == 2:
				self.Keg_Data[count]._Active = self.UI.checkBox2.isChecked()

			# Save Names
			self.Keg_Data[count]._Name1 = self.UI.Beer_Name1[count].text()
			self.Keg_Data[count]._Name2 = self.UI.Beer_Name2[count].text()

			# Save ABV, IBU, SRM
			self.Keg_Data[count]._ABV = self.UI.ABV[count].text()
			self.Keg_Data[count]._IBU = self.UI.IBU[count].text()
			self.Keg_Data[count]._SRM = self.UI.SRM[count].text()

			# Save Brew Date and Keg Date
			self.Keg_Data[count]._BrewDate = self.UI.Brew_Date[count].date().toString("MMM dd yyyy")
			self.Keg_Data[count]._KegDate = self.UI.Keg_Date[count].date().toString("MMM dd yyyy")

			# Save Keg Size
			self.Keg_Data[count]._KegSize = str(self.UI.Keg_Size[count].currentIndex())

		# Open the Keg Data file and save the changes
		with open('BeerData.csv', mode = 'w', newline='') as beerfile:
			beer_writer = csv.writer(beerfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

			isActive = 0

			for count in range(3):
				if self.Keg_Data[count]._Active:
					isActive = 1
				else:
					isActive = 0
				beer_writer.writerow([self.Keg_Data[count]._Keg, isActive, self.Keg_Data[count]._Name1, self.Keg_Data[count]._Name2,self.Keg_Data[count]._ABV, 
					self.Keg_Data[count]._IBU, self.Keg_Data[count]._SRM, self.Keg_Data[count]._BrewDate, self.Keg_Data[count]._KegDate, self.Keg_Data[count]._KegSize])

	
	def Exit_Program(self):
		sys.exit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec())