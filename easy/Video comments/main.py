#  https://www.codingame.com/ide/puzzle/video-comments

import sys,math


def setKey(c,nr):
    iList = c.split("|")
    key = "A" if iList[3] == "none" else iList[3][0].upper()
    likes = "0000"[:-len(str(iList[2]))] + str(iList[2])
  #  pos=0
  #  for i in range(len(iList[0])):
  #      m = 1+i
  #      if iList[0][-m] in ['0','1','2','3','4','5','6','7','8','9']:
  #          pos+=1
  #      else:
  #          break
  #  pos = len(iList[0]) -pos
  #  anz = 10000 - int(iList[0][pos:])
  #  user = "00000"[:-(len(str(iList[0]))-pos)] + str(anz)
  #  user = "0000"[:-(len(str(nr)))] + str(nr)
    user = str(9999-nr)
    key += "#" + likes + "#" + iList[1] + "#" + user
    return key

cList=['user1|05:00|0|none', 'user2|06:00|-1|none']
#cList=['user5|10:03|5|none', 'user9|09:12|0|Followed', 'user1|10:50|6|none', 'user3|10:50|6|none', 'user10|21:32|10|none']
#cList=['user5|11:00|10|Followed', 'user6|10:00|0|Pinned', 'user4|11:00|0|none']
#cList=['user1|20:00|1|none', '    user2|22:21|2|none', '    user3|21:22|3|none', 'user5|12:00|2|none', 'user2|09:00|0|Pinned']
cList=['user5|00:03|1|Followed', 'user9|09:12|0|Followed', 'user1|10:50|6|none', 'user3|10:50|6|none', 'user10|21:32|10|none']



cDict={};key=""
for i in range(len(cList)):
    c = cList[i]
    if c[0] == " ":
        wList = cDict[key]
        wList.append(c)
    else:
        key = setKey(c,i)
        cDict[key] = [c]

for key in (sorted(cDict,reverse=True)):
    print(cDict[key][0])
    uList=cDict[key][1:]
    if len(uList) > 0:
        #print(uList,file=sys.stderr)
        dDict={};key=""
        for i in range(len(uList)):
            c = uList[i]
            key = setKey(c,i)
            dDict[key] = c
        for key in (sorted(dDict,reverse=True)):
            print(dDict[key])