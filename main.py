try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/myStyleTool/resources'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('MY Tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: qlineargradient(xi:0, yi:0, y2:1, stop:0 #FFC5BF, stop:1 #CCE2CB);')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/images/AH.png")
		scaled_pixmap = self.imagePixmap.scaled(
				QtCore.QSize(300,300),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name:')
		self.nameLabel.setStyleSheet(
			'''
			QLabel{
				color: navy;
			}
			'''
		)
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
			QLineEdit{
				color: navy;
			}
			'''
		)
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('Create')
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #8FCACA;
					color: white;
					border-radius: 10px;
					front-size: 16px;
					padding: 8px;
					font-family: Papyrus;
					font-weight: bold;
				}
				QPushButton:hover{	
					background-color: #808080;
				}
			'''
		)
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FF96BA;
					color: white;
					border-radius: 10px;
					front-size: 16px;
					padding: 8px;
					font-family: Papyrus;
					font-weight: bold;
				}
				QPushButton:hover{	
					background-color: #808080;
				}
			'''
		)
		self.cancelButton.clicked.connect(self.close)
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch

def run():
	global ui
	try:
		ui.close
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MyStyleToolDialog(parent=ptr)
	ui.show()