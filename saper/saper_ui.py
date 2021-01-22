from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import functools
from result_handler import ResultHandler

class SaperUI(QMainWindow):
    def __init__(self):
        super(SaperUI, self).__init__()
        # Window
        self.setWindowTitle("Minesweeper")
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.__menu_bar()
        self.__header()
        self.gridLayout_field = QGridLayout()
        self.gridLayout_field.setSpacing(0)
        self.verticalLayout.addLayout(self.gridLayout_field)

    def __menu_bar(self):
        # menu bar
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)
        # menu "Field size"
        self.menu = QMenu("Field size")
        self.menuBar.addMenu(self.menu)
        # action
        self.act1 = QAction("Small", self)
        self.act1.triggered.connect(functools.partial(self.restart_resize_command, "SMALL"))
        self.menu.addAction(self.act1)
        self.act2 = QAction("Middle", self)
        self.act2.triggered.connect(functools.partial(self.restart_resize_command, "MEDIUM"))
        self.menu.addAction(self.act2)
        self.act3 = QAction("Large", self)
        self.act3.triggered.connect(functools.partial(self.restart_resize_command, "LARGE"))
        self.menu.addAction(self.act3)
        # menu "Help"
        self.menu_help = QMenu("Additional")
        self.menuBar.addMenu(self.menu_help)
        # action
        self.act4 = QAction("About program", self)
        self.act4.triggered.connect(functools.partial(self.text_dialog, "ABOUT_PROGRAM"))
        self.menu_help.addAction(self.act4)
        
        self.act_record = QAction("Records", self)
        self.act_record.triggered.connect(self.start_records_dealog)
        self.menu_help.addAction(self.act_record)
        
        self.act_help = QAction("Help", self)
        self.act_help.triggered.connect(functools.partial(self.text_dialog, "HELP_TEXT"))
        self.menu_help.addAction(self.act_help)

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
        self.pushButton_reset = QPushButton("Restart")
        self.pushButton_reset.setMinimumSize(QSize(50, 20))
        self.pushButton_reset.setMaximumSize(QSize(50, 20))
        self.horizontalLayout.addWidget(self.pushButton_reset, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.pushButton_reset.clicked.connect(functools.partial(self.restart_resize_command, "Restart"))

        self.label_mines_count = QLabel("000")
        font = QFont()
        font.setPointSize(12)
        self.label_mines_count.setFont(font)
        self.label_mines_count.setObjectName("label_mines_count")
        self.horizontalLayout.addWidget(self.label_mines_count, 0, Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_top)

    def start_records_dealog(self):
        self.records_dealog = ResultHandler()
        self.records_dealog.exec_()





