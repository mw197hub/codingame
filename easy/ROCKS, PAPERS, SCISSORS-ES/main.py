#https://www.codingame.com/ide/puzzle/rocks-papers-scissors-es

import sys,math

def lauf(start,ergDict,enemyDict,pos,winDict,playDict):
    ergList=[];erg=0
    for i in range(len(enemyDict)):
        iPos = pos + i if pos + i < len(enemyDict) else pos + i - len(enemyDict)        
        if winDict[start] == enemyDict[iPos]:    
            ergList.append(enemyDict[iPos]);erg+=1
        elif start == enemyDict[iPos]:
            ergList.append(enemyDict[iPos]);erg-=0.1
        else:
            break
    ergList.insert(0,erg)
    ergDict[str(pos)+"#"+start] = ergList[:]


enemyDict={0: 'Paper', 1: 'Paper', 2: 'Paper', 3: 'Rock'}
enemyDict={0: 'Paper', 1: 'Rock', 2: 'Paper', 3: 'Rock', 4: 'Paper', 5: 'Rock', 6: 'Scissors'}

winDict={'Rock':'Scissors','Scissors':'Paper','Paper':'Rock'}
playDict={'Rock':['Rock','Paper'],'Scissors':['Scissors','Rock'],'Paper':['Paper','Scissors']}
ergDict={}

for i in range(len(enemyDict)):
    startList=playDict[enemyDict[i]]
    for start in startList:
        lauf(start,ergDict,enemyDict,i,winDict,playDict)

win="";winZahl=-1
print(ergDict,file=sys.stderr)
for erg,ergList in ergDict.items():
    if ergList[0] > winZahl:
        win=erg;winZahl=ergList[0]
winL=win.split("#")
print(winL[1])
print(winL[0])