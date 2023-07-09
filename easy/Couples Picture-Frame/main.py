# https://www.codingame.com/ide/puzzle/couples-picture-frame

import sys,math

# 2
wife,husband="Kathleen","Ivan"
# 6 
wife,husband="Jill","Larry"


sumL=len(wife)*len(husband)
laenge,vW,vH=sumL,int(sumL/len(wife)),int(sumL/len(husband))
for i in range(2,len(wife)+len(husband)):
    if sumL%i == 0:
        teil = sumL/i
        if teil%len(wife) == 0 and teil%len(husband) == 0:
            laenge=int(teil)
            vW = int(teil/len(wife));vH=int(teil/len(husband))
            
wifeOut=wife*vW
husbandOut=husband*vH
for z in range(laenge+2):
    for s in range(laenge):
        if z == 0 or z == laenge+2-1:
            if z == 0:
                print(wifeOut[s],end="")
            else:
                print(husbandOut[s],end="")
        else:
            if s == 0 or s == laenge-1:
                if s == 0:
                    print(husbandOut[z-1],end="")
                else:
                    print(wifeOut[z-1],end="")
            else:
                print(" ",end="")
    print("")        


