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

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('icon_conv1.png'))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
