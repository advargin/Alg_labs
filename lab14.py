import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow


class CurrencyConv(QtWidgets.QMainWindow):
    def _init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.input_cur.setPlaceholderText('Из валюты')
        self.ui.input_sum.setPlaceholderText('Сколько')
        self.ui.output_cur.setPlaceholderText('В валюту')
        self.ui.output_sum.setPlaceholderText('Итого')

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('pngwing.com.png'))
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_cur = self.ui.input_cur.text()
        output_cur = self.ui.output_cur.text()
        input_sum = int(self.ui.input_sum.text())
        output_sum = round(c.convert(input_sum, '%s' % (input_cur), '%s' % (output_cur)), 2)
        self.ui.output_sum.setText(str(output_sum))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
sys.exit(app.exec())
