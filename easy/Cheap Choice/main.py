#https://www.codingame.com/ide/puzzle/cheap-choices

import sys,math

#1
itemList=[['JEANS', 'LARGE', '30'], ['SHIRT', 'SMALL', '15'], ['JACKET', 'LARGE', '20']]
orderList=[['JEANS', 'LARGE'], ['JACKET', 'LARGE']]

#4
itemList=[['COAT', 'LARGE', '40'], ['SHIRT', 'MEDIUM', '15'], ['SHOES', 'LARGE', '25'], ['PANTS', 'SMALL', '20']]
orderList=[['COAT', 'LARGE'], ['SHOES', 'LARGE'], ['SHIRT', 'MEDIUM'], ['SHIRT', 'MEDIUM'], ['PANTS', 'SMALL'], ['COAT', 'LARGE']]

#5
itemList=[['COAT', 'MEDIUM', '35'], ['SHIRT', 'SMALL', '20'], ['JEANS', 'LARGE', '30'], ['JACKET', 'MEDIUM', '45'], ['SHOES', 'LARGE', '25'], ['SHIRT', 'SMALL', '15'], ['COAT', 'MEDIUM', '25']]
orderList=[['COAT', 'MEDIUM'], ['SHOES', 'LARGE'], ['SHIRT', 'SMALL'], ['SHIRT', 'SMALL']]

itemDict={}
for item in itemList:
    key=item[0]+item[1]
    if key in itemDict:
        w=itemDict[key]
        w.append(item[2])
        itemDict[key]=sorted(w)
    else:
        itemDict[key]=[item[2]]

#print(itemDict,file=sys.stderr)

for order in orderList:
    key=order[0]+order[1]
    if key in itemDict:
        wL=itemDict[key]
        w=wL.pop(0)
        print(w)
        if len(wL) == 0:
            itemDict.pop(key)
    else:
        print("NONE")