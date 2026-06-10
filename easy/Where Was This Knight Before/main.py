# https://www.codingame.com/ide/puzzle/where-was-this-knight-before

import math,sys,string
#1
pieces="RNBQKP"
aList=['RNBQKBNR', 'PPPPPPPP', '........', '........', '........', '........', 'pppppppp', 'rnbqkbnr'];bList=['RNBQKBNR', 'PPPPPPPP', '........', '........', '........', '....p...', 'pppp.ppp', 'rnbqkbnr']
#2
pieces="RNBQKP"
aList=['R.BQKBNR', 'PPP.PPPP', '..N.....', '...P....', '....p...', '..n.....', 'pppp.ppp', 'r.bqkbnr'];bList=['R.BQKBNR', 'PPP.PPPP', '..N.....', '...n....', '....p...', '........', 'pppp.ppp', 'r.bqkbnr']


#6
#pieces="IJK"
#aList=['abcdefKh', 'ABDIDEFH', 'ZYXWVUTS', 'zyxsatoj', 'lmnarepo', 'LMNtenkt', 'opqopera', 'iPQrotal'];bList=['SaTORaKi', 'aReIObBY', 'TENetcDX', 'OpeRAdCj', 'RoTaSeDV', 'fEUzlLkO', 'gFTymMpP', 'hHSxnNqq']


###
abcList = string.ascii_uppercase;lowList=string.ascii_lowercase
koorList=['a','b','c','d','e','f','g','h']
abwList=[];aFiguren=[];bFiguren=[];figurenList=[];von="";nach="";verb="-"
for p in pieces:
    pos = abcList.find(p)
    figurenList.append(abcList[pos])
    figurenList.append(lowList[pos])
for y in range(8):
    for x in range(8):
        if not aList[y][x] == bList[y][x]:
            abwList.append([y,x])
            if aList[y][x] in figurenList:
                aFiguren.append([y,x])
            if bList[y][x] in figurenList:
                bFiguren.append([y,x])
if bFiguren[0] in aFiguren:
    aFiguren.remove(bFiguren[0]);verb="x"
von=koorList[aFiguren[0][1]]+str(8-aFiguren[0][0])
nach=koorList[bFiguren[0][1]]+str(8-bFiguren[0][0])
print(von+verb+nach)
diffy=abs(bFiguren[0][0]-aFiguren[0][0]);diffx=abs(bFiguren[0][1]-aFiguren[0][1])    
if (diffy == 2 and diffx == 1) or (diffy == 1 and diffx == 2):
    print("Knight")
else:
    print("Other")