from pathlib import Path
import re

import pandas as pd
import numpy as np

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2023"

input = open(Path(proj_path,'day1input0.txt' ), 'r' ).read()

s1 = input.split('\n')

n1 = list()
n2 = list()
for i, s in enumerate(s1):
     n1.append(int((re.findall('^[a-zA-Z]*(\d{1})', s) or [0])[0]) )
     n2.append(int((re.findall('(\d{1})[a-zA-Z]*$', s) or [0])[-1]) )

# n1 = [int(re.search('^[a-zA-Z]*(\d{1})', x ).group(1)) for x in s1]
# n2 = [int(re.search('(\d{1})[a-zA-Z]*$', x ).group(1)) for x in s1]

n3 = [10*x + y for x,y in zip(n1, n2)]

sum(n3)

nu1 = 'one, two, three, four, five, six, seven, eight, nine'.split(', ')
nu2 = 'o1e, t2o, th3ee, fo4r, f5ve, s6x, se7en, ei8ht, n9ne'.split(', ')

for i, nu in enumerate(nu1):
     s1 =   list(map(lambda x: x.replace(nu,str(i + 1) ), s1))


n1 = [int(re.search('^[a-zA-Z]*(\d{1})', x ).group(1)) for x in s1]
n2 = [int(re.search('(\d{1})[a-zA-Z]*$', x ).group(1)) for x in s1]

n3 = [10*x + y for x,y in zip(n1, n2)]

result2  = sum(n3)
result2
s1
