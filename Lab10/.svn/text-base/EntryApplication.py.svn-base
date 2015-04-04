import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore, QtGui
from EntryForm import *
import re
import string

class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)

        self.text_boxes = [self.txtFirstName, self.txtLastName, self.txtAddress, self.txtCity, self.txtState, self.txtEmail, self.txtZip]
        (self.btnClear).clicked.connect(self.clear)
        self.btnSave.clicked.connect(self.validate)
        #self.btnSave.setEnabled(True)
        self.btnLoad.clicked.connect(self.loadData)

        for i in self.text_boxes:
            i.textChanged.connect(self.save_enable)

        self.states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def save_enable(self):
        for i in self.text_boxes:
            if i.text() is not '':
                self.btnSave.setEnabled(True)
                self.btnLoad.setEnabled(False)

    def validate(self):
        valid = 1
        for i in self.text_boxes:
            if(i.text() == ''):
                self.lblError.setText('Not all entries are populated')
                return
        if self.txtState.text() not in self.states:
            valid = 0
            self.lblError.setText('State is not valid')
            return
        if len(str(self.txtZip.text())) != 5:
            valid = 0
            self.lblError.setText('Zip code must be a 5 digit number')
            return
        for i in self.txtZip.text():
            if i not in string.digits:
                valid = 0
                self.lblError.setText('Zip code must be a 5 digit number')
                return 
        m = re.match(r'(\w+@\w+\.\w+)', str(self.txtEmail.text()))
        print(m)
        if(not m):
            valid = 0
            self.lblError.setText('Email is not valid')
            return
        if valid == 1:
            self.lblError.setText('')
            fileout = open('target.xml', 'w')
            fileout.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            fileout.write('<user>\n')
            fileout.write('\t<FirstName>' + self.txtFirstName.text() + '</FirstName>\n')
            fileout.write('\t<LastName>' + self.txtLastName.text() + '</LastName>\n')
            fileout.write('\t<Address>' + self.txtAddress.text() + '</Address>\n')
            fileout.write('\t<City>' + self.txtCity.text() + '</City>\n')
            fileout.write('\t<State>' + self.txtState.text() + '</State>\n')
            fileout.write('\t<ZIP>' + self.txtZip.text() + '</ZIP>\n')
            fileout.write('\t<Email>' + self.txtEmail.text() + '</Email>\n')
            fileout.write('</user>')

        

        


    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """
        with open(filePath, 'r') as inputf:
            lines = [x.strip('\n').strip() for x in inputf.readlines()]
            data = lines[2:]
            for entry in data:
                if 'FirstName' in entry:
                    self.txtFirstName.setText(entry[11:-12])
                if 'LastName' in entry:
                    self.txtLastName.setText(entry[10:-11])
                if 'Address' in entry:
                    self.txtAddress.setText(entry[9:-10])
                if 'City' in entry:
                    self.txtCity.setText(entry[6:-7])
                if 'State' in entry:
                    self.txtState.setText(entry[7:-8])
                if 'ZIP' in entry:
                    self.txtZip.setText(entry[5:-6])
                if 'Email' in entry:
                    self.txtEmail.setText(entry[7:-8])
            print(data)
        pass

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)

    def clear(self):
        for i in self.text_boxes:
            i.setText('')
            self.btnLoad.setEnabled(True)
            self.btnSave.setEnabled(False)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
