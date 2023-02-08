# https://www.codingame.com/ide/puzzle/make-an-atari-font

import sys,math
import binascii

a_word = "ABC"

abc='0x1818243C42420000, A, 0x7844784444780000, B, 0x3844808044380000, C, 0x7844444444780000, D, 0x7C407840407C0000, E, 0x7C40784040400000, F, 0x3844809C44380000, G, 0x42427E4242420000, H, 0x3E080808083E0000, I, 0x1C04040444380000, J, 0x4448507048440000, K, 0x40404040407E0000, L, 0x4163554941410000, M, 0x4262524A46420000, N, 0x1C222222221C0000, O, 0x7844784040400000, P, 0x1C222222221C0200, Q, 0x7844785048440000, R, 0x1C22100C221C0000, S, 0x7F08080808080000, T, 0x42424242423C0000, U, 0x8142422424180000, V, 0x4141495563410000, W, 0x4224181824420000, X, 0x4122140808080000, Y, 0x7E040810207E0000, Z'
abcList = abc.split(",")

abcDict={}
for i in range(0,len(abcList),2):
    buch = abcList[i+1].strip()
    byt = abcList[i].strip()
    resList=[]
    for j in range(2,18,2):
        re = ("{0:08b}".format(int(byt[j:j+2], 16)));res=""
        for r in re:
            res = res + " " if r == "0" else res + "X"
                
        resList.append(res)
    abcDict[buch] =resList
#print(abcDict)
outList=[]
for i in range(8):
    outList.append("")

for a in a_word:
    cList = abcDict[a]
    for i in range(8):
        c = cList[i]
        outList[i] = outList[i] + c 
for out in outList:
    if "X" in out:
        print(out.rstrip())