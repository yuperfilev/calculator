from src.calculator import Calculator
from src.exceptions import *
from PyQt5 import QtWidgets
from src.mainwindow import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._errorFlag = False
        self._calculator = Calculator()

        self.ui.zeroButton.clicked.connect(lambda: self.numOrOperButtonClicked('0'))
        self.ui.oneButton.clicked.connect(lambda: self.numOrOperButtonClicked('1'))
        self.ui.twoButton.clicked.connect(lambda: self.numOrOperButtonClicked('2'))
        self.ui.threeButton.clicked.connect(lambda: self.numOrOperButtonClicked('3'))
        self.ui.fourButton.clicked.connect(lambda: self.numOrOperButtonClicked('4'))
        self.ui.fiveButton.clicked.connect(lambda: self.numOrOperButtonClicked('5'))
        self.ui.sixButton.clicked.connect(lambda: self.numOrOperButtonClicked('6'))
        self.ui.sevenButton.clicked.connect(lambda: self.numOrOperButtonClicked('7'))
        self.ui.eightButton.clicked.connect(lambda: self.numOrOperButtonClicked('8'))
        self.ui.nineButton.clicked.connect(lambda: self.numOrOperButtonClicked('9'))
        self.ui.obracketButton.clicked.connect(lambda: self.numOrOperButtonClicked('('))
        self.ui.cbracketButton.clicked.connect(lambda: self.numOrOperButtonClicked(')'))
        self.ui.sqrtButton.clicked.connect(lambda: self.numOrOperButtonClicked('√'))
        self.ui.piButton.clicked.connect(lambda: self.numOrOperButtonClicked('п'))
        self.ui.eButton.clicked.connect(lambda: self.numOrOperButtonClicked('e'))
        self.ui.commaButton.clicked.connect(lambda: self.numOrOperButtonClicked('.'))
        self.ui.plusButton.clicked.connect(lambda: self.numOrOperButtonClicked('+'))
        self.ui.minusButton.clicked.connect(lambda: self.numOrOperButtonClicked('-'))
        self.ui.multiplyButton.clicked.connect(lambda: self.numOrOperButtonClicked('*'))
        self.ui.divideButton.clicked.connect(lambda: self.numOrOperButtonClicked('/'))
        self.ui.powerButton.clicked.connect(lambda: self.numOrOperButtonClicked('^'))
        self.ui.eraseButton.clicked.connect(lambda: self.eraseButtonClicked())
        self.ui.clearButton.clicked.connect(lambda: self.clearButtonClicked())
        self.ui.equalButton.clicked.connect(lambda: self.equalButtonClicked())


    def eraseButtonClicked(self):
        if self._errorFlag == True:
            tmp = ''
            self._errorFlag == False
        else:
            tmp = self.ui.ioLine.text()[:-1]
        self.ui.ioLine.setText(tmp)


    def clearButtonClicked(self):
        self.ui.ioLine.setText('')


    def numOrOperButtonClicked(self, symbol):
        if self._errorFlag == True:
            tmp = symbol
            self._errorFlag = False
        else:
            tmp = self.ui.ioLine.text() + symbol
        self.ui.ioLine.setText(tmp)


    def equalButtonClicked(self):
        try:
            if self._errorFlag != True:
                tmp = self.ui.ioLine.text()
                result = self._calculator.calculate(tmp)
                if result is not None:
                    if float.is_integer(result):
                        result = str(int(result))
                    else:
                        result = str(format(result, '.15g'))
                    self.ui.ioLine.setText(result)
        except (IncorrectExpression, ValueError, InconsistentBrackets,
            ZeroDivisionError, OverflowError) as e:
            self.ui.ioLine.setText(str(e))
            self._errorFlag = True


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
