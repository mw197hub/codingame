import sys
import math

class Point:
    x,y = 0,0
    def __init__(self,x,y) -> None:
        self.x = x; self.y = y
    def __repr__(self) -> str:
        return(str(self.x) + " " + str(self.y))

wallyList = [' O ', '/|\\', '/ \\']
pictureList = ['..........', '.......O..', '....../|\\.', '....../.\\.', '..........', '..........', '..........', '..........', '..........', '..........']

wallyList = [' O ', '/|\\', '/ \\']
pictureList = ['\\OO\\.OO.|\\', '..../||\\\\/', '\\./||//|/O', 'O\\|O.O\\\\|\\', '.OOOO|O.O|', 'O|\\||/|\\|\\', '\\/\\/O/.\\.O', 'O.\\|O/\\O\\.', './\\\\./||O/', '\\O|.|\\\\||\\']



wallyDict = {}
posX,posY = -1,-1
anzahl = 0
startPoint = Point(0,0)
startZeichen = ""
for y in range(len(wallyList)):
    zeile = wallyList[y]
    for x in range(len(zeile)):
        zeichen = zeile[x]
        if not zeichen == " ":
            
            if anzahl == 0:
                startPoint = Point(x,y)
                startZeichen = zeichen
            else:
                wallyDict[str(x - startPoint.x)+ " " + str(y - startPoint.y)] = zeichen
            anzahl += 1
print(wallyDict,file=sys.stderr)
#print(startPoint,file=sys.stderr)

for y in range(len(pictureList)):
    pic = pictureList[y]
    for x in range(len(pic)):
        zeichen = pic[x]
        if zeichen == startZeichen:
            treffer = True
            for key,item in wallyDict.items():
                x1,y1 = key.split(" ")
                if y + int(y1) >= len(pictureList) or x + int(x1) >= len(pic):
                    treffer = False
                else:
                    zeile = pictureList[y+int(y1)]
                    if not item == zeile[x+int(x1)]:
                        treffer = False
            if treffer:
                posX = x - startPoint.x
                posY = y
        

print(str(posX) + " " + str(posY))