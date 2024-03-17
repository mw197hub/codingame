# https://www.codingame.com/ide/puzzle/periodic-table-spelling

import sys,math,copy

elements="H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og"

#elements="C Ar Ca B O N Rb"

eList=elements.split(" ")
ergList=[]

word="Pauses"
#word="carbon"

fList=[]
pos=0
erg2=[]
for e in eList:
    if word[pos:len(e)].upper() == e.upper():
        ergList.append(e) 
for i in range(len(word)-1):
    erg2.clear()
    for erg in ergList:
        pos=len(erg)
        for e in eList:
          #  print("{}    {}".format(word[pos:len(e)+pos].upper(),e.upper()),file=sys.stderr)
            if word[pos:len(e)+pos].upper() == e.upper():
                if word.upper() == (erg+e).upper():
                    fList.append(erg+e)
                else:
                    erg2.append(erg+e) 
                

    ergList = copy.deepcopy(erg2)
if len(fList) == 0:
    print("none")
else:
    for e in sorted(fList):
        print(e)