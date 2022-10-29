import sys
import math,copy

number,d=3141,3
number,d=72659,5
number,d=675379052,3
number,d=104890600,9

erg=number
if number % d == 0:
    print(erg)
else:
    treffer=False
    ergList = list(str(number))
    sList=[]
    for i in range(len(ergList)-1,-1,-1):
        nList = copy.deepcopy(ergList)
        nList.pop(i)
        erg = "".join(nList)
        if int(erg) % d == 0 and not erg[0] == '0':
            treffer=True
            sList.append(int(erg))
    if treffer:
        print(max(sList))
    else:
        sList=[]
        for i in range(len(ergList)-1,-1,-1):
            for j in range(i -1,-1,-1):
                nList = copy.deepcopy(ergList)
                nList.pop(i)
                nList.pop(j)
                erg = "".join(nList)
                if int(erg) % d == 0 and not erg[0] == '0':
                    treffer=True
                    sList.append(int(erg))
        if treffer:
            print(max(sList))
        else:
            print(0)