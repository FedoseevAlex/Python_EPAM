#! /usr/bin/env python3.6
"""
Simple GUI calculator using PyQt5.
Supported operations: +, -, *, /, ^
Operates with integers.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import Buttons
import sys
from functools import partial
import operator


class MainApplication(QtWidgets.QMainWindow):
    """
    Main application class. Handles calculator logic itself.
    """
    def __init__(self):
        """
        Initialising method for MainApplication class.
        Sets up user interface and connect buttons to handler functions.
        """
        super(MainApplication, self).__init__()

        self.ui = Buttons.Ui_Form()
        self.ui.setupUi(self)
        self._input = str()
        self._x = None
        self._y = None
        self._op = None
        self._op_table = {'add': operator.add, 'sub': operator.sub,
                          'mul': operator.mul, 'div': operator.truediv,
                          'pow': operator.pow}

        for num in range(10):
            getattr(self.ui, f'pushButton_{num}').clicked.connect(partial(self.numeric_pressed, str(num)))

        for operation in self._op_table.keys():
            getattr(self.ui, f'pushButton_{operation}').clicked.connect(partial(self.operation_pressed, operation))

        self.ui.pushButton_calc.clicked.connect(self.calculate)
        self.ui.pushButton_ac.clicked.connect(self.clear_all)

    def numeric_pressed(self, num: str) -> None:
        """
        Callback method called when numeric buttons pressed.
        Number of clicked function passed as argument.

        :param num: number of pressed button
        :type num: str
        :return: None
        """
        self._input += num
        self.ui.LcdDisplay.display(self._input)

    def operation_pressed(self, operation: str) -> None:
        """
        Callback method called when operation buttons pressed.
        Operation name passed as argument.

        :param operation: operation to perform e.g. 'add'
        :type operation: str
        :return: None
        """
        self._x = self.ui.LcdDisplay.value()
        self._op = operation
        self._input = ''

    def clear_all(self):
        """
        Callback for 'AC' button. This function clears display, buffer and operands variables.
        """
        self._x = None
        self._y = None
        self._op = None
        self._input = ''
        self.ui.LcdDisplay.display('')

    def calculate(self):
        """
        Callback for '=' button. Perform evaluating and displaying result of calculation.
        """
        self._y = self.ui.LcdDisplay.value()
        if None not in [self._x, self._y, self._op]:
            res = self._op_table[self._op](int(self._x), int(self._y))
            self.ui.LcdDisplay.display(str(res))
            self._input = ''
            self._op = None


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()

    sys.exit(app.exec_())
