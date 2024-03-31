# https://www.codingame.com/ide/puzzle/scrabble-score

import math,sys

def addWert(y,x,buchstabe,sonderDict,scoreDict,played):
    w = scoreDict[buchstabe]
    sWord=1
    if [y,x] in played:
        if str(y)+"-"+str(x) in sonderDict:
            sond = sonderDict[str(y)+"-"+str(x)]
            if sond == "l":
                w*=2
            if sond == "L":
                w*=3
            if sond == "w":
                sWord=2
            if sond == "W":
                sWord=3
    return w,sWord

#1
scoreDict={'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, '_': 0}
emptyList=['W..w', '....', '....', 'l..L'];previousList=['....', '.OR.', '....', '....'];playedList=['....', '.OR.', '.F..', '....']
#4
scoreDict={'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2, 'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10, '_': 0}
emptyList=['W..w', '....', '....', 'l..L'];previousList=['....', '....', '.ROI', '....'];playedList=['...Q', '...U', '.ROI', '....']
#5
scoreDict={'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2, 'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10, '_': 0}
emptyList=['l........w', '..........', '..........', '..........', '..........', '..........', '..........', 'W........L'];previousList=['..........', '....F.....', '....R.....', '....O.....', '....M.....', '....A.....', '....G.....', '....E.....'];playedList=['..........', '....F.....', '....R.....', '....O.....', '....M.....', '....A.....', '....G.....', 'OMELETTE..']
#7
scoreDict={'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, '_': 0}
emptyList=['W..L..W', '.w...w.', '..l.l..', 'L..w..L', '..l.l..', '.w...w.', 'W..L..W'];previousList=['.TEST..', '..A....', '..S....', '..T....', '.......', '.......', '.......'];playedList=['.TESTS.', '..A..I.', '..S..C.', '..T..K.', '.......', '.......', '.......']



######
sonderDict={}
played=[]
werte={}
total=0
for y in range(len(playedList)):    
    line = emptyList[y]
    for x in range(len(line)):
        if not line[x] == ".":
            sonderDict[str(y)+"-"+str(x)] =  line[x]
    if not playedList[y] == previousList[y]:        
        line=playedList[y]
        line2=previousList[y]
        for x in range(len(line)):
            if not line[x] == line2[x]:
                played.append([y,x])
print(played,file=sys.stderr)
print(sonderDict,file=sys.stderr)



for play in played:
    word1=playedList[play[0]][play[1]];word2=playedList[play[0]][play[1]]
    wert1,multi1=addWert(play[0],play[1],playedList[play[0]][play[1]],sonderDict,scoreDict,played)
    wert2=wert1;multi2=multi1
    for y in range(play[0]-1,-1,-1):
        if not playedList[y][play[1]] == ".":
            word1=playedList[y][play[1]]+word1
            wert0,multi0=addWert(y,play[1],playedList[y][play[1]],sonderDict,scoreDict,played)
            wert1+=wert0;multi1=multi1*multi0
        else:
            break
    for y in range(play[0]+1,len(playedList),+1):
        if not playedList[y][play[1]] == ".":
            word1=word1+playedList[y][play[1]]
            wert0,multi0=addWert(y,play[1],playedList[y][play[1]],sonderDict,scoreDict,played)
            wert1+=wert0;multi1=multi1*multi0
        else:
            break
    for x in range(play[1]-1,-1,-1):
        if not playedList[play[0]][x] == ".":
            word2=playedList[play[0]][x]+word2
            wert0,multi0=addWert(play[0],x,playedList[play[0]][x],sonderDict,scoreDict,played)
            wert2+=wert0;multi2*=multi0
        else:
            break
    for x in range(play[1]+1,len(playedList[0]),+1):
        if not playedList[play[0]][x] == ".":
            word2=word2+playedList[play[0]][x]
            wert0,multi0=addWert(play[0],x,playedList[play[0]][x],sonderDict,scoreDict,played)
            wert2+=wert0;multi2*=multi0
        else:
            break

    wert1=wert1*multi1
    wert2=wert2*multi2

    print(word1 + "  #  " +word2,file=sys.stderr)
    if len(word1) > 1:
        werte[word1] = wert1
    if len(word2) > 1:
        werte[word2] = wert2    

for wert in sorted(werte):
    print(wert + " " + str(werte[wert]))
    total+=werte[wert]

if len(played)>6:
    print("Bonus 50")
    total+=50

print("Total " + str(total))