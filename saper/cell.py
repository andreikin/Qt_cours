from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

class Cell(QPushButton):
    def __init__(self, status, position):
        super().__init__()
        # load settings
        with open('conf.json', 'r') as file:
            self.conf = json.load(file)
        self.cell_path = self.conf["IMAGES"]["CELL"]
        self.empty_cell_path = self.conf["IMAGES"]["EMPTY_CELL"]
        self.flag_path = self.conf["IMAGES"]["FLAG"]
        self.mine_path = self.conf["IMAGES"]["MINE"]

        self.status = status   # mine * or mines number
        self.flag = False
        self.opened = False
        self.frozen = False    # when the end of the game all keys are frozen
        self.position = position
        self.__init_ui()

    def __init_ui(self):
        self.setFixedSize(self.conf["CELL_SIZE"], self.conf["CELL_SIZE"])
        self.setStyleSheet("QPushButton{border-image: url("+self.cell_path+")}")

    def open_cell(self):
        if not self.frozen:
            if self.status == "*":
                self.setStyleSheet("QPushButton{border-image: url("+self.mine_path+")}")
            else:
                self.setStyleSheet("QPushButton{border-image: url("+self.empty_cell_path+")}")
                if not self.status == "0":
                    self.setText(str(self.status))
                self.flag = False
            self.opened = True

    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.RightButton and not self.frozen:
            if not self.opened:
                if not self.flag:
                    self.flag = True
                    self.setStyleSheet("QPushButton{border-image: url("+self.flag_path+")}")
                else:
                    self.flag = False
                    self.setStyleSheet("QPushButton{border-image: url("+self.cell_path+")}")

        elif button == Qt.LeftButton:
            self.open_cell()
        return QPushButton.mousePressEvent(self, event)

