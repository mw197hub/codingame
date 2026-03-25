# https://www.codingame.com/ide/puzzle/cgfunge-interpreter

import sys,math,string

lineList=['2419+*+IE']
#lineList=['"txet elpmiS"CCCCCCCCCCCE']
lineList=['39DD1+*+DI  >11091+   v>v', ' v  " on the wall"    < D ', '>>     "reeb fo"      v S', '0v<" bottles "        < C', 'X>DSC_SvPD      _25*+Cv |', '       *v   IS        < P', '^IDX-1 <>  SC        0v X', 'v   "pass it around"  < 1', '>    " ,nwod eno ekat" ^-', ' Sing it!   ^+55D-1X_ESD<']

###
ende=False;befehl=True
pos=[0,0];move=[0,1]
stack=[]
while True:
    wert=lineList[pos[0]][pos[1]]
    #print("{}    {}".format(pos,wert),file=sys.stderr)
    if wert == "E":
        break
    elif wert == "I":
        wert1 = stack.pop()
        if wert1 == "10":
            print("")
        else:
            print(wert1,end="")
    elif befehl and wert == "C":
        wert1 = stack.pop()
        if wert1 == "10":
            print("")
        else:
            print(wert1,end="")
    elif befehl and wert == "S":
        pos[0]+=move[0];pos[1]+=move[1]
    elif wert == ">":
        move=[0,1]
    elif wert == "<":
        move=[0,-1]
    elif wert == "^":
        move=[-1,0]
    elif wert == "v":
        move=[1,0]
    elif wert in ["+","-","*"]:
        wert2=int(stack.pop())
        wert1=int(stack.pop())
        erg=wert1*wert2
        if wert == "+":
            erg=wert1+wert2
        if wert == "-":
            erg=wert1-wert2
        stack.append(str(erg))
    elif befehl and wert == " ":
        a=0
    elif wert == "\"":
        befehl = not befehl
       # stack.append(wert)
    elif befehl and wert == "P":
        stack.pop()
    elif befehl and wert == "X":
        wert1 = stack.pop()
        wert2 = stack.pop()
        stack.append(wert1);stack.append(wert2)
    elif befehl and wert == "D":
        wert1 = stack.pop()    
        stack.append(wert1);stack.append(wert1)
    elif wert == "_":
        wert1 = stack.pop()
        if wert1 == "0":
            move=[0,1]
        else:
            move=[0,-1]
    elif wert == "|":
        wert1 = stack.pop()
        if wert1 == "0":
            move=[1,0]
        else:
            move=[-1,0]
    else:
        if wert in string.digits:
            stack.append(wert)
        if not befehl:
            stack.append(wert)
    pos[0]+=move[0];pos[1]+=move[1]

        