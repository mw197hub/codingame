# https://www.codingame.com/ide/puzzle/create-turn-here-signs

import sys,math

_input = "right 3 9 8 6 2"
_input = "left 3 11 7 7 3"

iList=_input.split(" ")
zeichen="<" if iList[0] == "left" else ">"
zLaenge= (int(iList[1]) * (int(iList[3]) + int(iList[5]) * (int(iList[2]) //2) )) + ((int(iList[1]) -1) * int(iList[4])) 

pfeil=""
for i in range(int(iList[3])):
    pfeil+=zeichen
for y in range(int(iList[2])):
    vorspann=""
    if zeichen == ">":
        if y <= int(iList[2]) // 2 :
            vorspann = " " * int(iList[5]) * y
        else:
            vorspann = " " * int(iList[5]) * (int(iList[2]) - y -1)
    else:
        if y <= int(iList[2]) // 2 :
            vorspann = " " * int(iList[5]) * (int(iList[2]) // 2 - y )
        else:
            vorspann = " " * int(iList[5]) * (y - int(iList[2]) // 2 )

    #print((vorspann+pfeil + " " * int(iList[4])) * int(iList[1]))
    zeile = vorspann +(pfeil + " " * int(iList[4]))* int(iList[1])
    print(zeile.rstrip())