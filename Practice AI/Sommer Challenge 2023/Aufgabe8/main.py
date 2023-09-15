from json import dumps, loads
from typing import List
import sys


def testLauf(start,befehle,richtung,richtungen,obstacles):
    for befehl in befehle:
        if befehl == "F":
            start[0]+=richtungen[richtung][0]
            start[1]+=richtungen[richtung][1]
        if befehl == "B":
            start[0]-=richtungen[richtung][0]
            start[1]-=richtungen[richtung][1]
        if befehl == "R":
            richtung+=1
            if richtung > 3:
                richtung = 0
        if befehl == "L":
            richtung-=1
            if richtung < 0:
                richtung = 3
        if start in obstacles:
            return [0,0]
    return start

json = "Replace instruction 1 with BACK"


instructions="LFLFLB"
ziel=[-1,0]
obstacles=[[-1, 1]]

instructions="FRFLFRFLFRFFFFFRFLFFFLLFLLFFLLFFFRRRFFLLLLFFFFFFFRRFRRLFLFRFFRFFFLFFFFFFFRFFLLFFRFFRLLLFLRFRFRFRFFLLLFFRFFFFFFLFRFLLLFFLFRRFFFRFRFFRRRRLFRRRLLFFRFFFFLLLLRFFFLFFFLFFFRFLFLLFFFFLLLFRFFFRFFFRFFRLLLFRRFFFFFFLLLFRFRFLFFFFLFLFLBRFRFFLFFFFFRRFRFRLLFLFFFLFLLFLFRFFLFLFLFLLFLFLLFLLFLFFLFRFRFRRFFFFLFFFFRLFRFFLFFLLFLFLRLFLLFFFFLFFRRFFRLFFRFLFFLLFLFRFFRFLLLFRRRRFFFLFFRFFFFFLFRRFFFLFLFFRFRFLLFFRFFLFLLLFRFFFRLLFLLLLFFLLLLLRRFFFFFLFFFFRRFFRFLFFLFFLFRFFFRRFFFLFLBFRLLFFFRRRFRFFFFLFLLFFLFFLFFRRLFRFFFLLLLFRFRFLLFFFFRRFRFRRFFFRRFLFFFFRRRFFLFFFFLLFFFFLFLLLFFFFFFRFFFLLLLFFFRFFRFFFFFLLLFFFLFFRRFFLLFFFFFRFFFFRFRFFLFRRRRFLLFRFLRFRFLFRFRFFRRFFFRRRRLFRFRRRFFRFRFLFFRRFFFFRRFFFLLLFRFFFFLRFFLRRFRFFLFLLFFLLLRFFFLLFLLFFLFFFFRLLFRLFFFFRRRFFLFFLLFBFLFLFRFFFFFLFRLFFFFFRRFLLFRFLRLFFFFFFRRLLFFRRRFFRRFFRFRFFFRFLFFLFFLFLFFLFRFFFRRFRFFFFLFRFFFRFFLFFRFFRFRFFRFLFRFRFLFLFRFLFRFFLLFLRFRFRFFRFFLFFLLFRRFLFFRFLFFBFLRRRFFLFFFLFFFFRRFLFFFRRRFFFFRFLFFFRRFLFLRLLLRRFRFFFLBLFFLLRFRFRFRFLLLFRRFLFFLFLFRFFFLFLFFFFLFFFLLFFLFRRRFLFLLRFLFRRRRFL"
ziel=[-45,-19]
obstacles=[[21, -31], [12, 7], [-8, -28], [-11, -34], [-45, -2], [3, -41], [-25, -26], [-30, -45], [-7, -9], [-29, -42], [-15, -1], [19, 14], [-16, 22], [-7, -12], [-20, -34], [19, -16], [19, -39], [17, -5], [-36, -48], [21, -16], [-38, 6], [-25, -31], [15, 15], [-36, 2], [-25, 11], [-34, -5], [9, 16], [-10, 29], [11, -36], [9, -39], [25, -33], [28, 6], [23, -18], [-14, -44], [-5, -14], [-4, -15], [-23, -39], [5, 16], [11, -45], [-15, 15], [23, 29], [-14, -42], [-1, 8], [-40, -26], [4, -14], [-46, -30], [-16, -59], [-17, -12], [4, 5], [22, -27], [9, 6], [-8, 23], [-33, -31], [-32, 10], [-24, -35], [-16, 23], [1, -15], [-10, -13], [-13, -46], [-10, 1], [-10, -35], [-44, -6], [-25, -47], [16, 1], [-26, -46], [-33, -10], [-20, -37], [-21, 19], [-13, -49], [-1, -1], [-22, 22], [-25, 14], [-11, -4], [-42, -16], [-22, -43], [4, -16], [5, -37], [6, -37], [-25, -49], [-38, -12], [9, -1], [-21, 21], [-3, -10], [-26, -24], [-33, -38], [13, -37], [0, -11], [5, -1], [7, -48], [23, 23], [-4, -55], [-27, -46], [-25, -54], [-29, 12], [-26, -55], [-32, 12], [20, 12], [-5, -7], [-23, -55], [-32, -38], [11, -28], [-17, -57], [-36, -32], [-26, -48], [25, 16], [-4, -53], [-47, -2], [0, 19], [-35, -19], [20, -9], [8, -12], [11, 11], [7, -29], [-34, -43], [-3, -7], [17, -1], [7, -2], [1, -5], [-19, -48], [22, -3], [16, 0], [-28, -1], [-12, 2], [-2, -40], [-8, -8], [1, -3], [-36, -17], [-9, 25], [18, 2], [-52, -18], [-15, 9], [13, -7], [-42, -29], [4, -32], [-25, -45], [-28, -31], [-27, -21], [27, -8], [-13, -22], [-9, 5], [22, 13], [16, -25], [-30, 14], [30, 12], [-5, -42], [29, -20], [-25, -5], [-46, -1], [4, -37], [-16, 14], [-6, -2], [-9, -50], [-12, 1], [24, -18], [9, -34], [26, -24], [-49, -30], [20, 10], [19, -37], [9, -21], [-45, -11], [26, 2], [-20, -42], [4, -50], [-33, -26], [-3, -41], [20, -20], [13, -1], [26, 16], [1, -45], [-20, 9], [-29, -43], [-31, -44], [-37, -45], [27, 0], [28, -10], [-11, 26], [18, -20], [20, 5], [-27, -32], [-41, -9], [9, 4], [-5, -36], [-47, -22], [-16, -6], [-40, -20], [-6, -6], [-10, 3], [-7, -36], [5, -8], [-7, 23], [-10, -5], [-23, -43], [-15, -3], [-25, -22], [-21, -45], [23, -12], [-18, 12], [-42, 8], [-7, -5], [10, -16], [21, -11], [-25, -59], [10, 16], [-14, 21], [2, -34], [-3, 10], [-49, -14], [-9, -49], [-37, -14], [2, -32], [-28, 5], [-20, 3], [7, -42], [20, 22], [5, 2], [2, 5], [-11, -14], [29, 13], [5, -43], [14, -42], [-23, -50], [-50, -16], [24, -2], [0, -9], [-6, 20], [-15, -59], [-37, -41], [-48, -5], [29, -19], [-12, 7], [-11, -24], [-29, -60], [-19, -36], [-49, -22], [2, -27], [-10, 27], [22, 11], [13, -23], [0, -42], [-29, -44], [12, 6], [8, -42], [-40, -19], [-8, -37], [-6, 12], [-4, -31], [20, -6], [-8, -24], [-8, 12], [-33, -16], [26, -32], [-15, 30], [-43, -29], [16, -21], [-13, -39], [-1, -25], [13, -32], [-46, 0], [1, 12], [-2, -4], [12, -35], [11, -33], [-12, 30], [-2, 24], [-1, -43], [-34, -27], [-9, 4], [-37, -27], [-49, -7], [-5, -20], [-35, -36], [-48, -21], [-24, -31], [-23, -28], [-25, -61], [8, -35], [22, -20], [-29, 8], [8, -2], [-17, -48], [5, -36], [-24, -24], [-40...


instruction=list(instructions)
richtungen=[[1,0],[0,-1],[-1,0],[0,1]]
richtung=0
pos=[0,0]
moeglichkeiten=["B", "R", "F", "L"]
pos=0;b=""
for i in range(len(instruction)):
  ursprung=instruction[i]
  for m in moeglichkeiten:
      if not m == ursprung:
        testBefehl=instruction[:]
        testBefehl[i] = m
        erg=testLauf([0,0],testBefehl,richtung,richtungen,obstacles)
        if erg == ziel:
          pos=i+1;b=m

moegDict={"B":"BACK", "R":"TURN RIGHT", "F":"FORWARD", "L":"TURN LEFT"}
bef = moegDict[b]
erg= "Replace instruction "+str(pos)+" with " + bef
print(erg)