import sys,math,string,copy,time

steps=3
rowList=[['Y', 'D', 'O', 'S'], ['C', 'E', 'A', 'E']]

steps=5000
rowList=[['M', 'O', 'E', 'T', 'Y', 'S', 'E', 'E', 'U', 'R', 'B', 'K', 'N', 'E', 'A', 'O', 'E', 'T'], ['O', 'N', 'T', 'E', 'S', 'F', 'D', 'W', 'E', 'W', 'I', 'R', 'A', 'I', 'O', 'O', 'N', 'G'], ['R', 'I', 'R', 'W', 'I', 'I', 'S', 'R', 'S', 'O', 'L', 'I', 'O', 'R', 'N', 'E', 'E', 'E'], ['E', 'N', 'S', 'H', 'S', 'O', 'I', 'R', 'M', 'R', 'P', 'T', 'O', 'P', 'D', 'E', 'D', 'E'], ['R', 'M', 'H', 'H', 'E', 'D', 'K', 'L', 'U', 'O', 'T', 'D', 'D', 'N', 'G', 'H', 'O', 'W'], ['T', 'E', 'I', 'U', 'E', 'U', 'H', 'O', 'O', 'I', 'N', 'S', 'T', 'R', 'H', 'P', 'H', 'C'], ['M', 'P', 'L', 'W', 'L', 'E', 'D', 'T', 'S', 'K', 'T', 'A', 'O', 'N', 'R', 'R', 'T', 'O'], ['I', 'Y', 'N', 'K', 'L', 'R', 'B', 'A', 'S', 'I', 'E', 'D', 'R', 'D', 'E', 'T', 'D', 'N'], ['K', 'M', 'N', 'E', 'N', 'M', 'E', 'R', 'N', 'H', 'E', 'S', 'A', 'H', 'L', 'R', 'F', 'E'], ['O', 'E', 'H', 'A', 'L', 'N', 'R', 'D', 'N', 'S', 'L', 'G', 'O', 'S', 'I', 'O', 'D', 'D'], ['R', 'W', 'N', 'T', 'C', 'I', 'T', 'E', 'E', 'N', 'E', 'O', 'B', 'E', 'H', 'B', 'C', 'D'], ['V', 'D', 'A', 'N', 'A', 'T', 'T', 'E', 'M', 'S', 'N', 'A', 'E', 'V', 'E', 'O', 'R', 'G'], ['G', 'T', 'E', 'A', 'A', 'E', 'A', 'U', 'D', 'I', 'H', 'M', 'H', 'P', 'T', 'S', 'R', 'N'], ['A', 'E', 'P', 'E', 'N', 'T', 'H', 'T', 'E', 'E', 'D', 'R', 'E', 'O', 'R', 'E', 'D', 'S'], ['N', 'A', 'W', 'O', 'R', 'G', 'O', 'E', 'B', 'G', 'E', 'I', 'A', 'D', 'E', 'A', 'E', 'L'], ['D', 'N', 'T', 'N', 'N', 'R', 'W', 'E', 'E', 'N', 'S', 'R', 'E', 'D', 'G', 'I', 'A', 'N']]


start=time.time()
abcDict={};tausch=[]
for i in range(65,65+len(string.ascii_uppercase)):
    abcDict[string.ascii_uppercase[i-65]] = i

for _ in range(steps):
    sumDict={}
    for i in range(len(rowList[0])):
        summe = 0
        tausch.clear()
        for j in range(len(rowList)):
            summe+=abcDict[rowList[j][i]]
            tausch.append(rowList[j][i])
        anz = len(rowList) - (summe % len(rowList))
     #   print(anz,file=sys.stderr,end=", ")
        if not anz == len(rowList):
     #       tausch=copy.deepcopy(rowList)
            for z in range(len(rowList)):
                pos = z - anz
                if pos < 0:
                    pos = pos + len(rowList)
                rowList[pos][i] = tausch[z]
     
                
   # print("  ##  ",file=sys.stderr,end=" ")
    for i in range(len(rowList)):
        summe=0
        tausch.clear()
        for j in range(len(rowList[0])):
            summe+=abcDict[rowList[i][j]]
            tausch.append(rowList[i][j])
        anz = len(rowList[0]) -(summe % len(rowList[0]))
    #   print(anz,file=sys.stderr,end=", ")
        if not anz == len(rowList[0]):
    #        tausch=copy.deepcopy(rowList)
            for z in range(len(rowList[0])):
                pos = z - anz
                if pos < 0:
                    pos = pos + len(rowList[0])
                rowList[i][pos] = tausch[z]
    
  #  print("",file=sys.stderr)
  #  print(rowList,file=sys.stderr)


for row in rowList:
    r=""
    for i in range(len(row)):
        r+=row[i]
    print(r)

print(time.time()-start,file=sys.stderr)



