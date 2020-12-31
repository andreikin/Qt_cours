

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
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.__menu_bar()
        self.__header()

    def __menu_bar(self):
        # menu bar
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)
        # menu "Field size"
        self.menu = QMenu("Field size")
        self.menuBar.addMenu(self.menu)
        # action
        self.act1 = QAction("Small", self)
        self.act1.triggered.connect(self.actionSmile)
        self.menu.addAction(self.act1)
        self.act2 = QAction("Middle", self)
        self.act2.triggered.connect(self.actionMiddle)
        self.menu.addAction(self.act2)
        self.act3 = QAction("Large", self)
        self.act3.triggered.connect(self.actionLarge)
        self.menu.addAction(self.act3)
        # menu "Help"
        self.menu_help = QMenu("Help")
        self.menuBar.addMenu(self.menu_help)
        # action
        self.act4 = QAction("About program", self)
        self.act4.triggered.connect(self.action_about_program)
        self.menu_help.addAction(self.act4)
        self.act5 = QAction("Help", self)
        self.act5.triggered.connect(self.action_help)
        self.menu_help.addAction(self.act5)

    def __header(self):
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setMaximumSize(QSize(16777215, 42))
        self.frame_top.setFrameShape(QFrame.Panel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout.addWidget(self.frame_top)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(-1, 1, -1, 1)

        self.label_time = QLabel("00:00")
        font = QFont()
        font.setPointSize(12)
        self.label_time.setFont(font)
        self.horizontalLayout.addWidget(self.label_time, 0, Qt.AlignLeft)

        self.pushButton_reset = QPushButton(self.frame_top)
        self.pushButton_reset.setMinimumSize(QSize(40, 40))
        self.pushButton_reset.setMaximumSize(QSize(40, 40))
        self.horizontalLayout.addWidget(self.pushButton_reset, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_mines_count = QLabel("000")

        font = QFont()
        font.setPointSize(12)
        self.label_mines_count.setFont(font)
        self.label_mines_count.setObjectName("label_mines_count")
        self.horizontalLayout.addWidget(self.label_mines_count, 0, Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_top)

    def actionSmile(self):
        print ("Small")

    def actionMiddle(self):
        print("Middle")

    def actionLarge(self):
        print("Large")

    def action_about_program(self):
        print("About program")

    def action_help(self):
        print("Help")





if __name__ == '__main__':
    app = QApplication([])
    win = SaperUI()
    win.show()
    app.exec_()