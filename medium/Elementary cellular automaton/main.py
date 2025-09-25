# https://www.codingame.com/ide/puzzle/elementary-cellular-automaton

import sys,math
import numpy as np

r = int(input())
n = int(input())
start_pattern = input()

col = len(start_pattern)
# Make a grid and translate input to zeros and ones
grid = np.zeros((n,col), dtype=np.int)
for j,c in enumerate(start_pattern):
    grid[0,j] = c == '@'

# Get the 8-bit binary number from the rule integer
r_bin = bin(r)[2:]
r_bin = '0'*(8-len(r_bin)) + r_bin

# Define the rule for all possible neighborhoods
PATTERNS = ['111', '110', '101', '100', '011', '010', '001', '000']
rule_dict = dict()
for p,c in zip(PATTERNS, r_bin):
    rule_dict[p] = int(c)

# Calculate the evolution of the automaton
for i in range(1,n):
    for j in range(col):
        if j == 0:  # Left wrap-around
            t = np.concatenate([[grid[i-1, col-1]], grid[i-1, j:j+2]])
        elif j == col-1:  # Right wrap-around
            t = np.concatenate([grid[i-1, j-1:], [grid[i-1, 0]]])
        else:
            t = grid[i-1,j-1:j+2]
        # Look-up the next value in the 'rulebook'
        t = ''.join(str(d) for d in t)
        grid[i,j] = rule_dict[t]

# Translate back to '@' and '.' and print the result
for i in range(n):
    print(''.join('@' if g else '.' for g in grid[i]))
