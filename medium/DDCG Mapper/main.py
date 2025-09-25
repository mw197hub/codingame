# https://www.codingame.com/ide/puzzle/ddcg-mapper

import sys,math

l=7;patternDict={2: 'X000', 3: '00XX'}


ausList=[]
for i in range(l):
    ausgabe=["0","0","0","0"]
    for tempo,pattern in patternDict.items():
        rest =(i+1) % tempo
        if rest == 0:
            for j in range(4):
                if pattern[j] == "X":
                    ausgabe[j] = "X"

    ausList.append(ausgabe)

for i in range(l):
    ausgabe = ausList.pop()
    aus2=""
    for a in ausgabe:
        aus2+=a
    print(aus2)