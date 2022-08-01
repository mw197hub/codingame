from random import random
import sys
import math
import copy
import random
from fractions import Fraction


zaehler = 38 **7
nenner = 38*37*36*35*34*33
nenner = 38*38*38*38*38*36*37
# + (38*37*36*35*34*33*7)

#print(nenner)
#print(zaehler)
#print(int((nenner/zaehler * 100)+0.5))

zaehler = 38 **7
nenner = 38*37*36*35*34*33*7
#print(int((nenner/zaehler * 100)+0.5))

wert = 7/38 ** 7
#print((1-((6/38)**6)**7)*100)


#print(math.perm(38,7))
#print(6/38*100)
# print(6(1*5!+5(2*4!+4(3*3!+3(4*2!+2(5*1!+1*6))))))

m=6;n=7 #1
m=13;n=14 #2
#m=21;n=25
#m=24;n=37
#m=30;n=49

numList = [];treffer = 0
for i in range(20000):
    l = []
    for j in range(n):
        l.append(random.randint(0,37))        
    numList.append(copy.deepcopy(l))
for num in numList:
    numSet = set(num)
    if len(numSet) >= m:
        treffer +=1

print(str(int((treffer+49)/200))+"%")


OUTCOMES = 38
uniqs = [Fraction(1)]
for _ in range(n):
    next_uniqs = [Fraction(0)]
    for found, prob in enumerate(uniqs):
        prob_same = Fraction(found, OUTCOMES)
        next_uniqs[found] += prob * prob_same
        next_uniqs.append(prob * (1 - prob_same))
    uniqs = next_uniqs

print(f"{float(sum(uniqs[m:])):.0%}")

print(Fraction(1,6)**2)


z=0
for k in range(1,39-m):
  for j in range(1,39):
    z+=((-1)**(j-k))*math.comb(38,j)*math.comb(j,k)*(((38-j)**n)/(38**n))
print("%.0f%%"%(100*z))



def p(n, k):
    if k == 1: return 38
    if n == k: return math.perm(38, n)
    return p(n-1, k)*k + p(n-1, k-1)*(39-k)
s = sum(p(n, k) for k in range(m, min(n+1, 39)))
print(f"{s * 100 / (38**n):.0f}%")