


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(358)
        self.setMinimumHeight(70)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.gridLayout = QGridLayout()
        self.layout.addLayout(self.gridLayout)

        self.label_pfx = QLabel("Pfx:")
        self.gridLayout.addWidget(self.label_pfx, 0, 0, 1, 1)

        self.label_name = QLabel("Name:")
        self.gridLayout.addWidget(self.label_name, 0, 1, 1, 1)

        self.label_digits = QLabel("Digits:")
        self.gridLayout.addWidget(self.label_digits, 0, 2, 1, 1)

        self.label_sfx = QLabel("Sfx:")
        self.gridLayout.addWidget(self.label_sfx, 0, 3, 1, 1)


        self.comboBox_pfx = QComboBox()
        self.comboBox_pfx.addItem("l_")
        self.comboBox_pfx.addItem("r_")
        self.comboBox_pfx.addItem("up_")
        self.comboBox_pfx.addItem("dw_")
        self.gridLayout.addWidget(self.comboBox_pfx, 1, 0, 1, 1)

        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setMinimumSize(QSize(150, 0))
        self.gridLayout.addWidget(self.lineEdit_name, 1, 1, 1, 1)

        self.lineEdit_digit = QLineEdit()
        self.gridLayout.addWidget(self.lineEdit_digit, 1, 2, 1, 1)
        self.lineEdit_digit.setMaximumSize (QSize(50, 20))
        self.lineEdit_digit.setText("##")

        self.comboBox_sfx = QComboBox()
        self.comboBox_sfx.addItem("_CT")
        self.comboBox_sfx.addItem("_grp")
        self.comboBox_sfx.addItem("_jnt")
        self.comboBox_sfx.addItem("_ori")
        self.gridLayout.addWidget(self.comboBox_sfx, 1, 3, 1, 1)

        self.button_horizontalLayout = QHBoxLayout()
        self.layout.addLayout(self.button_horizontalLayout)

        self.pushButton_nonunik = QPushButton('Select nonunic')
        self.button_horizontalLayout.addWidget(self.pushButton_nonunik)

        self.pushButton_hierarhy = QPushButton("Rename hierarchy")
        self.button_horizontalLayout.addWidget(self.pushButton_hierarhy)

        self.pushButton_select = QPushButton("Rename selected")
        self.button_horizontalLayout.addWidget(self.pushButton_select)



if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()