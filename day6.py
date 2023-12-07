from pathlib import Path
import re

import pandas as pd
import numpy as np
from pathlib import Path
import humanfriendly

import itertools
import math

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2023"

input = """Time:      7  15   30
Distance:  9  40  200"""

input = """Time:        59     79     65     75
Distance:   597   1234   1032   1328"""

parts = input.split('\n')

tm = list(map(int, re.findall('\s\d{1,4}', parts[0]) ) )
di = list(map(int, re.findall('\s\d{1,4}', parts[1]) ) )

tm = np.array(tm)
di = np.array(di)


b1 = np.floor(tm/2 + np.sqrt( (tm/2)**2 - di ) - 0.000001 )
b2 = np.ceil( tm/2 - np.sqrt( (tm/2)**2 - di ) + 0.000001 )

np.prod(b1-b2 +1)

# part2

map(str,tm.tolist())

tm = int(''.join(map(str,tm.tolist())))
di = int(''.join(map(str,di.tolist())))

b1 = np.floor(tm/2 + np.sqrt( (tm/2)**2 - di ) - 0.000001 )
b2 = np.ceil( tm/2 - np.sqrt( (tm/2)**2 - di ) + 0.000001 )

b1-b2 +1