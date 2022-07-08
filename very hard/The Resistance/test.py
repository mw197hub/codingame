import sys
from itertools import permutations
from itertools import combinations

perm1=permutations(['B','A','A','A','A','A','A'],)
perm2=permutations(['B','B','A','A','A'])

erg1=[];erg2=[]
for i in list(perm1):
    if not i in erg1:
        erg1.append(i)
for i in list(perm2):
    if not i in erg2:
        erg2.append(i)
#print(list(perm1))
#print(list(perm2))
print(len(erg1))
print(len(erg2))
#print(erg1),print(erg2)
print(1+1+len(erg1)+len(erg2))

