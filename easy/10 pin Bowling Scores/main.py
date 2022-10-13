import sys
import math
from turtle import Vec2D

gameList=[['32', '71', '23', '44', '5-', '1-', '11', '15', '16', '7-']]
gameList=[['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX'], ['X', 'X', 'X', 'X', 'X', '-/', 'X', '4/', 'X', '4/8'], ['X', 'X', 'X', '-/', 'X', 'X', 'X', 'X', 'X', '8/5'], ['X', 'X', '7/', 'X', 'X', 'X', 'X', 'X', '-/', '-/6'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '2/X']]
gameList=[['7/', '-/', '5/', '72', '7/', '22', '6/', '-7', '7/', '--'], ['44', '1/', '2/', '-/', '-9', '81', '2/', '12', '7/', '5/6'], ['1/', '1/', '5/', '2/', '3/', '5/', '5/', '-/', '5/', '16']]
gameList=[['32', '7/', '6/', 'X', '2/', 'X', '1/', '11', '1/', 'X1/'], ['3-', '6/', 'X', '5/', '9/', 'X', '3/', '7/', '6/', '-/9'], ['X', 'X', 'X', '1/', '5/', 'X', '8/', '36', '3/', 'XX6'], ['7/', '7-', 'X', '7/', 'X', '2/', 'X', '8/', '9-', '61'], ['X', '7/', '9-', '3/', '8/', '5/', 'X', '52', 'X', '5/8']]


for game in gameList:
    ergS="";erg=0;v=0
    for i in range(len(game)):
        frame = game[i]
        for f in frame:
            if f in ['1','2','3','4','5','6','7','8','9']:
                erg+=int(f)
            if f == "/":
                erg=erg + 10 - v
                if i <9:
                    frame2=game[i+1]
                    if frame2[0] in ['1','2','3','4','5','6','7','8','9']:
                        erg+=int(frame2[0])
                    if frame2[0] =="X":
                        erg+=10
                    if frame2[0] == "/":
                        erg=erg + 10 - v
            if f == "X":
                erg+=10
                frame2="--"
                if i == 8:
                    frame2=game[i+1]
                if i < 8:
                    frame2=game[i+1]+game[i+2]
                for i2 in range(2):
                    if frame2[i2] in ['1','2','3','4','5','6','7','8','9']:
                        erg+=int(frame2[i2])
                    if frame2[i2] == "X":                        
                        erg+=10
                    if frame2[i2] == "/":
                        erg+=10-v
                    if frame2[i2] in ['1','2','3','4','5','6','7','8','9']:
                        v=int(frame2[i2])
                    else:
                        v=0
            if f in ['1','2','3','4','5','6','7','8','9']:
                v=int(f)
            else:
                v=0
        ergS=ergS+str(erg)+" "
    print(ergS[:-1])
