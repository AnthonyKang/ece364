import sys
#from Pyside import QtGui
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore, QtGui
num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""
 
opVar = False
sumIt = 0

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.line = QtGui.QLineEdit(self)
        self.line.move(5,5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(490,50)

        zero = QtGui.QPushButton("0", self)
        zero.move(10,160)
        zero.resize(190,30)

        one = QtGui.QPushButton("1", self)
        one.move(10,130)
        one.resize(90,30)

        two = QtGui.QPushButton("2", self)
        two.move(110, 130)
        two.resize(90, 30)

        three = QtGui.QPushButton("3", self)
        three.move(210, 130)
        three.resize(90, 30)

        four = QtGui.QPushButton("4", self)
        four.move(10,100)
        four.resize(90,30)

        five = QtGui.QPushButton("5", self)
        five.move(110,100)
        five.resize(90, 30)

        six = QtGui.QPushButton("6", self)
        six.move(210,100)
        six.resize(90 , 30)

        seven = QtGui.QPushButton("7", self)
        seven.move(10,70)
        seven.resize(90,30)

        eight = QtGui.QPushButton("8", self)
        eight.move(110,70)
        eight.resize(90,30)

        nine = QtGui.QPushButton("9", self)
        nine.move(210, 70)
        nine.resize(90, 30)

        point = QtGui.QPushButton(".", self)
        point.move(210,160)
        point.resize(90,30)

        div = QtGui.QPushButton("/", self)
        div.move(310,70)
        div.resize(90,30)

        mult = QtGui.QPushButton("x", self)
        mult.move(310, 100)
        mult.resize(90,30)

        minus = QtGui.QPushButton("-", self)
        minus.move(310,130)
        minus.resize(90,30)

        plus = QtGui.QPushButton("+", self)
        plus.move(310,160)
        plus.resize(90,30)

        c = QtGui.QPushButton("C", self)
        c.move(410,70)
        c.resize(90,60)
        c.clicked.connect(self.C)

        equal = QtGui.QPushButton("=", self)
        equal.move(410,130)
        equal.resize(90,60)
        equal.clicked.connect(self.Equal)

        checkbox = QtGui.QCheckBox("Display Thousands' Seperator", self)
        checkbox.move(210, 190)
        checkbox.resize(300, 30)

        combobox = QtGui.QComboBox()
        combobox.move(10, 190)
        combobox.resize(90,30)


        nums = [zero, one, two, three, four, five, six, seven, eight, nine]
        ops = [c, div, mult, minus, plus, equal]

        for i in nums:
            i.clicked.connect(self.Nums)

        for i in ops[1:5]:
            i.clicked.connect(self.Operator)

    def Nums(self):
        global num
        global newNum
        global opVar

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)

        if opVar == False:
            self.line.setText(self.line.text() + setNum)
        else:
            self.line.setText(setNum)
            opVar = False
    

    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt

        sumIt += 1

        if sumIt > 1:
            self.Equal()

        num = self.line.text()
        sender = self.sender()
        operator = sender.text()
        opVar = True

    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar
        global sumIt
        print("hi")
        sumIt = 0
        newNum = self.line.text()

        if operator == "+":
            sumAll = float(num) + float(newNum)
        elif operator == "-":
            sumAll = float(num) - float(newNum)
        elif operator == "/":
            sumAll = float(num) / float(newNum)
        elif operator == "x":
            sumAll = float(num) * float(newNum)

        self.line.setText(str(sumAll))
        opVar = True
        print(str(self.comboBox.currentText()))
        self.line.setText(str(self.comboBox.currentText())
        print("jh")

    def C(self):
        global newNum
        global sumAll
        global operator
        global num

        self.line.clear()
        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        oeprator = ""


        self.setGeometry(0,0,500,220)
        self.setFixedSize(500,220)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
