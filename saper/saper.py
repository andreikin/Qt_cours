import json
from random import randint

# load configurations
with open('conf.json', 'r') as file:
    conf = json.load(file)

class Game:
    # mine matrix
    # opening of voids
    def __init__(self, mode ="SMALL"):
        self.mode = mode
        self.width = conf["FIELD_SIZE"][self.mode][0]
        self.height = conf["FIELD_SIZE"][self.mode][1]
        # define matrix with 0 values
        self.matrix = [[0 for i in range(self.width+2)] for j in range(self.height+2)]
        self.mines_num = int(self.width*self.height/100*conf["MINES_PERCENTAGE"])
        self.__add_mines()

    def __add_mines(self):
        self.mines_list = []
        while len(self.mines_list)<self.mines_num:
            min_pos = (randint(1, self.width), randint(1, self.height))
            if not min_pos in self.mines_list:
                self.mines_list.append(min_pos)
                self.matrix[min_pos[1]][min_pos[0]] = '*'

    def __str__(self):
        for i in self.matrix:
            print(* i)
        print(self.mines_num)
        print(len(self.mines_list))


class Cell:
    # define cell functions
    pass

class GameUi:
    # draw ui
    pass

g = Game()

print(g)