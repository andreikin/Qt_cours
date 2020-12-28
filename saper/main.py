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
        self.mines_num = int(self.width * self.height / 100 * conf["MINES_PERCENTAGE"])


    def print_cell(self):
        for i in self.matrix:
            print(* i)



g = Game()
g.print_cell()

