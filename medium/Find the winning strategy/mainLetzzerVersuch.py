import sys,math,string

def ungerade(wert):
    if wert %2:
        return 0 #ungerade
    return 1 #gerade



##############################
#1
rows=2;columns=6
gameList=[[1, 5], [0, 5]]
gameList=[[1, 4], [1, 5]]
#gameList=[[1, 3], [2, 5]]
#2 
#rows=1;columns=30
#gameList=[[0, 29]]
#3
#rows=5;columns=11
#gameList=[[4, 6], [3, 7], [2, 8], [1, 9], [0, 10]]


###############################

while True:
    col=-1;row=-1;schritt=1;maxAbstand=-1;anzahlCol=0
    piles=[];geradeList=[]
    for i in range(len(gameList)):
        columen = gameList[i]
        wert=columen[1] - columen[0] -1
        piles.append(wert)
        geradeList.append(ungerade(wert))
        if wert > maxAbstand:
            maxAbstand=wert
        if wert > 0:
            anzahlCol+=1
    print("{}  {}  max={}  anzahlCol={}".format(piles,geradeList,maxAbstand,anzahlCol),file=sys.stderr)
    ####
    if anzahlCol == 1:
        for i in range(len(gameList)):
            columen = gameList[i]
            if columen[1] - columen[0] -1 > 0:
                col=i;row=columen[1] -1
    else:
        move = 0;zeilenWert=-1
        colGerade=ungerade(anzahlCol);sumGerade=ungerade(sum(piles))
        if colGerade == 1:  #gerade Anzahl
            zeilenWert=1
            if sumGerade == 1:
                move = 2
            else:
                move = 1
        else:
            zeilenWert=0
            if sumGerade == 1:
                move = 1
            else:
                move = 2
        for i in range(len(gameList)):
            game=gameList[i]
            #if zeilenWert == geradeList[i]:
            if maxAbstand == piles[i]:
                col = i;row = game[0] + move


    ####
    print("{} {}".format(col,row))
    
    


#########
    break
print((7 ) % 2)