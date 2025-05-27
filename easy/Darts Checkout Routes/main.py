# https://www.codingame.com/ide/puzzle/darts-checkout-routes

import sys,math,itertools

score=4;darts=2  #1


mWerte=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,50,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60]
erg=0


ergList=set()
mList = itertools.combinations_with_replacement(mWerte,darts)
for mL in mList:
    if sum(mL) == score:
        #print(mL)
        ergList.add(mL[:])
print(ergList)

print(erg)

singles = {val:f"{val}" for val in [i for i in range(1,21)]+[25]}
doubles = {val:f"D{val//2}" for val in [i*2 for i in range(1,21)]+[50]}
trebles = {val:f"T{val//3}" for val in [i*3 for i in range(1,21)]}

combinations = set()
def search(score, darts, left):
    if score < 0 or left == -1:
        return
    
    if score == 0 and darts and "D" in str(darts[-1]):
        combinations.add(tuple(darts))
        return

    for arr in [singles, doubles, trebles] if left > 1 else [doubles]:
        for dart, dart_str in arr.items():
            search(score - dart, darts+[dart_str], left - 1)         
    return

search(score, [], darts)
print(len(combinations))