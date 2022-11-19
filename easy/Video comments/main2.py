#  https://www.codingame.com/ide/puzzle/video-comments

import sys,math

def swapPositions(list, pos1, pos2):     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def vergleich(aU,bU):
    a = aU.split("|");b=bU.split("|")
    if b[3].upper() == "PINNED" and not a[3].upper() == "PINNED":
        return True
    if a[3].upper() == "PINNED" and not b[3].upper() == "PINNED":
        return False
    if b[3].upper() == "FOLLOWED" and not a[3].upper() == "FOLLOWED":
        return True
    if a[3].upper() == "FOLLOWED" and not b[3].upper() == "FOLLOWED":
        return False
    if int(b[2]) > int(a[2]):
        return True
    if int(b[2]) < int(a[2]):
        return False
    if b[1] > a[1]:
        return True
    if b[1] > a[1]:
        return False
    
    if b[0].strip() > a[0].strip():  # validate 3
        return True
    return False

def sortList(outList,i):
    for j in range(i+1,len(outList)):
        if vergleich(outList[i],outList[j]):
            outList = swapPositions(outList,i,j)


cList=['user1|05:00|0|Followed', 'user2|06:00|0|none']
#cList=['user5|10:03|5|none', 'user9|09:12|0|Followed', 'user1|10:50|6|none', 'user3|10:50|6|none', 'user10|21:32|10|none']
#cList=['user5|11:00|10|Followed', 'user6|10:00|0|Pinned', 'user4|11:00|0|none']
#cList=['user1|20:00|1|none', '    user2|22:21|2|none', '    user3|21:22|3|none', 'user5|12:00|2|none', 'user2|09:00|0|Pinned']
#cList=['user5|10:03|5|none', 'user9|09:12|0|Followed', 'user1|10:50|6|none', 'user3|10:50|6|none', 'user10|21:32|10|none']


outDict={};key="";outList=[]
for c in cList:
    if c[0] == " ":
        wList = outDict[key]
        wList.append(c)
    else:
        key = c
        outDict[key] = [c]
        outList.append(c)
#print(outList,file=sys.stderr)

for i in range(len(outList)-1):    
    sortList(outList,i)
for out in outList:
    print(out)