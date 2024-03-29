# https://www.codingame.com/ide/puzzle/you-are-the-father-maury-povich-style

import sys,math


def getGen(person):
    ergL=[]
    tPerson=person[person.find(":")+1:]
    sList=tPerson.split(" ")
    #print(sList,file=sys.stderr)
    for s in sList:
        if len(s) == 2:
            ergL.append(s)
    return ergL

def mischen(gen1,gen2):
    ergL=[]
    ergL.append(gen1[0]+gen2[0])
    ergL.append(gen1[1]+gen2[0])
    ergL.append(gen1[0]+gen2[1])
    ergL.append(gen1[1]+gen2[1])
    ergL.append(gen2[0]+gen1[0])
    ergL.append(gen2[1]+gen1[0])
    ergL.append(gen2[0]+gen1[1])
    ergL.append(gen2[1]+gen1[1])
    return ergL

mother,child="Mother Julie:        Uj $7","Child Brandon:       Wj =$"
fatherList=['Garrett:             #; wc', 'Macallister:         P2 zv', 'Jeffrey:             KI J&', 'Scott:               WW :=', 'Angus:               Xm N1']

mother,child="Mother Fiona:        ;L KR O* \"X </ 5, JC hG *2 nh 2? y/ p& J. QX rQ ?k ,E vP /M lj :2 ?g ws #y nd Xe 97 YY SU E: pb t% i& I0 0m","Child Delia:         #L RR Oy -\" /% 51 C? bh 2p -h ?R y; Ip *J XQ rN kA E$ P) MG jD 32 <g ,s #C nK XO 7/ MY UY EO >b %S &) e0 Pm"
fatherList=['Theodore:            t# kR Ey )- %! F1 s? b0 kp -l $R E; ?I ,* Xw Nv jA $Z t) Gh D! o3 <M d, CC Kf Oj /6 fM Yj On a> FS E) O5 8u', 'Michael:             T# !R Wy -z %F c1 v? b4 p$ -O Rs ,; I; *; Xl 2N A= $6 )N Gz !D 3q 4< ,T C? kK y# Qy J( )- =H +9 F8 ij Bv )i', 'Jordan:              a# R< yU "- <% ;1 D? bR &p I- jR 6; Ir 5* kX TN AD o$ )2 G. sD s3 >< ," C* KZ OV /q GM Yi .O L> (S b) eO 9U', "David:               #o R> y' !- #% >1 o? b; pP (- 1R ;8 OI *P zQ Np WA ,$ <) hG LD 3/ <8 h, CN BK %O /P LM SY OI !> CS 3A aH O(", "Jonathan:            #y 'R vy =- %b 91 ?? 8b f9 NI uj C; Zd *, !m Hk 2S IP I7 +0 8r vS Vy 6o Ne /( v? !: s& K) rH A# Ru T- 93 9h", 'Ronald:              z# RP y< (- d% "& Tp JF ;5 b< $g md 6y Va IP ex z& qz Pk :4 cY x: :M 4s (# n, r( Mj i( 1s c1 "= sV BF #N :2', 'Zion:                #\' bR yh -0 %o !1 7? &b p$ *- R0 ;Z XI *" &X NA UA $l )T =G D1 F3 <J ,M C* kK sO !/ 1M KY O# >4 S, Z) 9e PY', "James:               #8 Rk yC 4< +l zR +f )j GD x* Zw R- FN Uz Y% k) J' u4 nw 3$ 5/ 4' A. rl iz d* vr uO #s t, <x y3 1! /r pN lR"]



motherL=getGen(mother)
childL=getGen(child)


name=""
for father in fatherList:
    fName = father[:father.find(":")]
    fatherL=getGen(father)
    treffer=True
    for i in range(len(fatherL)):
        mischL=mischen(fatherL[i],motherL[i])
        if not childL[i] in mischL:
            treffer=False;break
    if treffer:
        name=fName;break


print("{}, you are the father!".format(name))