from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# import PyQt5
# help (PySide2)

class Cell(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(20, 20)
        self.flag = False
        self.setIcon(QIcon(r'images\cell.jpg'))
        self.setIconSize(QSize(20, 20))
        self.show()

    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.RightButton:
            if not self.flag:
                self.flag = True
                self.setIcon(QIcon(r'images\flag.jpg'))
            else:
                self.flag = False
                self.setIcon(QIcon(r'images\cell.jpg'))

        elif button == Qt.LeftButton:
            print("Left button click!")
        return QPushButton.mousePressEvent(self, event)


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        layout = QVBoxLayout(self)
        for _ in range(7):
            self.layout().addWidget(Cell())




if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
