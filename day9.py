from pathlib import Path
import re

import numpy as np
from pathlib import Path
import math

proj_path  = r"/home/gabi/python/aoc2023/AoC2023/"

input = open(Path(proj_path,'day9input0.txt' ), 'r' ).read()

series = input.split('\n')
ss = series[2]

n0 = np.array(list(map(int, ss.split(' '))))

diff_count = 0
n1 = n0.copy()
while sum(n1) != 0:
    n1 = np.ediff1d(n1)
    diff_count += 1



diff_count

np.ediff1d(n0)

