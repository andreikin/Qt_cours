import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3 as sq

class ResultHandler(QDialog):
    def __init__(self):
        super(ResultHandler, self).__init__()
        with open('conf.json', 'r') as file:
            self.conf = json.load(file)
        self.layout = QVBoxLayout(self)
        self.grid_layout = QGridLayout()
        self.grid_layout.setColumnMinimumWidth(0, 100)
        self.layout.addLayout(self.grid_layout)
        records_data = self.get_win_list()

        for line in range(len(records_data)):
            name, val = records_data[line]
            name_label = QLabel(name)
            self.grid_layout.addWidget(name_label, line, 0, 1, 1)
            time_label = QLabel(val)
            self.grid_layout.addWidget(time_label, line, 1, 1, 1)

        self.cencel_btn = QPushButton("Cancel")
        self.layout.addWidget(self.cencel_btn)
        self.cencel_btn.clicked.connect(self.reject)

    def get_win_list(self):
        with sq.connect(self.conf["DATA_BASE"]) as con:
            cur = con.cursor()
            data = cur.execute('SELECT name, result FROM records ORDER BY result LIMIT 10')
        # lines = []
        # for name, val in data.fetchall():
        #     lines.append(name+" "*(30-len(name))+ val+"\n")
        # return "".join(lines)

        return data.fetchall()