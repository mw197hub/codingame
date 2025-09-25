# https://www.codingame.com/ide/puzzle/number-of-letters-in-a-number---binary


import sys,math

def itter(n, k): 
    k = min(k, 15)
    for i in range(k): 
        n = to_next(n) 
    return n 
    
def to_next(n): 
    n_str = bin(n) 
    return len(n_str) * 3 + n_str.count('0') - 7

start=5;n=2

print(itter(start, n))