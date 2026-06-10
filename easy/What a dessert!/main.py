# https://www.codingame.com/ide/puzzle/what-a-dessert

import sys,math

e=6;f=550;s=700;b=200    #1
e=12;f=800;s=600;b=900   #2


rezeptDict={'Cookie':[1,100,150,50],'Cake':[3,180,100,100],'Muffin':[2,150,100,150]}

artList=[];teilList=[]
for art,zutatenList in rezeptDict.items():
    teilList.clear()
    teilList.append(e//zutatenList[0])
    teilList.append(f//zutatenList[1])
    teilList.append(s//zutatenList[2])
    teilList.append(b//zutatenList[3])
    artList.append(min(teilList))
print(artList)
ausgabe=""
if artList[1] >= artList[0] and artList[1] >= artList[2]:
    ausgabe=str(artList[1]) + " Cake"
elif artList[0] >= artList[2]:
    ausgabe=str(artList[0]) + " Cookie"
else:
    ausgabe=str(artList[2]) + " Muffin"    

print(ausgabe)