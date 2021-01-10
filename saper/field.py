from random import randint

class Field:
    def __init__(self, width, height, mines_num):
        self.width = width
        self.height = height
        self.mines_num = mines_num
        self.mines_list = []
        self.__generate_field()

    def __add_mines(self):
        while len(self.mines_list)<self.mines_num:
            min_pos = (randint(1, self.width), randint(1, self.height))
            if not min_pos in self.mines_list:
                self.mines_list.append(min_pos)
                self.field[min_pos[1]][min_pos[0]] = '*'

    def __solve_num_for_each_cell(self):
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                if not self.field[i][j] == '*':
                    up_line = "".join(self.field[i - 1][j - 1:j + 2]).count("*")
                    mid_line = "".join(self.field[i][j - 1:j + 2]).count("*")
                    dw_line = "".join(self.field[i + 1][j - 1:j + 2]).count("*")
                    self.field[i][j] = str(up_line+mid_line+dw_line)

    def __generate_field(self):
        # generate field with 0 values for each cell with extra sells
        self.field = [["0" for i in range(self.width+2)] for j in range(self.height+2)]
        self.__add_mines()
        self.__solve_num_for_each_cell()
        # cat extra cells
        self.field = [x[1:-1] for x in self.field[1:-1]]

    def print_cell(self):
        print (*"_"*len(self.field[0]))
        for i in self.field:
            print(* i)


# if __name__ == '__main__':
#
# #from field import Field, get_sells_around
#     g = Field(10, 10, 20)
#     g.print_cell()
#
#     get_sells_around(g.field, 5, 5)
