import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from saper_ui import SaperUI
from field import Field
from cell import Cell
from result_handler import ResultHandler
import sqlite3 as sq

class Game(SaperUI):
    def __init__(self, mode="SMALL"):
        super(Game, self).__init__()
        self.mode = mode
        # load configurations
        with open('conf.json', 'r') as file:
            self.conf = json.load(file)
        self.init_game()

    def init_game(self):
        self.width = self.conf["FIELD_SIZE"][self.mode][0]
        self.height = self.conf["FIELD_SIZE"][self.mode][1]
        self.mines_num = int(self.width * self.height / 100 * self.conf["MINES_PERCENTAGE"])
        self.game_is_on = True  # if Folse - turns off time and mines counter
        self.cells_list = [["0" for i in range(self.width)] for j in range(self.height)]  # cell objects matrix
        self.pushButton_reset.setStyleSheet('QPushButton {background-color: light gray;}')
        self.generate_field(self.width, self.height, self.mines_num)
        self.__resize_widow()
        self.__start_timer()

    def __start_timer(self):
        self.label_time.setText("00:00")
        self.game_timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.game_timer.setInterval(1000)
        self.game_timer.timeout.connect(self.__change_time)
        self.game_timer.start()


    def __change_time(self):
        if self.game_is_on:
            self.time = self.time.addSecs(1)
            self.label_time.setText(self.time.toString("mm:ss"))
        else:
            self.game_timer.stop()

    def generate_field(self, width=15, height=10, mines_num=20):
        # create field object
        self.field = Field(width, height, mines_num)
        self.field.print_cell()
        for j in range(self.field.height):
            for i in range(self.field.width):
                cll = Cell(self.field.field[j][i], (j, i))
                cll.setObjectName(str(j) + " " + str(i) + " " + self.field.field[j][i])
                cll.installEventFilter(self)
                self.cells_list[j][i] = cll
                self.gridLayout_field.addWidget(cll, j, i, 1, 1)
        self.label_mines_count.setText(str(mines_num))

    def __resize_widow(self):
        win_width = self.width * self.conf["CELL_SIZE"] + 18
        win_height = self.height * self.conf["CELL_SIZE"] + 80
        self.setFixedSize(win_width, win_height)

    def __is_victory(self):
        open_sells_num=0
        for j in range(self.field.height):
            for i in range(self.field.width):
                if self.cells_list[j][i].opened:
                    open_sells_num += 1
        if not self.mines_num==0:
            return False
        return len(self.field.mines_list) + open_sells_num == self.field.height * self.field.width

    def __stop_game(self, show_mines=False):
        for j in range(self.field.height):
            for i in range(self.field.width):
                if show_mines:
                    if self.cells_list[j][i].status == "*":
                        self.cells_list[j][i].open_cell()
                        self.pushButton_reset.setStyleSheet('QPushButton {background-color: red; color: white;}')
                else:
                    self.pushButton_reset.setStyleSheet('QPushButton {background-color: green; color: white;}')
                self.cells_list[j][i].frozen = True
        self.game_is_on = False

    def eventFilter(self, cell, event):
        if event.type() == QEvent.MouseButtonPress:
            # Left click
            if event.button() == Qt.LeftButton:
                if cell.status == "*":
                    self.__stop_game(show_mines=True)
                else:
                    self.open_sells(cell.position[0], cell.position[1])
            # Right click
            elif event.button() == Qt.RightButton:
                self.__flags_caunter(cell)

            if self.__is_victory():
                self.__stop_game()
                #self.__win_dialog()
        return QObject.event(cell, event)

    def __flags_caunter(self, cell):
        if self.game_is_on and not cell.opened:
            if not cell.flag:
                self.mines_num -= 1
            else:
                self.mines_num += 1
            text_mines_num = self.mines_num if self.mines_num >= 0 else 0
            self.label_mines_count.setText(str(text_mines_num))

    # opens all fields adjacent to empty cells
    def open_sells(self, in_y, in_x):
        out_set = set()
        
        def __turn_off_flag(y, x):
            if self.cells_list[y][x].flag:
                self.mines_num += 1
                self.label_mines_count.setText(str(self.mines_num))
                print(self.mines_num)
            
        def __recursion_fun( y, x):
            if not self.field.field[y][x] == "0":  # if  cell status not 0
                __turn_off_flag(y, x)
                out_set.add((y, x))
                self.cells_list[y][x].open_cell()
            else:
                for coord_y in [y - 1, y, y + 1]:
                    for coord_x in [x - 1, x, x + 1]:
                        if (0 <= coord_y <= (len(self.field.field) - 1)) and \
                                (0 <= coord_x <= (len(self.field.field[0]) - 1)) and \
                                not (coord_y, coord_x) in out_set:
                            __turn_off_flag(coord_y, coord_x)
                            self.cells_list[coord_y][coord_x].open_cell()
                            out_set.add((coord_y, coord_x))
                            __recursion_fun(coord_y, coord_x)
        __recursion_fun(in_y, in_x)

    def __del_cells(self):
        for j in range(self.field.height):
            for i in range(self.field.width):
                self.cells_list[j][i].deleteLater()
        self.cells_list = [["0" for i in range(self.width)] for j in range(self.height)]

    def restart_resize_command(self, mode):
        self.__del_cells()
        if mode == "Restart":
            self.init_game()
        else:
            self.mode = mode
            self.init_game()

    def text_dialog (self, text_type):
        if text_type == "HELP_TEXT":
            title = "Game rules"
            text = self.conf["HELP_TEXT"]

        # elif text_type == "WIN_LIST":
        #     title = "Records"
        #     text = self.get_win_list()

        else:
            title = "About program"
            text = self.conf["ABOUT_PROGRAM"]
        help_dialog = QMessageBox()
        help_dialog.setWindowTitle(title)
        help_dialog.setText(text)
        help_dialog.setStandardButtons(QMessageBox.Cancel)
        help_dialog.exec_()

    # def win_dialog (self):
    #     text, ok = QInputDialog.getText(self, 'Text Input Dialog', self.conf["WIN_TEXT"])
    #     time = self.time.toString("mm:ss")
    #     if ok:
    #         with sq.connect(self.conf["DATA_BASE"]) as con:
    #             cur = con.cursor()
    #             cur.execute("""CREATE TABLE IF NOT EXISTS records (
    #             name Text,
    #             result Text
    #             )""")
    #             cur.execute('INSERT INTO records VALUES ("'+text+'", "'+time+'")')
    # #



if __name__ == '__main__':
    app = QApplication([])
    win = Game()
    win.show()
    app.exec_()
