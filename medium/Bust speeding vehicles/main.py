# https://www.codingame.com/ide/puzzle/bust-speeding-vehicles

import sys,math
import datetime
first_date = datetime.datetime(1970, 1, 1)
time_since = datetime.datetime.now() - first_date
seconds = int(time_since.total_seconds())


l=50;rList=['RSLJ97 134 1447409503', 'RSLJ97 185 1447413099', 'RSLJ97 201 1447420298']


auto=""
ausgabeList=[]
for i in range(len(rList)):
    rL = rList[i].split(" ")
    if auto == rL[0]:
        vL = rList[i-1].split(" ")
        diff=(int(rL[1])-int(vL[1]))/((int(rL[2])-int(vL[2]))/3600)
        if diff > l:
            ausgabeList.append([rL[0],rL[1]])

    else:
        auto = rL[0]


if len(ausgabeList) == 0:
    print("OK")
else:
    for ausgabe in ausgabeList:
        print(ausgabe[0] + " " + ausgabe[1])
