from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

with open('conf.json', 'r') as file:
    conf = json.load(file)




class Cell(QPushButton):
    def __init__(self, status):
        super().__init__()

        self.cell_path = conf["IMAGES"]["CELL"]
        self.empty_cell_path = conf["IMAGES"]["EMPTY_CELL"]
        self.flag_path = conf["IMAGES"]["FLAG"]
        self.mine_path = conf["IMAGES"]["MINE"]

        self.status = status # mine * or mines number
        self.__init_ui()
        self.flag = False
        self.opened = False




    def __init_ui(self):
        self.setFixedSize(20, 20)
        self.setStyleSheet("QPushButton{border-image: url("+self.cell_path+")}")

    def open_cell(self):
        if self.status == "*":
            self.setStyleSheet("QPushButton{border-image: url("+self.mine_path+")}")
        else:
            self.setStyleSheet("QPushButton{border-image: url("+self.empty_cell_path+")}")
            self.setText(str(self.status))
        self.opened = True

    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.RightButton:
            if not self.opened:
                if not self.flag:
                    self.flag = True
                    self.setStyleSheet("QPushButton{border-image: url("+self.flag_path+")}")
                else:
                    self.flag = False
                    self.setStyleSheet("QPushButton{border-image: url("+self.cell_path++")}")
        elif button == Qt.LeftButton:
            self.open_cell()
        return QPushButton.mousePressEvent(self, event)


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        layout = QVBoxLayout(self)
        for i in range(7):
            bt = Cell(i)
            self.layout().addWidget(bt)

if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
