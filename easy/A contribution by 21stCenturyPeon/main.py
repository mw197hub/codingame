# https://www.codingame.com/ide/puzzle/fussy-fuzzy-matching

import sys,math,string,difflib


def trenne(eingabe):
    zahlen=[];buchstaben=[];rest=[]
    ziffer=False;zahl=0
    for e in eingabe:
        if e in string.ascii_letters:
            buchstaben.append(e)
            if ziffer:
                zahlen.append(zahl);ziffer=False
        elif e in "0123456789":
            if ziffer:
                zahl+=e
            else:
                ziffer=True
                zahl=e
        else:
            rest.append(e)
            if ziffer:
                zahlen.append(zahl);ziffer=False
    return zahlen,buchstaben,rest


#1
letter_case="true";letter_fuzz=0;number_fuzz=0;other_fuzz="true";template="Some1thing?"
candidateList=['some1thing?', 'Some1thing?', 'Some1thing!', 'Some thing?', 'Some2thing?', 'Some1thang?']
#2
letter_case="false";letter_fuzz=2;number_fuzz=0;other_fuzz="true";template="Correct Horse Battery Staple"
candidateList=['Dotteds Hoste Battery STAPLE', 'Corrupt Horse Batters Stable', 'Correct HORSE basterz urbond', 'Correct Battery Horse Staple']

#4
letter_case="true";letter_fuzz=0;number_fuzz=50;other_fuzz="true";template="The 82nd Airborne"
candidateList=['The 132nd Airborne', 'The 82nd Airborn', 'The 32nd Airborne', 'The 31nd Airborne', 'the 101nd Airborne', 'The 50nd Airborne']

#5
letter_case="true";letter_fuzz=5;number_fuzz=100;other_fuzz="false";template="Ab100-500,EfG?h1jK 50.1000n0p. Qr5; tU5-WxYz"
#candidateList=['Ab6-432,EfG?h75jK 144.911n0p. Qr35; tU56-WxYz', 'Ab0?576!EfG.h101jK{69}1066n100p+(Qr7)*tU102?WxYz', 'Ea0?576!BcD.m101kJ{79}1066o100q+(Uv7)*rV102?ZyXw', 'Ea8?444!BcD.m2kJ{88}988o80q+(Uv8)*rV98?ZyXw', 'Ab300-500,EfG?h1jK 50.1000n0p. Qr5; tU5-WxYz', 'Ab100-500,EfG?h1jK 50.1000n0p. qR5; tU5-WxYz', 'Ab100.500.EfG.h1jK.92..960n0p..Qr5.-tU5-WxYz']
candidateList=['Ea0?576!BcD.m101kJ{79}1066o100q+(Uv7)*rV102?ZyXw', 'Ea8?444!BcD.m2kJ{88}988o80q+(Uv8)*rV98?ZyXw', 'Ab300-500,EfG?h1jK 50.1000n0p. Qr5; tU5-WxYz', 'Ab100-500,EfG?h1jK 50.1000n0p. qR5; tU5-WxYz', 'Ab100.500.EfG.h1jK.92..960n0p..Qr5.-tU5-WxYz']





zahl1,buchstaben1,rest1=trenne(template)

for candidate in candidateList:
    print(candidate,file=sys.stderr)
    zahl2,buchstaben2,rest2=trenne(candidate)
    erg=True
    if len(zahl1) == len(zahl2):
        for i in range(len(zahl1)):
            if abs(int(zahl1[i]) - int(zahl2[i])) > number_fuzz:
                erg=False
    else:
        erg=False

    if len(rest1) == len(rest2):
        if other_fuzz == "true":
            for i in range(len(rest1)):
                if not rest1[i] == rest2[i]:
                    erg=False
    else:
        erg=False

    if len(buchstaben1) == len(buchstaben2):
        for i in range(len(buchstaben1)):
            if letter_case == "true":
                if buchstaben1[i] in string.ascii_lowercase and not buchstaben2[i] in string.ascii_lowercase:
                    erg=False
                if buchstaben1[i] in string.ascii_uppercase and not buchstaben2[i] in string.ascii_uppercase:
                    erg=False
            b1=buchstaben1[i].lower()
            b2=buchstaben2[i].lower()
            diff = (int(b1.encode('utf-8').hex(),16)) - (int(b2.encode('utf-8').hex(),16)) 
            if abs(diff) > letter_fuzz:
                erg=False
    else:
        erg=False

    if erg:
        print("true")
    else:
        print("false")
