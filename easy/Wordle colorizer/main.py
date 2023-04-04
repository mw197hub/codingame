# https://www.codingame.com/ide/puzzle/wordle-colorizer

import sys,math

answer="POLKA"
attemptList=['QUICK', 'BROWN', 'GLADY', 'POLKA']

answer="WATER"
attemptList=['MILKY', 'AWAIT', 'TWATS', 'WATCH', 'WATER']



for attempt in attemptList:
    erg=["X" for _ in range(len(answer))]
    rest=[]
    for i in range(len(answer)):
        if attempt[i] == answer[i]:
            erg[i] = "#"
        else:
            rest.append(answer[i])
    for i in range(len(answer)):
        if not erg[i] == "#" and attempt[i] in rest:
            erg[i] = "O"
            rest.remove(attempt[i])

    print("".join(erg))