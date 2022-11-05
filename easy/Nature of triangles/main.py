# https://www.codingame.com/ide/puzzle/nature-of-triangles

import sys,math,copy

# hilfe: https://www.matheretter.de/wiki/dreieck-berechnen-abc

def distance(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def winkel(a,b,c):
    wertA = (a**2-b**2-c**2) / (-2 * b * c)
    return round(math.degrees(math.acos(wertA)),2)



abcList=[['A', '5', '-2', 'B', '8', '2', 'C', '-1', '-9'], ['O', '0', '0', 'A', '3', '0', 'B', '1', '2']]
#abcList=[['O', '0', '0', 'I', '1', '0', 'J', '0', '1'], ['H', '1', '2', 'O', '5', '-6', 'G', '-1', '0']]
abcList=[['D', '-4', '-3', 'O', '3', '-4', 'G', '8', '1']]
abcList=[['O', '0', '0', 'I', '1', '0', 'J', '0', '1'], ['H', '1', '2', 'O', '5', '-6', 'G', '-1', '0']]
abcList=[['A', '5', '4', 'B', '-6', '-1', 'C', '9', '-5']]



for abc in abcList:
    name=abc[0]+abc[3]+abc[6]
    ab = distance([int(abc[1]),int(abc[2])],[int(abc[4]),int(abc[5])])
    bc = distance([int(abc[4]),int(abc[5])],[int(abc[7]),int(abc[8])])
    ac = distance([int(abc[1]),int(abc[2])],[int(abc[7]),int(abc[8])])
    art = " is a scalene and "
    if ab == bc:
        art = " is an isosceles in " + abc[3] + " and "
    elif ab == ac:
        art = " is an isosceles in " + abc[0] + " and "
    elif bc == ac:
        art = " is an isosceles in " + abc[6] + " and "
    
    aWinkel = winkel(bc,ac,ab)
    bWinkel = winkel(ac,bc,ab)
    cWinkel = winkel(ab,ac,bc)
    
    trian = "an acute triangle."    
    if bc > ab and bc > ac:
        if aWinkel == 90:
            trian = "a right in "+abc[0]+" triangle."
        elif aWinkel > 90:
            trian = "an obtuse in "+abc[0]+ " ("+str(int(round(aWinkel,0)))+"°) triangle."
    elif ac > ab and ac > bc:
        if bWinkel == 90:
            trian = "a right in "+abc[3]+" triangle."
        elif bWinkel > 90:
            trian = "an obtuse in "+abc[3]+ " ("+str(int(round(bWinkel,0)))+"°) triangle."
    elif ab > ac and ab > bc:
        if cWinkel == 90:
            trian = "a right in "+abc[6]+" triangle."
        elif cWinkel > 90:
            trian = "an obtuse in "+abc[6]+ " ("+str(int(round(cWinkel,0)))+"°) triangle."


    print(name + art + trian)


#print(math.degrees(math.asin(3/6)))
