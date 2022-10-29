import sys,math



def random(seed):
    return ((214013*seed + 2531011) & 0xffffffff) >> 16
   # return int(((214013*seed + 2531011) % 2**32) / 65536)
   # return int((214013 * seed + 2531011) / 65536)

n='6 6 7 3 3 31'
nList = (list(map(int,n.split(" "))))
print(nList)

erg=nList[5]
yxList=[]
while nList[2] > len(yxList):
    erg = (random(erg))
    x = erg % nList[0]
    erg = (random(erg))
    y = erg % nList[1]
    if not [y,x] in yxList and (abs(nList[4] - y) > 1 or abs(nList[3] - x) > 1):
        yxList.append([y,x])
print(sorted(yxList))
mList=[]
for y in range(nList[1]):
    xList=[]
    for x in range(nList[0]):
        if [y,x] in yxList:
            xList.append("#")
        else:
            xList.append(".")
    mList.append(xList)
#print(mList,file=sys.stderr)
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

for yx in yxList:
    y,x=yx[0],yx[1]
    for um in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]:
        yN=y+um[0];xN=x+um[1]
        if 0<=yN<nList[1] and 0<=xN<nList[0]:
            if mList[yN][xN] == ".":
                mList[yN][xN] = 1
            elif mList[yN][xN] in [1,2,3,4,5,6,7,8,9]:
                mList[yN][xN] += 1
            

for y in range(nList[1]):
    erg=""
    for x in range(nList[0]):
        erg+= str(mList[y][x])
    print(erg)
