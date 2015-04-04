# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\UserApps\Google Drive\Purdue\ECE 364 2015-1 Spring\Examples\Python Qt\Example3\ExperimentWindow.ui'
#
# Created: Mon Mar 23 12:04:39 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblName = QtGui.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.lblName.setObjectName("lblName")
        self.lblMessage = QtGui.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(10, 230, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.lblMessage.setFont(font)
        self.lblMessage.setText("")
        self.lblMessage.setObjectName("lblMessage")
        self.txtName = QtGui.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.txtName.setText("")
        self.txtName.setObjectName("txtName")
        self.btnShow = QtGui.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(20, 90, 75, 23))
        self.btnShow.setObjectName("btnShow")
        self.chkItalic = QtGui.QCheckBox(self.centralwidget)
        self.chkItalic.setGeometry(QtCore.QRect(280, 30, 70, 17))
        self.chkItalic.setChecked(True)
        self.chkItalic.setObjectName("chkItalic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblName.setText(QtGui.QApplication.translate("MainWindow", "Full Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShow.setText(QtGui.QApplication.translate("MainWindow", "Show Name", None, QtGui.QApplication.UnicodeUTF8))
        self.chkItalic.setText(QtGui.QApplication.translate("MainWindow", "Italic", None, QtGui.QApplication.UnicodeUTF8))

