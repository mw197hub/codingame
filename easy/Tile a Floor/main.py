#  https://www.codingame.com/ide/puzzle/tile-a-floor

import sys,math


n=3;rowList=['(  ', '  A', '  *']
n=4;rowList=['@   ', '   A', '   x', '    ']
n=4;rowList=['/   ', '   ^', '  /V', '    ']



rechtsDict={'/':'\\','\\':'/','(': ')', ')': '(', '{': '}', '}': '{', '[': ']', ']': '[', '<': '>', '>': '<'}
downDict={'/':'\\','\\':'/','^': 'v', 'v': '^', 'A': 'V', 'V': 'A', 'w': 'm', 'm': 'w', 'W': 'M', 'M': 'W', 'u': 'n', 'n': 'u'}
xy = 3 + n *4 -2 
mitte=xy//2
outList=[[" " for x in range(xy)]for y in range(xy)]
rahmenList=[0,mitte,xy-1]
#rahmen
for y in range(xy):
    for x in range(xy):
        xN = x -1 if x < mitte else x - mitte -1
        yN = y -1 if y < mitte else y - mitte -1
        if (y in rahmenList) and (x in rahmenList):
            outList[y][x] = "+"
        elif y in rahmenList:
            outList[y][x] = "-"
        elif x in rahmenList:
            outList[y][x] = "|"
        elif (y > 0 and y < n+1) or (y > 0+mitte and y < n+1+mitte):
            if (x > 0 and x < n +1) or (x> 0+mitte and x < n+1+mitte):                
                outList[y][x] = rowList[yN][xN]
            else:                
                xN = n - 2 - xN 
                zeichen = rowList[yN][xN]
                if rowList[yN][xN] in rechtsDict:
                    zeichen = rechtsDict[rowList[yN][xN]]
                outList[y][x] = zeichen
        else:           
            yN = n -2 - yN 
            if (x > 0 and x < n +1) or (x> 0+mitte and x < n+1+mitte):
                zeichen = rowList[yN][xN]
                if rowList[yN][xN] in downDict:
                    zeichen = downDict[rowList[yN][xN]]
                outList[y][x] = zeichen
            else:
                xN = n - 2 - xN         
                zeichen = rowList[yN][xN]
                if rowList[yN][xN] in downDict:
                    zeichen = downDict[rowList[yN][xN]]
                if zeichen in rechtsDict:
                    zeichen = rechtsDict[zeichen]
                outList[y][x] = zeichen

for y in outList:
    print("".join(y))