from json import dumps, loads
from typing import List
import sys


def testLauf(start,befehle,richtung,richtungen):
    for befehl in befehle:
        if befehl == "FORWARD":
            start[0]+=richtungen[richtung][0]
            start[1]+=richtungen[richtung][1]
        if befehl == "BACK":
            start[0]-=richtungen[richtung][0]
            start[1]-=richtungen[richtung][1]
        if befehl == "TURN RIGHT":
            richtung+=1
            if richtung > 3:
                richtung = 0
        if befehl == "TURN LEFT":
            richtung-=1
            if richtung < 0:
                richtung = 3
    return start

json = "Replace instruction 1 with BACK"


instructions=["BACK", "TURN RIGHT", "FORWARD", "TURN RIGHT", "FORWARD", "FORWARD", "FORWARD", "FORWARD"]
#befehle=["TURN RIGHT", "TURN RIGHT", "FORWARD", "TURN RIGHT", "FORWARD", "FORWARD", "FORWARD", "FORWARD"]
ziel=[-1,4]

instructions=['FORWARD', 'FORWARD', 'FORWARD', 'TURN RIGHT', 'TURN RIGHT', 'TURN RIGHT', 'BACK', 'TURN LEFT', 'TURN LEFT', 'FORWARD']
ziel=[-1,-1]

richtungen=[[1,0],[0,-1],[-1,0],[0,1]]
richtung=0
pos=[0,0]
moeglichkeiten=["BACK", "TURN RIGHT", "FORWARD", "TURN LEFT"]
pos=0;b=""
for i in range(len(instructions)):
  ursprung=instructions[i]
  for m in moeglichkeiten:
      if not m == ursprung:
        testBefehl=instructions[:]
        testBefehl[i] = m
        erg=testLauf([0,0],testBefehl,richtung,richtungen)
        if erg == ziel:
          pos=i+1;b=m

erg= "Replace instruction "+str(pos)+" with " + b
print(erg)