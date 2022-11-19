#  https://www.codingame.com/ide/puzzle/nicholas-breakspeare-and-hugh-of-evesham

import sys,math
#from num2words import num2words
#print(num2words(525600, lang="en", to="ordinal"))

def cardinal(wert):
    e =""
    if wert[0] in einerDict:
        e = einerDict[wert[0]]
        e = e + " " + sonst['1'] + ' '
    if wert[1] in tyDict:
        e = e + tyDict[wert[1]] + " "
        if wert[2] in einerDict:
            e = e[:-1] +"-"+einerDict[wert[2]] + " "
    else:
        #print(wert[1:3])
        if wert[1:3] in zehnDict:
            e = e + zehnDict[wert[1:3]] + " "
        else:
            if wert[2] in einerDict:
                e = e +einerDict[wert[2]] + " "
    return e

sonst={'0':'zero','1':'hundred'}
einerDict={'1':'one','2':'two','3':"three",'4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
zehnDict={'10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'} 
tyDict={'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
potDict={'3':'thousand','6':'million','9':'billion','12':'trillion','15':'quadrillion','18':'quintillion'}

xList=['525600']
xList=['10', '1', '2', '3', '4']
xList=['10000000', '1000000000', '100000000000', '10000000000000', '1000000000000000', '100000000000000000', '10000000000000000000']



neg='negative '
for x in xList:
    if x == "0":
        print("zero")
    else:
        nega=False
        if x[0] == "-":
            nega=True
            x = x[1:]
        erg="";pos=0;tp=0
    # if x[0] == "-":
    #     erg=neg;pos=1
        while True:
            if len(x) < pos +3:
                break        
            teil = x[len(x)-pos-3:len(x)-pos]
         #   print(teil,file=sys.stderr)
            e = cardinal(teil)
            if str(pos) in potDict and len(e) > 0:
                erg = potDict[str(pos)] +" "+ erg
            erg = e + erg
            pos+=3;tp+=1
        if len(x) > pos:     
            rest = len(x) -pos
            teil = "0"+x[0:rest] if rest==2 else "00"+x[0:rest]
            e = cardinal(teil)
            if str(pos) in potDict:
                erg = potDict[str(pos)] +" "+ erg
            erg = e + erg
        if nega:
            print(neg +erg.strip())
        else:
            print(erg.strip())

