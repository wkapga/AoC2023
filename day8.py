from pathlib import Path
import re

import numpy as np
from pathlib import Path
import math

proj_path  = r"/home/gabi/python/aoc2023/AoC2023/"

input = open(Path(proj_path,'day8input.txt' ), 'r' ).read()

parts = input.split('\n\n')

nav = list(parts[0])

navdict = {'R':1, 'L' :0}

nodes = parts[1].split('\n')

dd = dict()
for node in nodes:
    kk = re.findall('^(\w{3})', node)[0]
    tu = re.findall('[A-Z,]{3}', node)[1:3]
    dd[kk] = tuple(tu)



step = 0
pointer = 0
nextnode = 'AAA'


while nextnode != 'ZZZ':
    nextnode = dd[nextnode][navdict[nav[pointer]]]
    step = step +1
    pointer = step % len(nav)
    if step == 2000000:
        break

step

## part 2


input = open(Path(proj_path,'day8input.txt' ), 'r' ).read()

parts = input.split('\n\n')

nav = list(parts[0])

navdict = {'R':1, 'L' :0}

nodes = parts[1].split('\n')

dd = dict()
for node in nodes:
    kk = re.findall('^(\w{3})', node)[0]
    tu = re.findall('[A-Z,0-9]{3}', node)[1:3]
    dd[kk] = tuple(tu)

dd

nextnodes = [x for x in list(dd.keys()) if x[-1]=='A']

step = 0
pointer = 0

cycles = np.zeros(len(nextnodes), dtype= int)

cycles


while cycles.min() == 0:
    oldnodes = nextnodes.copy()
    nextnodes = list()
    for i, nextnode in enumerate(oldnodes):
        # print(nextnode)
        if nextnode[-1] == 'Z':
            cycles[i] = step
        nextnodes.append( dd[nextnode][navdict[nav[pointer]]] )
    step = step +1
    pointer = step % len(nav)

   # print(nextnodes)
    if step == 500000:
        break
    if (step % 1000) == 0:
        print(step)

cycles

ll = 1

for x in cycles:
    ll = math.lcm(ll, x)
ll

