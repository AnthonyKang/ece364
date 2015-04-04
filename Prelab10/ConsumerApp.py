# Import PySide classes

import sys
from PySide.QtCore import *
from PySide.QtGui import *

from ExperimentWindow import *

class ConsumerApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(ConsumerApp, self).__init__(parent)
        self.setupUi(self)

        self.btnShow.clicked.connect(self.displayName)
        self.chkItalic.stateChanged.connect(self.modifyItalic)

    def displayName(self):

        fullName = self.txtName.text()
        self.lblMessage.setText(fullName)

    def modifyItalic(self):

        isChecked = self.chkItalic.isChecked()

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(isChecked)
        font.setBold(True)
        self.lblMessage.setFont(font)


currentApp = QApplication(sys.argv)
currentForm = ConsumerApp()

currentForm.show()
currentApp.exec_()
