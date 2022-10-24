import sys
import math

ansList=[['23', 'female', 'hip-hop'], ['30', 'female', 'hip-hop']]
ergList=[['24', 'female']]

ansList=[['50', 'female', 'classical'], ['60', 'female', 'classical'], ['50', 'male', 'country'], ['52', 'female', 'classical'], ['53', 'male', 'country']]
ergList=[['55', 'female'], ['60', 'female'], ['55', 'male']]


fDict={};mDict={};ansDict={}
for ans in ansList:
    if ans[1] == 'female':
        if ans[2] in fDict:
            aList = fDict[ans[2]]
            aList.append(ans[0])
        else:
            fDict[ans[2]] = [ans[0]]
    else:
        if ans[2] in mDict:
            aList = mDict[ans[2]]
            aList.append(ans[0])
        else:
            mDict[ans[2]] = [ans[0]]

for mus,aList in fDict.items():
    if len(aList) == 1:
        ansDict[aList[0]+'female'] = mus
    else:
        bList = sorted(aList)
        for i in range(int(bList[0]),int(bList[-1])+1):
            ansDict[str(i)+'female'] = mus
for mus,aList in mDict.items():
    if len(aList) == 1:
        ansDict[aList[0]+'male'] = mus
    else:
        bList = sorted(aList)
        for i in range(int(bList[0]),int(bList[-1])+1):
            ansDict[str(i)+'male'] = mus

print(ansDict)
for erg in ergList:
    if erg[0]+erg[1] in ansDict:
        print(ansDict[erg[0]+erg[1]])
    else:
        print("None")