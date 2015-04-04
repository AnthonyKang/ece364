import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore, QtGui
from calculator import *
num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""
 
opVar = False
sumIt = 0

class CalculatorApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(CalculatorApp, self).__init__(parent)
        self.setupUi(self)

        nums = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]
        ops = [self.c, self.div, self.mult, self.minus, self.plus, self.equals]
        
        for i in nums:
            i.clicked.connect(self.Nums)

        for i in ops[1:5]:
            i.clicked.connect(self.Operator)
            
        self.c.clicked.connect(self.C)
        self.equals.clicked.connect(self.Equal)
        self.setGeometry(0,0,500,220)
        self.setFixedSize(500,220)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

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
            print(sumIt)

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

        #sumIt = 0
        newNum = self.line.text()
        newNum = newNum.replace(",","")

        if operator == "+":
            sumAll = float(num) + float(newNum)
        elif operator == "-":
            sumAll = float(num) - float(newNum)
        elif operator == "/":
            sumAll = float(num) / float(newNum)
        elif operator == "x":
            sumAll = float(num) * float(newNum)
        
        sumAll = ('{0:.'+str(self.comboBox.currentText())+'f}').format(float(sumAll))  
        
        if(self.thousands.isChecked()) == True:
            print("hi")
            #print(self.Thousands(str(sumAll)))
            self.line.setText(self.Thousands(str(sumAll)))
        else:
            num_digits = self.line.setText(str(sumAll))
        #self.Thousands(str(sumAll))
        
        opVar = True
        print(str(self.comboBox.currentText()))
        #print(str(self.thousands.isChecked()))

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


   
    
    def Thousands(self,num_string):
        decimil = self.comboBox.currentText()
        nums = num_string[0:-(int(decimil)+1)]
        print(nums)
        num_display = ''
        comma = 1
        for i in range(len(nums)):
            num_display = nums[-1-i] + num_display
            
            if comma == 3:
                comma = 0
                num_display = ',' + num_display 
            comma = comma + 1
        if num_display[0] == ',':
            num_display = num_display[1:]
        return num_display

def main():
    app = QtGui.QApplication(sys.argv)
    main = CalculatorApp()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
