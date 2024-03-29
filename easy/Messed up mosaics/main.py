#  https://www.codingame.com/ide/puzzle/messed-up-mosaics

import sys,math,copy

def sucheX(row,pattern,startPos):
    #print(row[startPos:startPos+len(pattern)])
    for k in range(startPos,startPos+len(pattern)):
        if not row[k] == pattern[k-startPos]:
            return k
    return -1


pattern='{-_-}-_-'
rowList=['{-_-}-_-{-_-}-_-{-_-}-_-{-_-}-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '_-}-_-{-_-}-_-{-_-}-_-{-_-}-_-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '{-_-}-_-{-_-}-_-{-_-}-_-{-_-}-', '-{-_-}-_-{-_-}-_-{-_-}-_-{-_-}', '_-{-_-}-_-{-_-}-_-{-_-}-_-{-_-', '-{-_-}-_-{-_-}-_-{-_-}-_-{-_-}', '{-_-}-_-{-_-}-_-{-_-}-_-{-_-}-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '_-}-_-{-_-}-_-{-_-}-_-{-_-}-_-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '{-_-}-_-{-_-}-_-{-_-}-_-{-_-}-', '-{-_-}-_-{-_-}-_-{-_-}-_-{-_-}', '_-{-_-}-_-{-_-}-_-{-_-}-_-{-_-', '-{-_-}-_-{-_-}-_-{-_-}-_-{-_-}', '{-_-}-_-{-_-}-_-}-_-}-_-{-_-}-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '_-}-_-{-_-}-_-{-_-}-_-{-_-}-_-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '{-_-}-_-{-_-}-_-{-_-}-_-{-_-}-', '-{-_-}-_-{-_-}-_-{-_-}-_-{-_-}', '_-{-_-}-_-{-_-}-_-{-_-}-_-{-_-', '-{-_-}-_-{-_-}-_-{-_-}-_-{-_-}', '{-_-}-_-{-_-}-_-{-_-}-_-{-_-}-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '_-}-_-{-_-}-_-{-_-}-_-{-_-}-_-', '-_-}-_-{-_-}-_-{-_-}-_-{-_-}-_', '{-_-}-_-{-_-}-_-{-_-}-_-{-_-}-', '-{-_-}-_-{-_-}-_-{-_-}-_-{-_-}']
#pattern='_~#~'
#rowList=['_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#', '_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~', '##~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_', '#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~', '~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#~_~#']
pattern="ABBACD"
rowList=['BACDABXACDAB','ABBACDABBACD']

ende=False
x,y=1,0
for i in range(len(rowList)):
    row = rowList[i]
    startPos=0
    while True:
        if row[startPos:len(pattern)+startPos] == pattern:
            break
        startPos+=1
        if startPos > len(pattern):
            y=i
            startPos=0;laenge=len(pattern)-1
            while True:
                if row[:laenge] == pattern[len(pattern)-laenge:]:
                    break
                laenge-=1
            startPos =laenge
            x = sucheX(row,pattern,startPos)
            ende=True
            break

   # print(str(i)+":   "+str(startPos))
    
    if not row[0:startPos] == pattern[len(pattern)-startPos:]:
        y=i
        x = sucheX(row,pattern,0)
        ende=True
    else:
        for j in range(startPos,len(row),len(pattern)):
        #  print(row[j:len(pattern)+j])
            if  len(pattern)+j > len(row):
        #     print(pattern[:len(row)-j])
                if not row[j:] == pattern[:len(row)-j]:
                    y=i
                    x = sucheX(row,pattern,j)
                    ende=True
                    break
            else:
                if not row[j:len(pattern)+j] == pattern:
                    y=i
                    x = sucheX(row,pattern,j)
                    ende=True
                    break
    if ende:
        break


print("("+str(x)+","+str(y)+")")