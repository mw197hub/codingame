# https://www.codingame.com/ide/puzzle/vote-counting

import sys,math

nameDict={'Albert': 2, 'Roger': 1};voteList=[['Albert', 'Yes'], ['Roger', 'No'], ['Albert', 'Yes']]


yes=0;no=0
for name,votes in nameDict.items():
    anzahl=0;y,n=0,0
    for vList in voteList:
        if vList[0] == name:
            anzahl+=1
            if vList[1] == "Yes":
                y+=1
            elif vList[1] == "No":
                n+=1
    if anzahl <= votes:
        yes+=y
        no+=n
print(str(yes)+" "+str(no))