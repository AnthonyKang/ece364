# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ecegrid/a/ee364f03/Prelab10/calculator.ui'
#
# Created: Wed Apr  1 09:26:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 244)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.seven = QtGui.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 40, 92, 27))
        self.seven.setObjectName("seven")
        self.four = QtGui.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 70, 92, 27))
        self.four.setObjectName("four")
        self.one = QtGui.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 100, 92, 27))
        self.one.setObjectName("one")
        self.eight = QtGui.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(110, 40, 92, 27))
        self.eight.setObjectName("eight")
        self.two = QtGui.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(110, 100, 92, 27))
        self.two.setObjectName("two")
        self.six = QtGui.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(210, 70, 92, 27))
        self.six.setObjectName("six")
        self.nine = QtGui.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(210, 40, 92, 27))
        self.nine.setObjectName("nine")
        self.three = QtGui.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(210, 100, 92, 27))
        self.three.setObjectName("three")
        self.mult = QtGui.QPushButton(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(310, 70, 92, 27))
        self.mult.setObjectName("mult")
        self.div = QtGui.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(310, 40, 92, 27))
        self.div.setObjectName("div")
        self.minus = QtGui.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(310, 100, 92, 27))
        self.minus.setObjectName("minus")
        self.plus = QtGui.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(310, 130, 92, 27))
        self.plus.setObjectName("plus")
        self.dot = QtGui.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(210, 130, 92, 27))
        self.dot.setObjectName("dot")
        self.zero = QtGui.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(10, 130, 191, 27))
        self.zero.setObjectName("zero")
        self.line = QtGui.QLineEdit(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 10, 491, 27))
        self.line.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.line.setObjectName("line")
        self.c = QtGui.QPushButton(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(410, 40, 92, 51))
        self.c.setObjectName("c")
        self.equals = QtGui.QPushButton(self.centralwidget)
        self.equals.setGeometry(QtCore.QRect(410, 100, 92, 51))
        self.equals.setObjectName("equals")
        self.thousands = QtGui.QCheckBox(self.centralwidget)
        self.thousands.setGeometry(QtCore.QRect(280, 170, 221, 22))
        self.thousands.setObjectName("thousands")
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 170, 91, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.five = QtGui.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(110, 70, 92, 27))
        self.five.setObjectName("five")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.seven.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.four.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.one.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.eight.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.two.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.six.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.nine.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.three.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.mult.setText(QtGui.QApplication.translate("MainWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.div.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.minus.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.plus.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.dot.setText(QtGui.QApplication.translate("MainWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.zero.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.c.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.equals.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.thousands.setText(QtGui.QApplication.translate("MainWindow", "Display Thousands\' Seperator", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.five.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))

