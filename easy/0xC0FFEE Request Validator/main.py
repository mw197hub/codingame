# https://www.codingame.com/ide/puzzle/0xc0ffee-request-validator

import sys,math

frame="DECAFBAD00744C23A5F"  #1
frame="3CFB4D1" #2
frame="DECAFBAD0516555D5FE21427D4304CBFE78C4F63F06466F5CB76223299AF915463EB6083896D9F6B7A3DA11" #7


fehler="403 Forbidden"

if len(frame) < 12:
    print(fehler)
    exit(0)
if not frame[0:8] == "DECAFBAD":
    print(fehler)
    exit(0)
anzahl=int(frame[8:11],16)
if not anzahl+8+3+1 == len(frame):
    print(fehler)
    exit(0)
checksum=0
for f in frame[:]:
    checksum+=int(f,16)
if not checksum//16 == checksum/16:
    print(fehler)
else:
    ausgabeList=[];anzahlDict={}
    for f in frame[11:-1]:
        if f in anzahlDict:
            anzahlDict[f]+=1
        else:
            ausgabeList.append(f)
            anzahlDict[f] = 1
    for a in ausgabeList:
        print(str(anzahlDict[a])+" "+a)