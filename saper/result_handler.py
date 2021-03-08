import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3 as sq
import tempfile
import os


class ResultHandler:
    def __init__(self, mode="SMALL"):
        with open('conf.json', 'r') as file:
            self.conf = json.load(file)
        self.db_path = os.path.join(tempfile.gettempdir(), self.conf["DATA_BASE"])
        self.mode = mode

    def get_win_list(self, mode):
        with sq.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS records' + mode + ' ( name Text, result Text )')
            data = cur.execute('SELECT name, result FROM records' + mode + ' ORDER BY result LIMIT 10')
        return data.fetchall()

    def add_result(self, obj, time, mode):
        text, ok = QInputDialog.getText(obj, 'Text Input Dialog', self.conf["WIN_TEXT"])
        if ok and text:
            with sq.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS records' + mode + ' ( name Text, result Text )')
                cur.execute('INSERT INTO records' + mode + ' VALUES ("' + text + '", "' + time + '")')

    def erase_records(self):
        with sq.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute('DROP TABLE   records' + self.mode)

    def show_result(self):
        records_data = self.get_win_list(self.mode)
        records_dealog = ResultDialog(records_data)
        records_dealog.exec_()


class ResultDialog(QDialog):
    def __init__(self, records_data):
        super(ResultDialog, self).__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.setWindowTitle("Records:")
        self.grid_layout = QGridLayout()
        self.layout.setSpacing(5)
        self.grid_layout.setColumnMinimumWidth(0, 100)
        self.layout.addLayout(self.grid_layout)
        for line in range(len(records_data)):
            name, val = records_data[line]
            name_label = QLabel(name)
            self.grid_layout.addWidget(name_label, line, 0, 1, 1)
            time_label = QLabel(val)
            self.grid_layout.addWidget(time_label, line, 1, 1, 1)
        self.cencel_btn = QPushButton("Cancel")
        self.layout.addWidget(self.cencel_btn)
        self.cencel_btn.clicked.connect(self.reject)


ResultHandler()
