import win32api
import tempfile
import win32print
import os, sys
from PyQt5 import QtCore, QtWidgets, QtPrintSupport
from PyQt5.QtGui import *

textdata = "*500098254884*"

# win32api.ShellExecute(0, 'print', filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)

class Window(QtWidgets.QWidget):
    def __init__(self):
        print("inside window")
        super(Window,self).__init__()
        self.setWindowTitle('Document Printer')
        self.editor = QtWidgets.QTextEdit(self)
        #self.editor.setFont(QFont('Times', pointSize=20))
        #self.editor.append(textdata)
        self.editor.setDocument(data)
        self.editor.setDisabled(True)
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        layout.addWidget(self.buttonPrint, 1, 1)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

def processprint(tdoc):
    app = QtWidgets.QApplication(sys.argv)
    window = Window(tdoc)
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())