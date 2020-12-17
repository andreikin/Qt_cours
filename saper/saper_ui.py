

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# import PyQt5
# help (PySide2)


class SaperUI(QMainWindow):
    def __init__(self):
        super(SaperUI, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(300)

        # widget
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        # menu bar
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)
        # menu
        self.menu = QMenu("Field size")
        self.menuBar.addMenu(self.menu)
        # action
        self.act1 = QAction("Small", self)
        self.act1.triggered.connect(self.actionSmile)
        self.menu.addAction(self.act1)

        self.act2 = QAction("Middle", self)
        self.act2.triggered.connect(self.actionMiddle)
        self.menu.addAction(self.act2)

    def actionSmile(self):
        print ("Small")

    def actionMiddle(self):
        print("Middle")

        # layout = QVBoxLayout(self)
        # label = QLabel('Saper')
        # layout.addWidget(label)
        #
        #
        # btn1 = QPushButton('Button 1')
        # self.layout().addWidget(btn1)



if __name__ == '__main__':
    app = QApplication([])
    win = SaperUI()
    win.show()
    app.exec_()