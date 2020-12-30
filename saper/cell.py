from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# import PyQt5
# help (PySide2)

class Cell(QPushButton):
    def __init__(self, status):
        super().__init__()
        self.status = status # mine * or mines number
        self.__init_ui()
        self.flag = False

    def __init_ui(self):
        self.setFixedSize(20, 20)
        self.setStyleSheet("QPushButton{border-image: url(images/cell.jpg)}")


    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.RightButton:
            if not self.flag:
                self.flag = True
                self.setStyleSheet("QPushButton{border-image: url(images/flag.jpg)}")
            else:
                self.flag = False
                self.setStyleSheet("QPushButton{border-image: url(images/cell.jpg)}")
                self.setText(self.status)

        elif button == Qt.LeftButton:
            print(self.status)
            self.setStyleSheet("QPushButton{border-image: url(images/0cell.jpg)}")
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
