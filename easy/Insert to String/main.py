#  https://www.codingame.com/ide/puzzle/insert-to-string

import sys,math,copy


start="Hello world"
rawList=['0|11|!', '0|5|,\\n', '0|7| w', '0|10|\\n']

start='main\\nHello World}'
rawList=['0|0|void ', '1|0|  Console.WriteLine("', '0|4|()\\n{', '1|11|");\\n']

sList=[];tList=[];zW=False
for i in range(len(start)):
    if zW:
        zW = False
    else:
        if start[i:i+2] == "\\n":
            zW=True
            sList.append(copy.deepcopy(tList))
            tList.clear()
        else:
            tList.append(start[i])
sList.append(tList)
print(sList,file=sys.stderr)

restDict={};erg=""
for raw in rawList:
    rList = raw.split("|")
    if int(rList[0]) in restDict:
        uDict = restDict[int(rList[0])]
        uDict[int(rList[1])] = rList[2]
        restDict[int(rList[0])] = uDict
    else:
        uDict={}
        uDict[int(rList[1])] = rList[2]
        restDict[int(rList[0])] = uDict

print(restDict,file=sys.stderr)

for z in sorted(restDict):
    if z > len(sList):
        sList.append([])
    uDict = restDict[z]    
    for u in sorted(uDict,reverse=True):
        wert = uDict[u]
        sList[z].insert(u,wert)
print(sList,file=sys.stderr)

for tList in sList:
    erg=""
    for t in tList:
        if "\\n" in t:
            weiter=False
            for i in range(len(t)):
                if weiter:
                    weiter=False
                else:                     
                    if t[i:i+2] == "\\n":
                        print(erg);erg=""
                        weiter = True
                    else:
                        erg+=t[i]
        else:
            erg+=t
    
    print(erg)

#print("void main()\n{\nHello World}")
        
