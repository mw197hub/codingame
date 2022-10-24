import sys
import math
import string

#print(string.ascii_lowercase)

#speedDict={a: 56, b: 6, c: 2, d: 23, e: 9, f: 25, g: 41, h: 15}
speedDict={0: 56, 1: 6, 2: 2, 3: 23, 4: 9, 5: 25, 6: 41, 7: 15}
bendsList=[40, 30]

speedDict={0: 25, 1: 17, 2: 35, 3: 11, 4: 2, 5: 15, 6: 22, 7: 56, 8: 8, 9: 46, 10: 6}
bendsList=[5]


ergDict={}
maxA = 60 * math.pi / 180

maxSpeed=int(math.sqrt(math.tan(maxA)*min(bendsList)*9.81))
print(maxSpeed)
ergDict['y'] = maxSpeed
for nr,speed in speedDict.items():
    #print("Speed: " + str(speed))
    anz=0
    for r in bendsList:
        deg = speed **2 / (r * 9.81)
        erg =(math.atan(deg))
        if erg < maxA:
            anz+=0.1+(speed/10000)
        else:
            anz+=(speed/10000)
            break
    if anz == len(bendsList):
        ergDict[string.ascii_lowercase[nr]] = speed
    else:
        ergDict[string.ascii_lowercase[nr]] = anz

print(ergDict,file=sys.stderr)
for w in sorted(ergDict, key=ergDict.get, reverse=True):
    if ergDict[w] > 0:
        print(w)
for w in sorted(ergDict):
    if ergDict[w] == 0:
        print(w)
