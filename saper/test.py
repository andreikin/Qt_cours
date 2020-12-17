
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# import PyQt5
# help (PySide2)


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)
        label = QLabel('Text')
        layout.addWidget(label)


        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
        btn3 = QPushButton('Button 3')
        btn4 = QPushButton('Button 4')
        btn5 = QPushButton('Button 5')

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