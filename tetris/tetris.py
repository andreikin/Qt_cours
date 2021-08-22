# -*- coding: utf-8 -*-

from tetris_ui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class Tetris_UI(QMainWindow):

    def __init__(self):
        super().__init__()

        # insert ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # def initUI(self):
    #
    #     self.setGeometry(300, 300, 300, 220)
    #     self.setWindowTitle('Icon')
    #     self.setWindowIcon(QIcon('web.png'))
    #
    #     self.show()

if __name__ == '__main__':


    app = QApplication([])
    win = Tetris_UI()
    win.show()
    app.exec_()