import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def keyloesen(key):
    x,y = key.split("-")
    return int(x), int(y)

def umsetzen(von,zu):
    x1, y1 = keyloesen(von)
    x2, y2 = keyloesen(zu)
    if x1 > x2:
        return "LEFT"
    if x1 < x2:
        return "RIGHT"
    if y1 > y2:
        return "UP"
    if y1 < y2:
        return "DOWN"

def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
 
    if start == goal:
        return "That was easy! Start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)

    return "So sorry"
 
def aufbauTabelle(zeile, tabelle, y):
    controlP = "0-0"
  #  print(zeile + "   y:" + str(y),file=sys.stderr)
    i = 0
    while i < len(zeile):
        if zeile[i:i+1] == '.' or zeile[i:i+1] == 'T' or zeile[i:i+1] == 'C':
         #   print("feld: " + str(i) + '-' + str(y),file=sys.stderr)
            tabelle.append(str(i) + '-' + str(y))   
        if zeile[i:i+1] == 'C':
            controlP = str(i) + '-' + str(y) 
        i = i +1
    return controlP

def aufbauGraph(tabelle,graph, maxX):
    for tab in tabelle:
        neuTab = []
        x,y = tab.split("-")
        x = int(x)
        y = int(y)
        if x + 1 == maxX:
            s1 = str(0) + "-" + str(y)
        else:
            s1 = str(x+1) + "-" + str(y)
        if x -1 < 0:
            s2 = str(maxX-1) + "-" + str(y)
        else:
            s2 = str(x-1) + "-" + str(y)
        s3 = str(x) + "-" + str(y+1)
        s4 = str(x) + "-" + str(y-1)
        if s1 in tabelle:
            neuTab.append(s1)
        if s2 in tabelle:
            neuTab.append(s2)
        if s3 in tabelle:
            neuTab.append(s3)
        if s4 in tabelle:
            neuTab.append(s4)
        graph[tab] = neuTab

def pointModi(p,mX,mY):
    x,y = keyloesen(p)
    return str(x + mX) + "-" + str(y + mY)

def nSchritt(moveZahl):
    if moveZahl == 0:        
        return 0, -1
    if moveZahl == 1:
        return 1, 0
    if moveZahl == 2:
        return 0, 1
    if moveZahl == 3:
        return -1, 0

def sucheWeg(kirkP,tabelle,controlP, move, erkundet,unerkundet,rueckweg):
   # print(tabelle,file=sys.stderr)
    newKirkP = "0-0"
    if controlP != kirkP:
        moveZahl = 0
        moveList = [1,0,3,2]
        if move == "RIGHT":
            moveZahl = 1    
            moveList = [2,1,0,3]
        if move == "DOWN":
            moveZahl = 2
            moveList = [3,2,1,0]
        if move == "LEFT":
            moveZahl = 3
            moveList = [0,3,2,1]
        
      #  print(move + " zahl: " + str(moveZahl),file=sys.stderr)      
        zwZahl = 9
        newZahl = 9
        saveP = "0-0"
        while moveList:
            moveZahl = moveList.pop(0)
            x,y = nSchritt(moveZahl)
            newKirkP = pointModi(kirkP,x,y)
            if newKirkP in tabelle:
     #           print(newKirkP,file=sys.stderr)
                if zwZahl == 9:
                    zwZahl = moveZahl
                    saveP = newKirkP                    
          #      print(newKirkP,file=sys.stderr)
                if newKirkP not in erkundet and newKirkP not in unerkundet:
                    unerkundet.append(newKirkP)
                if newKirkP not in erkundet and newZahl == 9:                    
                    newZahl = moveZahl
                    saveP = newKirkP
            
        if newZahl < 9:
            moveZahl = newZahl
        else:
            moveZahl = zwZahl
            return " ", newKirkP,9
        newKirkP = saveP
        unerkundet.remove(newKirkP)
        #umsetzen(kirkP,newKirkP), newKirkP

        if moveZahl == 0:
            return "UP", newKirkP,0
        if moveZahl == 1:
            return "RIGHT", newKirkP,0
        if moveZahl == 2:
            return "DOWN", newKirkP,0
        if moveZahl == 3:
            return "LEFT", newKirkP,0

    else:
        return " ", newKirkP,9

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
maxY, maxX, time = [int(i) for i in input().split()]
maxXY = maxX
if maxY > maxX:
    maxXY = maxY

# game loop
controlP = "0-0"
startP = "0-0"
runde = 1
rueckweg = 0
tabelle = []
graph = {}
ergebnis = []
move = ""
rueckwegList = []
erkundet = []
unerkundet = []
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.    
    kirkY, kirkX = [int(i) for i in input().split()]
    kirkP = str(kirkX) + "-" + str(kirkY)
    erkundet.append(kirkP)


    if runde == 1:
        startP = str(kirkX) + "-" + str(kirkY)

    tabelle *= 0
    for i in range(maxY):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
       # print(row,file=sys.stderr)
        testP = aufbauTabelle(row,tabelle,i)        
        if testP != "0-0":
            controlP = testP
            #print(controlP + " - " + str(rueckweg),file=sys.stderr)
  ##  print(erkundet,file=sys.stderr)
    aufbauGraph(tabelle,graph, maxXY)
  
    for feld in unerkundet:        
        if feld in erkundet:   
            unerkundet.remove(feld)                                
            

    if controlP in unerkundet:
        unerkundet.remove(controlP)
      
    
    if controlP == kirkP and len(unerkundet) == 0:
        rueckweg = 1
    if controlP == kirkP and rueckweg == 10:
        rueckweg = 1
        print(str(rueckweg) + " " + controlP + " " + kirkP,file=sys.stderr)      
        

    if rueckweg == 1:       
      #  print(tabelle,file=sys.stderr)
        aufbauGraph(tabelle,graph, maxXY)
      #  print(graph,file=sys.stderr)
        ergebnis = bfs_shortest_path(graph, controlP, startP)        
      #  print(ergebnis,file=sys.stderr)
        rueckweg = 2
        vonP = controlP
        for zuP in ergebnis:
            rueckwegList.append(umsetzen(vonP,zuP))
            vonP = zuP
        rueckwegList.pop(0)
        print(rueckwegList,file=sys.stderr)
    if len(rueckwegList) == 0 and rueckweg == 10:        
        rueckweg = 0
    if rueckweg == 2 or rueckweg == 10:
        move = rueckwegList.pop(0)
    else:
   #     for next in unerkundet:
    #        if next in erkundet:
    #            unerkundet.remove(next)        
                
        move, newKirkP, rueckweg = sucheWeg(kirkP,tabelle,controlP,move,erkundet,unerkundet,rueckweg)
        if controlP == newKirkP and len(unerkundet) > 0:
            rueckweg = 9
        if rueckweg == 9:            
            # unerkundete Felder abarbeiten
            
            if len(unerkundet) > 0:
                if controlP in tabelle:
                    tabelle.remove(controlP)
                for j in range(len(unerkundet)):
                    newZielP = unerkundet[j]
                    print("neues Ziel: " + newZielP + " - " + str(j),file=sys.stderr)                    
                    aufbauGraph(tabelle,graph, maxXY)
                    ergebnis = bfs_shortest_path(graph, kirkP, newZielP)  
                    if ergebnis != "So sorry":
                        break
                    else:                        
                        erkundet.append(newZielP)
                        print("nicht erreichbar: " + newZielP,file=sys.stderr)

                if ergebnis == "So sorry":
                    newZielP = controlP
                    print("gehezu ControllPunkt: " + newZielP,file=sys.stderr)
                    aufbauGraph(tabelle,graph, maxXY)
                    ergebnis = bfs_shortest_path(graph, kirkP, newZielP) 

                print(ergebnis,file=sys.stderr)
                vonP = kirkP
                for zuP in ergebnis:
                    rueckwegList.append(umsetzen(vonP,zuP))
                    vonP = zuP
                rueckwegList.pop(0)
                rueckweg = 10
                move = rueckwegList.pop(0)
            else:
                newZielP = controlP
                print("gehezu ControllPunkt: " + newZielP,file=sys.stderr)
                aufbauGraph(tabelle,graph, maxXY)
                ergebnis = bfs_shortest_path(graph, kirkP, newZielP)
                print(ergebnis,file=sys.stderr)
                vonP = kirkP
                for zuP in ergebnis:
                    rueckwegList.append(umsetzen(vonP,zuP))
                    vonP = zuP
                rueckwegList.pop(0)
                rueckweg = 10
                move = rueckwegList.pop(0)
 ##   print(unerkundet,file=sys.stderr)    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Kirk's next move (UP DOWN LEFT or RIGHT).
    print(move)
    runde = runde + 1
