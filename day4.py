from pathlib import Path
import re

import pandas as pd
import numpy as np
from pathlib import Path

import itertools
import math

proj_path  = r"C:\Users\WKAPGA\OneDrive - Raiffeisen Bank International Group\python\aoc\2023"

input = open(Path(proj_path,'day4input.txt' ), 'r' ).read()

lines = input.split('\n')

nr_of_hits = list()

for i, l in enumerate(lines):
    line = l.split('|')
    card_numbers =      set(map(int, re.findall('\d+ ', line[0]) ) )
    winning_numbers =   set(map(int, re.findall(' \d+', line[1]) ) )
    print(card_numbers)
    print(winning_numbers) 
    nr_of_hits.append(len(card_numbers.intersection( winning_numbers )) )
    print(i)
    

# use numpy
nr_of_hits = np.array(nr_of_hits)

# result
np.power(2, ( nr_of_hits[nr_of_hits >0]-1 ) ).sum()

# part 2

nr_of_cards = np.ones([len(nr_of_hits)])

for i, hits_of_current_card in enumerate(nr_of_hits) :
    nr_of_cards[i+1:(i + hits_of_current_card + 1)]  =  nr_of_cards[i+1:(i + hits_of_current_card + 1)] + nr_of_cards[i]


nr_of_cards.sum()