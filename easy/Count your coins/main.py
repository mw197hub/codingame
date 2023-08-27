#  https://www.codingame.com/ide/puzzle/count-your-coins

import sys,math

value_to_reach=8;valueDict={6: 5}
value_to_reach=154;valueDict={8: 66, 7: 76}


summe=0
anzahl=0;ende=False
for value,anz in sorted(valueDict.items()):
    for i in range(anz):
        summe+=value
        anzahl+=1
        print("{}:  {}".format(anzahl,summe),file=sys.stderr)
        if anzahl == 22:
            a=0
        if summe >= value_to_reach:
            ende=True;break
    if ende:
        break
if summe < value_to_reach:
    print("-1")
else:
    print(anzahl)