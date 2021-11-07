import sys
import math
import itertools


ausgangsList = ['1','2','3','4','5']

permuList = itertools.permutations(ausgangsList)
permuList = [p + (p[0],) for p in permuList]   # erstes Element hinten anhängen
for per in permuList:
    print(per)
print(len(permuList))