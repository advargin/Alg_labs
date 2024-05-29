import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5. QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow
class CurrencyConv(QtWidgets.QMainWindow):
    def _init__(self):
        super(CurrencyConv,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets. QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())