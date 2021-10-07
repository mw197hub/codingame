import sys
import math


def cube(x):
    if 0<=x: return x**(1./3.)
    return -(-x)**(1./3.)


pList = {'Alice': [10807261.866810458, 0.0], 'BLARGHHH': [12.411752151763306, 514000000000.0], 'G7_24a': [6593.444826000909, 55100000000000.0]}

aliceD = 10807261.866810458
aliceR = float(4.70e11)
treffer = "not"
distanz = 0.0

for planet, wList in pList.items():
  #  print(planet,file=sys.stderr)
  #  print(wList,file=sys.stderr)
    if planet != "Alice":
        limitC = aliceR * cube(2 * aliceD / wList[0])
        if wList[1] >= limitC and (wList[1] < distanz or distanz == 0):
            treffer = planet
            distanz = wList[1]
    
print(treffer)