<<<<<<< HEAD
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate
# 
# Set up location of source code for main window and Setup dialog window
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
=======
import sys
import time
import csv
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QThread, pyqtSignal
# 
# Set up location of source code for main window and Setup dialog window
from Keg_Level_Screen import Ui_MainWindow
from Setup_Dialog_Screen import Ui_Setup_Dialog

class Beer_Data:
	# Structure to hold information about the current beer in each keg
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

class Beer_Readings:
	# Structure used to pass information from the hardware reading back to the program
	def __init__(self, level, temp, press):
		self._Level = level 
		self._Temp = temp 
		self._Press = press 

class Conversion_Data:
	# Structure that holds expected hardware readings, and associated calculations for each keg size
	def __init__(self, kegfull, kegempty, kegrange, Ozmm):
		self._KegFull = kegfull
		self._KegEmpty = kegempty
		self._KegRange = kegrange
		self._Ozmm = Ozmm

def truncate(number, decimals=0):
	# Returns a value truncated to the specific number of decimal places.
	if not isinstance(decimals, int):
		raise TypeError("decimal places must be integer.")
	elif decimals < 0:
		raise ValueError("decimal places has to be 0 of more")
	elif decimals == 0:
		return math.trunc(number)

	factor = 10.0 ** decimals
	return math.trunc(number * factor) / factor

#	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 	This is where I will insert the logic to read the sensors.
#	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

TIME_LIMIT = 700

class External(QThread):
#
# Runs a counter thread
#
	countChanged = pyqtSignal(int, int, int, int, int, int, int, int, int)

	def run(self):
		count = 35
		while count < TIME_LIMIT:
			time.sleep(1)
			
			# Call the routines to get data from the hardware
			count +=1
			_Level1 = count 


			# Load the variables to send back to the main program
			# Trigger the event
			self.countChanged.emit(_Level1, 36, 12, _Level1, 37, 13, _Level1, 38, 14)



#	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	Set up Main Window
#	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Window(QMainWindow, Ui_MainWindow):
	# Create structure to hold Keg Data
	Keg_Data = []
	Beer_Level_Press = []
	Hardware_Data = []

	# Intialize the Main Window
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)

		# Connect buttons and menus with routines
		self.connectSignalSlots()

		# Initialize the array to hold the reading from the kegs
		self.create_Beer_Readings(self.Beer_Level_Press)

		# Load the hardware reading to Kag Size conversion data from the file
		self.Load_Conversion(self.Hardware_Data)

		# Load the Keg data from the file
		self.load_File(self.Keg_Data)

		# Load the screen fields with the file data
		self.load_Fields(self.Keg_Data)

		# Determine if each keg is being used
		self.Display_Kegs(self.Keg_Data)
		

	def Load_Conversion(self, _Conversion_Data):
		# Initialize Keg to Hardware Conversion data structure with data from the Hardware.csv file

		# Create a tuple to hold the number of ounces in each size keg
		Keg_Capacity_Tuple = [224, 384, 640]  # Capacity of 1.75, 3 and 5 gallon kegs

		try:
			with open('hardware.csv', 'r') as csv_file:
				Hardware_Reader = csv.reader(csv_file, delimiter = ',')
				line = 0

				for row in Hardware_Reader:
					# Load data from file into Data structure
					_Conversion_Data.append(Conversion_Data(int(row[0]), int(row[1]), 1, 1.0))

					# Calculate the range of reading based on (Empty-Full) for each keg size
					_Conversion_Data[line]._KegRange = _Conversion_Data[line]._KegEmpty - _Conversion_Data[line]._KegFull

					# Calculate Oz/mm for each keg Size
					_Conversion_Data[line].Ozmm = truncate((Keg_Capacity_Tuple[line]/_Conversion_Data[line]._KegRange), 4)

					line += 1

		except IOError:
			print("Hardware File Not Found")
			for count in range(3):
				_Conversion_Data.append(Conversion_Data(0,100,100,1))

			with open('Hardware.csv', mode = 'w', newline='') as hardwarefile:
				hardware_writer = csv.writer(hardwarefile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
				for count in range(3):
					hardware_writer.writerow([_Conversion_Data[count]._KegFull, _Conversion_Data[count]._KegEmpty])



	def load_File(Self, _Keg_Data):
		# Initialize Keg Data Structure with data from the file
		try:
			with open('BeerData.csv', 'r') as csv_file:
				Keg_Reader = csv.reader(csv_file, delimiter=',')
				line = 0
				
				for row in Keg_Reader:
					if row[1] == "1":
						_Active = True
					else:
						_Active = False
					_Keg_Data.append(Beer_Data(row[0],_Active,row[2],row[3],row[4],row[5],row[6],row[7],row[8],int(row[9])))
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


	def create_Beer_Readings(self, _Beer_Readings):
		# Create the structure to hold the beer level, pressure and temerature readings
		for count in range(3):
			_Beer_Readings.append(Beer_Readings(0,0,0))


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
			if _Keg_Data[count]._KegSize == 0:
				self.Keg_Volume_Label[count].setText("1.75")
			elif _Keg_Data[count]._KegSize == 1:
				self.Keg_Volume_Label[count].setText("3.0")
			elif _Keg_Data[count]._KegSize == 2:
				self.Keg_Volume_Label[count].setText("5.0")
			self.Keg_Level_Bar[count].setMaximum(self.Hardware_Data[_Keg_Data[count]._KegSize]._KegRange)

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
		self.button.clicked.connect(self.StartHardwareReadings)
		self.actionExit.triggered.connect(self.Exit_Program)
		self.actionBeer_Names.triggered.connect(self.open_Setup)

	# This routine will start the parallel process that interfaces with the hardware
	def StartHardwareReadings(self):
		self.kegRead = External()
		self.kegRead.countChanged.connect(self.onCountChanged)
		self.kegRead.start()
		print("Started")

	# Dummy test routine
	def onCountChanged(self, keg1level, keg1press, keg1temp, keg2level, keg2press, keg2temp, keg3level, keg3press, keg3temp):
		# Define some variables
		self.Beer_Level_Press[0]._Level = keg1level
		self.Beer_Level_Press[1]._Level = keg2level
		self.Beer_Level_Press[2]._Level = keg3level

		print("Keg Level =", keg2level)
		
		for count in range(3):
			if self.Keg_Data[count]._Active:
				# Scale the raw hardware readings to the appropriate range for this keg size
				# Determine what size keg we are dealing with on this pass
				kegType = self.Keg_Data[count]._KegSize
				print("Keg Type = ", kegType)

				# Now Make sure the hardware reading is within the proper range.  If not, force the reading to the min or max
				if self.Beer_Level_Press[count]._Level < self.Hardware_Data[kegType]._KegFull:
					print("too small")
					self.Beer_Level_Press[count]._Level = self.Hardware_Data[kegType]._KegFull
				elif self.Beer_Level_Press[count]._Level > self.Hardware_Data[kegType]._KegEmpty:
					print("too large")
					self.Beer_Level_Press[count]._Level = self.Hardware_Data[kegType]._KegEmpty		

				# Calculate the keg level by 'flipping the reading' then subtracting that from the range of readings the thi keg type should have.
				# you have to flip the readings because full is a small number and full is a large number.
				currentKegLevel = self.Hardware_Data[kegType]._KegRange - (self.Beer_Level_Press[count]._Level - self.Hardware_Data[kegType]._KegFull)
				currentKegQty = currentKegLevel * self.Hardware_Data[kegType]._Ozmm
				print("Range = ",self.Hardware_Data[kegType]._KegRange ) 
				print("Full = ", self.Hardware_Data[kegType]._KegFull)
				print("Calc Level = ", currentKegLevel)
				print("Volume = ", currentKegQty)

				# Update the screen readings
				if currentKegLevel < 0:
					currentKegLevel = 0
				self.Keg_Level_Bar[count].setValue(currentKegLevel)
				self.Keg_Qty_Label[count].setText(str(truncate((currentKegQty/128), 2)))
				self.Mugs_Label[count].setText(str(truncate((currentKegQty/12), 0)))
				self.Keg_Press_Label[count].setText(str(self.Beer_Level_Press[count]._Press))
				self.Keg_Temp_Label[count].setText(str(truncate((self.Beer_Level_Press[count]._Temp * 1.8) + 32, 0)))




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
			self.UI.Keg_Size[count].setCurrentIndex(self.Keg_Data[count]._KegSize)
			

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
			self.Keg_Data[count]._KegSize = self.UI.Keg_Size[count].currentIndex()

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
>>>>>>> 573e239368316d29a94ce01ed1ba644361f594a6
	sys.exit(app.exec())