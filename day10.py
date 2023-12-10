from pathlib import Path
import re

import numpy as np
from pathlib import Path
import math

proj_path  = r"/home/gabi/python/aoc2023/AoC2023/"

input = open(Path(proj_path,'day10input0.txt' ), 'r' ).read()

lines =  input.split('\n')


# matrix j lines, k columns

j = len(lines)
k = len(lines[0])

conn = np.empty((4,j,k), dtype= bool)

conn[:]  = False

# west - east - north - south

symbs = dict({'-':(1,1,0,0),
      '|':(0,0,1,1),
      'F':(0,1,0,1),
      '7':(1,0,0,1 ),
      'L':(0,1,1,0),
      'J':(1,0,1,0)
      })

list(map(bool,symbs['7'])) 

s = np.zeros(2)

list(lines[0])

for i,line in enumerate(lines):
    for j, letter in enumerate(list(line)):
        # print(i,j, letter)
        if letter in symbs.keys():
            conn[:,i,j] = list(map(bool,symbs[letter]))
        if letter == 'S':
            s = [i,j]


s, conn

conn

lines


