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
        self.setIcon(QIcon('cell.jpg'))
        self.setIconSize(QSize(20, 20))
        self.show()

    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.RightButton:
            if not self.flag:
                self.flag = True
                self.setIcon(QIcon('flag.jpg'))
            else:
                self.flag = False
                self.setIcon(QIcon('cell.jpg'))

        elif button == Qt.LeftButton:
            print("Left button click!")
        return QPushButton.mousePressEvent(self, event)


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)
        label = QLabel('Text')
        layout.addWidget(label)

        btn1 = Cell()
        btn2 = Cell()
        btn3 = Cell()
        btn4 = Cell()
        btn5 = Cell()

        #btn1.setStyleSheet("background-image: sell.jpg ;")

        self.layout().addWidget(btn1)
        self.layout().addWidget(btn2)
        self.layout().addWidget(btn3)
        self.layout().addWidget(btn4)
        self.layout().addWidget(btn5)


if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
