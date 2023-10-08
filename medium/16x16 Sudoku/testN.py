#board = [list(input()) for x in range(9)]
board=[['1', '2', '0', '0', '7', '0', '5', '6', '0'], ['5', '0', '7', '9', '3', '2', '0', '8', '0'], ['0', '0', '0', '0', '0', '1', '0', '0', '0'], ['0', '1', '0', '2', '4', '0', '0', '5', '0'], ['3', '0', '8', '0', '0', '0', '4', '0', '2'], ['0', '7', '0', '0', '8', '5', '0', '1', '0'], ['0', '0', '0', '7', '0', '0', '0', '0', '0'], ['0', '8', '0', '4', '2', '3', '7', '0', '1'], ['0', '3', '4', '0', '1', '0', '0', '2', '8']]



moves = []
#[  [[x,y],[TRIED NUMBERS]]  ]
prSet=set()
prSet.add('0');prSet.add('1');prSet.add('2');prSet.add('3');prSet.add('4');prSet.add('5');prSet.add('6');prSet.add('7');prSet.add('8');prSet.add('9')
print(prSet)

def ermitteleRest(eingabe):
    erg=set()
    

def findSolY(col):
    erg= set([board[y][col]for y in range(9)])^prSet
    return erg

def findSolX(row):
    erg= set(board[row])^prSet # nicht vorhanden
    return erg

def findSolBox(px,py):
    xStart = px//3*3
    yStart = py//3*3
    square = []
   
    square+=board[yStart][xStart:xStart+3]
    square+=board[yStart+1][xStart:xStart+3]
    square+=board[yStart+2][xStart:xStart+3]
    #print(square)
    return set(square)^prSet

def pointSol(x,y,tried):
    return list((findSolBox(x,y)&findSolX(y)&findSolY(x))-set(tried))

def getEmpty():
    for y in range(9):
        if "0" in board[y]:return [board[y].index("0"),y]
    return [-1,-1]

def printBoard():
    for i in range(9):print(*board[i],sep="")


def solve():
    done=False
    while not done:
        x,y=moves[-1][0]
        ps=sorted(pointSol(x,y,moves[-1][1]))
        
        if ps:
            moves[-1][1]+=[ps[0]]
            board[y][x]=ps[0]
            p=getEmpty()
            if p[0]==-1:done = True
            moves.append([p,[]])
            #print(x,y,ps)
            #printBoard()
            #print(" ")
        else:
            board[y][x]="0"
            moves.pop()
            #print(x,y,"BACKTRACK")
            #print(moves)
            #break


#printBoard()
moves.append([getEmpty(),[]])
solve()
printBoard()