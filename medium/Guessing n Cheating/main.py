# https://www.codingame.com/ide/puzzle/guessing-n-cheating

import sys,math



inputList=['5 too high', '1 too high', '2 right on'] #1
inputList=['33 too low', '21 too low', '32 too high', '31 right on'] #11
inputList=['20 too high', '19 too high', '18 too low', '19 right on'] #2 validator



round=0
uGrenze=1;oGrenze=100

for i in range(len(inputList)):
    iList = inputList[i].split(" ")
    if iList[2] == "high":
        if int(iList[0]) <= oGrenze:
            oGrenze = int(iList[0]) -1
        if int(iList[0]) <= uGrenze:
            round = i +1; break
    elif iList[2] == "low":
        if int(iList[0]) >= uGrenze:
            uGrenze = int(iList[0]) +1
        if int(iList[0]) >= oGrenze:
            round = i + 1;break
    else:
        if int(iList[0]) >= uGrenze and int(iList[0]) <= oGrenze:
            continue
        else:
            round = i + 1
            break
   # if oGrenze - uGrenze <= 1:
   #     round = i + 1;break

if round > 0:
    print("Alice cheated in round {}".format(round))
else:
    print("No evidence of cheating")