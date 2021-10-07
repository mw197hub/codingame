import sys
import math

def tauschen(rubik,moveL):
    for ur,wert in rubik.items():
        for move in moveL:
            if wert == move[0]:
                rubik[ur] = move[1]
                break

def drehen(rubik,rotations):
    for r in rotations:
        if r == "z":
            tauschen(rubik,["LU", "UR", "RD", "DL"])
        if r == "z'":
            tauschen(rubik,["LD", "UL", "RU", "DR"])
        if r == "y'":
            tauschen(rubik,["BL", "RB", "FR", "LF"])
        if r == "y":
            tauschen(rubik,["BR", "RF", "FL", "LB"])
        if r == "x":
            tauschen(rubik,["UB", "FU", "DF", "BD"])
        if r == "x'":
            tauschen(rubik,["UF", "FD", "DB", "BU"])


rubik = {"D":"D","F":"F","B":"B","U":"U","R":"R","L":"L"}
rotations = "y z'".split(" ")
face_1 = "B"
face_2 = "D"
drehen(rubik,rotations)
print(rubik[face_1])
print(rubik[face_2])