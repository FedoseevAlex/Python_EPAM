from PyQt5 import QtCore, QtGui, QtWidgets
import Buttons
import sys
from functools import partial
import operator

class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()

        self.ui = Buttons.Ui_Form()
        self.ui.setupUi(self)
        #self.ui.button.clicked.connect(self.button_pressed)
        self._input = str()
        self.operations = {'+': operator.add, '*': operator.mul,
                           '/': operator.truediv, '-': operator.sub,
                           '^': operator.pow}
        self._x = self._y = None
        self._op = None

        # Number button creating
        for i in range(9):
            col = i % 3
            row = i // 3
            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName("button_{}".format(str(i + 1)))
            self.ui.gridLayout.addWidget(button, row, col, 1, 1)
            button.setText(str(i + 1))

            button.clicked.connect(partial(self.number_pressed, str(i + 1)))

        # Operation buttons created
        ops_to_display = ['+', '-', '*', '/', '^', 'AC', '=']
        for i, sign in enumerate(ops_to_display):
            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName(sign)
            self.ui.operations.addWidget(button, i, 0, 1, 1)
            button.setText(sign)

            button.clicked.connect(partial(self.operation_pressed(), sign))


    def number_pressed(self, char):
        to_display = ''
        if char in self.operations.keys():
            if not set(self._input).intersection(self.operations.keys()):
                self._input = self._input + char
            elif self._input.endswith(tuple(self.operations.keys())):
                self._input = self._input[0: -1] + char
            self._op = char
            self._x = self.ui.lcdNumber.value()
            self._input = ''
        elif char == 'AC':
            self.clear_all()
        elif char == '=':
            self._y = self.ui.lcdNumber.value()
            res = self.operations[self._op](self._x, self._y)
            print('Res = {}'.format(res))
            self.ui.lcdNumber.display(str(int(res)))
            self.clear_all()
            return
        else:
            self._input += char

        self.ui.lcdNumber.display(self._input)

    def operation_pressed(self):
        pass

    def clear_all(self):
        self._input = ''
        #self.ui.lcdNumber.display(self._input)
        self._x = None
        self._y = None
        self._op = None


        # self.ui.lcdNumber.display(number)

app = QtWidgets.QApplication(sys.argv)
window = MainApplication()
window.show()

sys.exit(app.exec_())
