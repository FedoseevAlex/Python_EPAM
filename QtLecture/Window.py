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
        self._string = str()
        self._x = None
        self._y = None
        self._op = None

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

            button.clicked.connect(partial(self.button_pressed, str(i + 1)))

            for i, sign in enumerate('+-*/=^'):
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
                button.setObjectName(sign)
                self.ui.operations.addWidget(button, i, 0, 1, 1)
                button.setText(sign)

                button.clicked.connect(partial(self.button_pressed, sign))

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
            button.setObjectName('reset')
            self.ui.operations.addWidget(button, i, 0, 1, 1)
            button.setText('reset')

            button.clicked.connect(partial(self.button_pressed, 'res'))

    def button_pressed(self, char):

        ops = {'+': operator.add, '*': operator.mul,
               '/': operator.truediv, '-': operator.sub,
               '^': operator.pow}




        # self.ui.lcdNumber.display(number)

app = QtWidgets.QApplication(sys.argv)
window = MainApplication()
window.show()

sys.exit(app.exec_())
