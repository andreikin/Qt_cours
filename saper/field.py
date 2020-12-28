import json
from random import randint

# load configurations
with open('conf.json', 'r') as file:
    conf = json.load(file)

class Fild:
    # mine matrix
    # opening of voids
    def __init__(self, mode ="SMALL"):
        self.mode = mode
        self.width = conf["FIELD_SIZE"][self.mode][0]
        self.height = conf["FIELD_SIZE"][self.mode][1]
        # generate matrix with 0 values for each cell
        self.matrix = [["0" for i in range(self.width+2)] for j in range(self.height+2)]
        self.mines_num = int(self.width*self.height/100*conf["MINES_PERCENTAGE"])
        self.__add_mines()
        self.__solve_num_for_each_cell()

    def __add_mines(self):
        self.mines_list = []
        while len(self.mines_list)<self.mines_num:
            min_pos = (randint(1, self.width), randint(1, self.height))
            if not min_pos in self.mines_list:
                self.mines_list.append(min_pos)
                self.matrix[min_pos[1]][min_pos[0]] = '*'

    def __solve_num_for_each_cell(self):
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                if not self.matrix[i][j] == '*':
                    up_line = "".join(self.matrix[i - 1][j - 1:j + 2]).count("*")
                    mid_line = "".join(self.matrix[i][j - 1:j + 2]).count("*")
                    dw_line = "".join(self.matrix[i + 1][j - 1:j + 2]).count("*")
                    self.matrix[i][j] = str(up_line+mid_line+dw_line)




    def print_cell(self):
        for i in self.matrix:
            print(* i)


class Cell:
    # define cell functions
    pass




g = Game()
g.print_cell()

