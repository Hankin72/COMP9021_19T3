# COMP9021 19T3 - Rachid Hamadi
# Assignment 2 *** Due Sunday Week 10

from collections import defaultdict
import numpy as np
import os
from collections import deque


 # directions
# maze area
class MazeVertex(object):

    def check_directions(self):

        if self.value == '1':
            self.top = True
        elif self.value == '2':
            self.left = True
        elif self.value =='3':
            self.top = True
            self.left = True

        # right value
        if self.x+1 < self.x_len \
                and self.input_digits[self.y][self.x + 1] in {'2','3'}:
            self.right = True
        if self.y +1 < self.y_len \
                and self.input_digits[self.y+1][self.x] in {'1','3'}:
            self.down = True
        self.directions = [self.top, self.down, self.left, self.right]

    def __init__(self, x=0, y=0, input_digits=[[]]):
        self.x = x
        self.y = y
        self.value = None
        self.down = False
        self.right = False
        self.directions = [False, False, False, False]
        if 0 <= self.x < len(input_digits[0]) and 0 <= self.y < len(input_digits):
            self.input_digits = input_digits
            self.x_len = len(input_digits[0])
            self.y_len = len(input_digits)
            self.value = input_digits[y][x]
            self.check_directions()

    # #  output
    # def __str__(self):
    #     return f'x:{self.x}, y:{self.y}, top:{self.top}, down:{self.down}, left:{self.left}, right:{self.right}'
    # def __repr__(self):
    #     return f'x:{self.x}, y:{self.y}, top:{self.top}, down:{self.down}, left:{self.left}, right:{self.right}'
    #
class MazeArea(object):

    def __init__(self, x, y):
        self.start = (x,y)
        self.paths = []
        self.gates = set()
        self.cul_de_sacs =[]

    # def __str__(self):
    #     return f'start:{self.start}, paths: {self.paths}, gates:{self.gates}'
    # def __repr__(self):
    #     return f'start:{self.start}, paths: {self.paths}, gates:{self.gates}'
    #
class Maze():

    # read file
    def check_input_file(self,file):
        with open(file,'r') as files:
            for item in files:
                if not item.isspace():
                    self.input_digits.append (list(''.join(item.split())))

        # x dim [2, 31]
        # y dim [2, 41] lines
        len_y_dim = len(self.input_digits)
        len_x_dim = len(self.input_digits[0])
        if len_y_dim < 2 or len_y_dim > 41:
            raise MazeError('Incorrect input. ')
        for line in self.input_digits:
            if len_x_dim != len(line):
                raise MazeError('Incorrect input. ')
            else:
                len_x_dim = len(line)
                if len_x_dim <2 or len_x_dim > 31:
                    raise MazeError('Incorrect input. ')

                



    def __init__(self, filename):
        # OPEN filename
        self.file_name = file
        # all the digits
        self.init_digits = {'0','1','2','3'}
        self.visits = set([])
        self.queue = deque ()
        self.np_digits = None

        # input digits
        # the length of  x_dim, y _dim
        self.len_x_dim  = 0
        self.len_y_dim  = 0
        self.len_x_np = 0
        self.len_y_np = 0
        self.eight_directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        self.four_directions = [(-1,0),(1,0),(0,-1),(0,1)]
        self.input_digits = []

        # all the gates are dict
        self.gates = set ([])
        self.gate_count  =  0
        # walls
        self.walls_count = 0
        # areas
        self.areas = {}
        #  inaccessible inner point
        self.inaccessible_inner_point_count = 0
        # accessible _area_count = 0
        self.inaccessible_area_count = 0
        # pillars
        self.pillars = []
        # cul-de-sacs
        self.cul_de_sacs = []
        self.cul_de_sacs = 0
        # entry-exit path
        self.entry_exit_path =[]

        # read the maze file name
        self.check_input_file(file)
        # construct numpy array
        self.get_np_array()
        # get all gates
        self.get_gates()
        # get_walls
        self. get_Walls()
        # get inaccessible inner point and areas
        self.get_area_and_inner_point_count()
        # get_areas
        self.get_areas()
        # get cul-de-sacs and count
        self.get_cul_de_sacs()


    def __analyse(self):
        #print gates
        if self.gates_count == 0:
            print("The maze has no gate.")
        elif self.gates_count == 1:
            print("The maze has a single gate.")
        else:
            print(f"The maze has {self.gates_count} gates.")

        # print walls
        if self.walls_count == 0:
            print("The maze has no wall.")
        elif self.walls_count == 1:
            print("The maze has walls that are all connected.")
        else:
            print(f'The maze has {self.walls_count} sets of walls that are all connected.')

        # print inaccessible inner point
        if self.inaccessible_inner_point_count == 0:
            print("The maze has no inaccessible inner point.")
        elif self.inaccessible_inner_point_count == 1:
            print("The maze has a unique inaccessible inner point.")
        else:
            print(f"The maze has {self.inaccessible_inner_point_count} inaccessible inner points.")

        # print accessible area
        if self.accessible_area_count == 0:
            print("The maze has no accessible area.")
        elif self.accessible_area_count == 1:
            print("The maze has a unique accessible area.")
        else:
            print(f"The maze has {self.accessible_area_count} accessible areas.")

        # accessible cul - de - sac.
        if self.cul_de_sacs_count == 0:
            print("The maze has no accessible cul-de-sac.")
        elif self.cul_de_sacs_count == 1:
            print("The maze has accessible cul-de-sacs that are all connected.")
        else:
            print(f'The maze has {self.cul_de_sacs_count} sets of accessible cul-de-sacs that are all connected.')

        if len(self.entry_exit_path) == 0:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif len(self.entry_exit_path) == 1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {len(self.entry_exit_path)} '
                  f'entry-exit paths with no intersections not to cul-de-sacs.')

    def analyse(self):
        #print all the results
        self.__analyse()



def display(self):

        pass
        # REPLACE PASS ABOVE WITH YOUR CODE


class MazeError(Exception):
    def __init__(self, message):
        self.message = message
