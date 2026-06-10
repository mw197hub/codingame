# https://www.codingame.com/ide/puzzle/minicpu-instruction-decoder

import sys,math

def hexToint(wert):
    return int(wert,16)
def pruefen(wert):
    if wert > 255:
        return wert % 256
    if wert < 0:
        return 256 + wert
    return wert

#1
codeList=['01', '00', '0A', '01', '01', '05', '02', '00', '01', '03', '00', '01', 'FF']
#4
codeList=['01', '00', 'FF', '05', '00', 'FF']
#7
codeList=['01', '00', '05', '01', '01', '0A', '03', '00', '01', 'FF']

inp ="01 00 14 01 01 08 01 02 03 01 03 E0 02 03 00 03 02 00 04 03 01 FF"
codeList = inp.split(" ")



regList=[0,0,0,0]
pos=0
while pos < len(codeList):
    if codeList[pos] == "01":
        regList[int(codeList[pos+1])] = hexToint(codeList[pos+2])
        pos+=3
    elif codeList[pos] == "02":
        regList[int(codeList[pos+1])] += regList[int(codeList[pos+2])]
        regList[int(codeList[pos+1])] = pruefen(regList[int(codeList[pos+1])])
        pos+=3
    elif codeList[pos] == "03":
        regList[int(codeList[pos+1])] -= regList[int(codeList[pos+2])]
        regList[int(codeList[pos+1])] = pruefen(regList[int(codeList[pos+1])])
        pos+=3
    elif codeList[pos] == "04":
        regList[int(codeList[pos+1])] *= regList[int(codeList[pos+2])]
        regList[int(codeList[pos+1])] = pruefen(regList[int(codeList[pos+1])])
        pos+=3
    elif codeList[pos] == "05":
        regList[int(codeList[pos+1])] += 1
        regList[int(codeList[pos+1])] = pruefen(regList[int(codeList[pos+1])])
        pos+=2
    elif codeList[pos] == "06":
        regList[int(codeList[pos+1])] -= 1
        regList[int(codeList[pos+1])] = pruefen(regList[int(codeList[pos+1])])
        pos+=2
    elif codeList[pos] == "FF":
        pos+=1
    
for r in regList:
    print(str(r))
