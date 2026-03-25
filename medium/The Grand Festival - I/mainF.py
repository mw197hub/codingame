##
import sys,math


F = dict()
def f(x):
    if x in F:
        return F[x]
    if x >= len(prizes) - rest:
        F[x] = sum(prizes[x:])
        return F[x]
    result = []
    for r in range(rest+1):
        result.append(sum(prizes[x:x+r])+f(x+r+1))
    F[x] = max(result)
    return F[x]
    

rest=3
prizes=[13, 12, 11, 9, 16, 17, 100] #1   169
print(f(0))