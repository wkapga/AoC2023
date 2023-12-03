from pathlib import Path
import re

import pandas as pd
import numpy as np
from pathlib import Path

import itertools
import math

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2023"

input = open(Path(proj_path,'day2input' ), 'r' ).read()

s1 = input.split('\n')

# part 1

n = len(s1) 

gam = list()
red = list()
gre = list()
blu = list()

for i, s in enumerate(s1):
     gam.append(max(map(int, re.findall('Game (\d+):', s ) ) ) )
     red.append(max(map(int, re.findall(' (\d+) red', s) )))
     gre.append(max(map(int, re.findall(' (\d+) green', s) )))
     blu.append(max(map(int, re.findall(' (\d+) blue', s) )))


g = [all(x) for x in zip([x <= 12 for x in red] , [x <= 13 for x in gre] , [x <= 14 for x in blu])  ]


r = list(itertools.compress(gam, g) ) 

sum(r)

# part 2

gam = list()
red = list()
gre = list()
blu = list()

for i, s in enumerate(s1):
     gam.append(max(map(int, re.findall('Game (\d+):', s ) ) ) )
     red.append(max(map(int, re.findall(' (\d+) red', s) )))
     gre.append(max(map(int, re.findall(' (\d+) green', s) )))
     blu.append(max(map(int, re.findall(' (\d+) blue', s) )))


r = [math.prod(x) for x in zip(red, gre, blu)  ]

sum(r)
