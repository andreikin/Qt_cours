from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import functools



ABOUT_SCRIPT = "\n" \
               "Latest updates:                \n" \
               "3.02.2021    -start writing   \n" \
               "                               \n" \
               "Created by Andrey Belyaev      \n" \
               "andreikin@mail.ru"

HELP_LABEL = "Select the required character controller and click bake dynamics. \n" \
            "After baking, you can fix problem points manually. "

HELP_TEXT = "\n" \
            "1 Choose the character you want to work with by choosing one of his controllers.\n" \
            "2 Adjust their orientation - the controllers will be oriented in a similar way\n" \
            "3 Make sure the bones are out of the collision objects \n" \
            "4 The root joint must have a parent, to which the system will be attached later\n" \
            "5 Choose 'Create dynanmics sistem'\n" \


class BakeStrand_UI(QMainWindow):
    def __init__(self):
        super(BakeStrand_UI, self).__init__()
        # Window
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Hair strand rigging system")
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.__menu_bar()  # help and About script windows
        self.__libel()  # text on top
        self.__buttons()

    
    def __menu_bar(self):
        menuBar = QMenuBar()
        self.setMenuBar(menuBar)
        menu = QMenu("Help")
        menuBar.addMenu(menu)
        help_action = QAction("Help", self)
        menu.addAction(help_action)
        help_action.triggered.connect(functools.partial(self.text_dialog, "Help"))
        about_script_action = QAction("About script", self)
        menu.addAction(about_script_action)
        about_script_action.triggered.connect(functools.partial(self.text_dialog, "About program"))

    def text_dialog(self, text_type):
        help_dialog = QMessageBox()
        if text_type == "Help":
            help_dialog.setWindowTitle("Help window")
            help_dialog.setText(HELP_TEXT)
        else:
            help_dialog.setWindowTitle("About program")
            help_dialog.setText(ABOUT_SCRIPT)
        help_dialog.setStandardButtons(QMessageBox.Cancel)
        help_dialog.exec_()

    def __libel(self):
        self.help_label = QLabel(HELP_LABEL)
        self.verticalLayout.addWidget(self.help_label)

    def __buttons(self):
        self.button_layout = QGridLayout()
        self.button_layout.setSpacing(2)

        self.bake_selaction_button = QPushButton("Bake_selaction")
        self.button_layout.addWidget(self.bake_selaction_button, 0, 0, 1, 1)
        self.bake_selaction_button.clicked.connect(self.bake_selaction)

        self.unbake_selaction_button = QPushButton("Unbake_selaction")
        self.button_layout.addWidget(self.unbake_selaction_button, 1, 0, 1, 1)
        self.unbake_selaction_button.clicked.connect(self.unbake_selaction)

        self.bake_all_button = QPushButton("Bake_all")
        self.button_layout.addWidget(self.bake_all_button, 0, 1, 1, 1)
        self.bake_all_button.clicked.connect(self.bake_all)

        self.unbake_all_button = QPushButton("Unbake_all")
        self.button_layout.addWidget(self.unbake_all_button, 1, 1, 1, 1)
        self.unbake_all_button.clicked.connect(self.unbake_all)

        self.verticalLayout.addLayout(self.button_layout)

    def bake_selaction(self):
        print("bake_selaction")

    def unbake_selaction(self):
        print("unbake_selaction")

    def bake_all(self):
        print("bake_all")

    def unbake_all(self):
        print("unbake_all")


def bake_strand():
    global dyn_win
    try:
        dyn_win.deleteLater()
    except NameError:
        pass

    app = QApplication([])
    dyn_win = BakeStrand_UI()
    dyn_win.show()
    app.exec_()

bake_strand()