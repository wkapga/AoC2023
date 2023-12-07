from pathlib import Path
import re

import pandas as pd
import numpy as np
from pathlib import Path
import humanfriendly

import itertools
import math

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2023"

input = open(Path(proj_path,'day5input.txt' ), 'r' ).read()

parts = input.split('\n\n')

# extract the seeds
seeds = list(map(int,re.findall(' \d+', parts[0])))


# list of lists for mapping
parts = parts[1:]

key = list()
value = list()
for p in parts:
    key.append(re.findall('(\w+-to-\w+) map:', p)[0])
    value.append(p.split('\n')[1:])

value2 = list()
for v in value:
    value2.append(list(map(lambda x: x.split(' '),v )) )

value3 =[[[int(v) for v in innerst_list] for innerst_list in inner_list] for inner_list in value2]


#seeds = seeds[:1]
# push the path per seed into an array
# set up array
paths = np.empty((len(seeds),8,), dtype=np.longlong)
#paths[:] = np.nan
paths[:] = -999999

# find the way
for i,path in enumerate(paths):
    print(i)
    paths[i,0] = seeds[i]
    for j, step in enumerate(path):
        if (j > 0) :
            print((i,j-1))
            print((paths[i,j-1],value3[j-1]) )
            for m in value3[j-1]:
                
                paths[i,j] = paths[i,j-1]
               # if paths[i,j] in range(m[1], m[1] + m[2]):
                if ( (paths[i,j] >= m[1]) and (paths[i,j] <= (m[1]+m[2]) ) ):
                    paths[i,j] = paths[i,j]-m[1]+m[0]
                    print(m[1])
                    break
paths

paths[0,0]

# result
min(paths[:,7])

# part 2
# nr of seeds to test
humanfriendly.format_number( sum(seeds[1::2]) )

# no no no