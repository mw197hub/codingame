import sys
import math

def pruefe(p,obj):
    if obj[0] == "SQUARE":
        if p[0] > int(obj[1]) and p[0] < int(obj[1]) + int(obj[3]):
            if p[1] > int(obj[2]) and p[1] < int(obj[2]) + int(obj[3]):
                return False,[int(obj[4]),int(obj[5]),int(obj[6])]
        if p[0] == int(obj[1]) or p[0] == int(obj[1]) + int(obj[3]):
            if p[1] >= int(obj[2]) and p[1] <= int(obj[2]) + int(obj[3]):
                return True,[]
        if p[1] == int(obj[2]) or p[1] == int(obj[2]) + int(obj[3]):
            if p[0] >= int(obj[1]) and p[0] <= int(obj[1]) + int(obj[3]):
                return True,[]
        return False,[]
    else:
        dist = math.sqrt( ((p[0]-int(obj[1]))**2)+((p[1]-int(obj[2]))**2) )
        if dist == int(obj[3]):
            return True,[]
        if dist < int(obj[3]):
            return False,[int(obj[4]),int(obj[5]),int(obj[6])]
    return False,[]


objList=[['SQUARE', '0', '5', '6', '255', '0', '0'], ['SQUARE', '4', '2', '3', '0', '255', '0'], ['CIRCLE', '4', '6', '3', '0', '0', '255']]
pList=[[0, 0], [4, 5], [2, 6], [5, 3], [5, 4], [3, 4]]

objList=[['CIRCLE', '60', '99', '42', '255', '0', '255'], ['SQUARE', '40', '9', '26', '255', '255', '0'], ['CIRCLE', '33', '2', '25', '255', '0', '255'], ['CIRCLE', '53', '88', '25', '255', '255', '0'], ['CIRCLE', '0', '27', '69', '255', '255', '0'], ['SQUARE', '15', '13', '58', '255', '0', '255'], ['SQUARE', '68', '25', '95', '0', '255', '255'], ['SQUARE', '21', '69', '55', '255', '0', '255'], ['CIRCLE', '13', '32', '86', '255', '255', '0'], ['SQUARE', '25', '77', '40', '0', '255', '255']]
pList=[[73, 17]]
#pList=[[34, 38], [21, 55], [92, 16], [77, 67], [90, 51], [8, 41], [73, 17], [93, 67], [83, 90], [66, 50], [42, 77], [31, 55], [33, 91], [88, 30], [12, 9], [41, 78], [77, 54], [19, 24], [40, 96], [51, 22]]


for p in pList:
    randB=False;newFarbe=[]
    for obj in objList:
        rand,farbe = pruefe(p,obj)
        if rand:
            randB=True
        if len(farbe) > 0:
            newFarbe.append(farbe)
    if randB:
        print("(0, 0, 0)")
    elif len(newFarbe) == 0:
        print("(255, 255, 255)")
    else:
        a,b,c=0,0,0
        for f in newFarbe:
            a+=f[0];b+=f[1];c+=f[2]
        a = int((a/len(newFarbe)+0.5))
        b = int((b/len(newFarbe)+0.5))
        c = int((c/len(newFarbe)+0.5))
        print("("+str(a)+", "+str(b)+", "+str(c)+")")