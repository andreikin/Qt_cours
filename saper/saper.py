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
        self.matrix = [[0 for i in range(self.width+2)] for j in range(self.height+2)]
        self.number_of_mines = int(self.width*self.height/100*conf["MINES_PERCENTAGE"])

    def __add_mines(self):
        pass

    def __str__(self):
        for i in self.matrix:
            print(* i)
        print(self.number_of_mines)


class Cell:
    # define cell functions
    pass

class GameUi:
    # draw ui
    pass

g = Game()

print(g)