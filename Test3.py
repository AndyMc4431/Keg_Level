import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton

from Keg_Level import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.connectSignalSlots()

	def connectSignalSlots(self):
		self.button.clicked.connect(self.change_Value)

	def change_Value(self):
		if self.Keg_Level_Bar[0].value() == 0:
			self.Keg_Level_Bar[0].setValue(50)
		else:
			self.Keg_Level_Bar[1].setValue(25)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec())