import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Emit(QMainWindow):
    def __init__(self, parent=None):
        super(Emit, self).__init__()
        self.resize(250, 150)

        searchRequested = SIGNAL('closeEmitApp()')

        self.connect(self, searchRequested, SLOT('close()'))

    def mousePressEvent(self, event):
        self.emit(SIGNAL('closeEmitApp()'))


app = QApplication(sys.argv)
qb = Emit()
qb.show()
sys.exit(app.exec_())
