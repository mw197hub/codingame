import sys
import math
import string
import copy

def distance(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

inList = ['fg9', 'ls11', 'oe7']
inList = ['ft17', 'PLANTft9', 'nf17', 'PLANTnf9', 'PLANTjm5']
inList = ['jm13', 'PLANTjm14']

def kreisZiehen(x,y,r,art,feldList):
    h = int((r-1)/2)
    b = r/2
    for i in range(y-h,y+h+1,1):
        for j in range(x-h,x+h+1,1):   
            diff = abs(y-i)+abs(x-j)
            diff = distance([y,x],[i,j])
            #print(str(diff) + " = "+ str(i)+"-"+str(j) + " zu " + str(y) + "-" + str(x))
            if diff <=b:          
                if i < 0 or j < 0 or i > 24 or j > 18:
                    held = 0
                else:
                    if art == 0:
                        feldList[i][j] = "  "
                    if art == 1:
                        feldList[i][j] = "{}"
                    if art == 2:
                        if feldList[i][j] == "  ":
                            feldList[i][j] = "{}"
                        else:
                            feldList[i][j] = "  "
   # feldList[y][x] = "S"
abcList= {}
i = 0
for z in string.ascii_lowercase:
    abcList[z] = i;i+=1
#print(abcList,file=sys.stderr)
feldList=[]
for i in range(25):
    fList = []
    for j in range(19):
        fList.append('{}')
        #fList.append('0')
    feldList.append(copy.deepcopy(fList))

for inL in inList:
    if len(inL) > 9:
        kreisZiehen(abcList[inL[8]],abcList[inL[9]],int(inL[10:]),2,feldList)
    elif len(inL) > 5:
        kreisZiehen(abcList[inL[5]],abcList[inL[6]],int(inL[7:]),1,feldList)
    else:
        kreisZiehen(abcList[inL[0]],abcList[inL[1]],int(inL[2:]),0,feldList)


for feld in feldList:
    for f in feld:
        print(f,end="")
    print("")


