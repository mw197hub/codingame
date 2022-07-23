import sys
import math
import string


w,h = 10,5
feldList = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', 'S', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', '#', '.', '#', '#', '#', '#', '#', '.', '#'], ['#', '#', '.', '#', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
#feldList = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', 'S', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', '#', '.', '#', '#', '#', '#', '#', '.', '#'], ['#', '#', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
feldList = [['#', '.', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '.', '#', '#', '.', '.', '#', '#', '#', '#'], ['.', '.', '#', '#', '.', '.', '#', '.', '.', '.'], ['#', '#', '#', '#', '.', '.', '#', 'S', '#', '#'], ['#', '.', '.', '.', '.', '#', '#', '#', '#', '#']]



zahlList = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

i = 10
for wert in string.ascii_uppercase:
    zahlList[i]=wert;i+=1
#print(zahlList)
moveList=[]
for i in range(h):
    for j in range(w):
        if feldList[i][j] == "S":
            moveList.append([i,j])
            feldList[i][j] = 0

nachbar=[[1,0],[-1,0],[0,1],[0,-1]]
suche = 0;treffer = True
while treffer:
    treffer = False
    for i in range(h):
        for j in range(w):
            if feldList[i][j] == suche:
                treffer = True
                for n in nachbar:
                    i1 = i + n[0]; j1 = j+n[1]
                    if i1 == h:
                        i1 = 0
                    if i1 < 0:
                        i1 = h-1
                    if j1 == w:
                        j1 = 0
                    if j1 < 0:
                        j1 = w-1
                    if feldList[i1][j1] == ".":                        
                        feldList[i1][j1] = suche + 1
    suche += 1


for i in range(h):
    for j in range(w):
        wert = feldList[i][j]
        if wert in zahlList:
            wert = zahlList[wert]
        print(wert,end="")
    print("")