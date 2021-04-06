import os
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QProgressDialog, qApp, QMessageBox
from MainWindow import Ui_MainWindow

HELP_TEXT = "                   Ui to python converter.                                    \n" \
            "-The program converts files created in the 'Qt designer' into                 \n" \
            "       files adapted to the pyQt format                                       \n" \
            "-To activate the interface, the path to the '*.ui' file must be loaded into   \n" \
            "       the 'Qt Designer file' text line"

ABOUT_SCRIPT = "Latest updates:                          \n" \
               "                                         \n" \
               "19.03.2021   -add help                   \n" \
               "18.03.2021   -start writing              \n" \
               "                                         \n" \
               "Created by Andrey Belyaev                \n" \
               "andreikin@mail.ru"


class UiToPythonConverter(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        # insert ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect menu items
        self.ui.actionHelp.triggered.connect(lambda: self.text_dialog("Help"))
        self.ui.actionAbout.triggered.connect(lambda: self.text_dialog("actionAbout"))

        # connect buttons
        self.ui.disigner_button.clicked.connect(self.add_ui_path)
        self.ui.qt_button.clicked.connect(self.add_py_path)
        self.ui.convert_button.clicked.connect(self.convert_ui_to_py)
        self.desable_out(False)

    # switch for interface part
    def desable_out(self, state):
        self.ui.qt_lineEdit.setEnabled(state)
        self.ui.qt_label.setEnabled(state)
        self.ui.qt_button.setEnabled(state)
        self.ui.convert_button.setEnabled(state)

    # add path for 'ui' lineEdit
    def add_ui_path(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File')[0]
        self.ui.disigner_lineEdit.setText(file_name)
        self.desable_out(True)
        self.ui.qt_lineEdit.setText(file_name.replace('.ui', '.py'))

    # add path for 'python' lineEdit
    def add_py_path(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', filter='*.py')[0]
        self.ui.qt_lineEdit.setText(file_name)

    # generate pyhon command
    def convert_ui_to_py(self):
        util = 'pyuic5.exe'
        dir_path = os.path.dirname(__file__)
        pyuic_path = os.path.join(dir_path, util)
        input_path = self.ui.disigner_lineEdit.text()
        out_path = self.ui.qt_lineEdit.text()
        os.system(pyuic_path + " " + input_path + " -o " + out_path)
        self.progress_dialog()

    # reaction to pressing a button
    def progress_dialog(self):
        dialog = QProgressDialog(self)
        dialog.show()
        for i in range(100):
            dialog.setValue(i)
            time.sleep(0.001)
            qApp.processEvents()
        dialog.cancel()

    # Help window
    def text_dialog(self, text_type):
        help_dialog = QMessageBox(self)
        if text_type == "Help":
            help_dialog.setWindowTitle("Help window")
            help_dialog.setText(HELP_TEXT)
        else:
            help_dialog.setWindowTitle("About program")
            help_dialog.setText(ABOUT_SCRIPT)
        help_dialog.setStandardButtons(QMessageBox.Cancel)
        help_dialog.exec_()


if __name__ == '__main__':
    app = QApplication([])
    win = UiToPythonConverter()
    win.show()
    app.exec_()

