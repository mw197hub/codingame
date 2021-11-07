import sys
import math


ip = "2001:0000:3c4d:0015:0000:0000:0db8:1a2b"
ip = "2001:0000:0000:0000:0001:0000:1a2f:1a2b"
ip = "0000:aaaa:a000:0000:000a:0030:0000:0000"

erg = ""
ipList = ip.split(":")

for nr in range(len(ipList)):
    i = ipList[nr]
    while True:
        if i[0] == "0" and len(i) > 1:
            i = i[1:]
        else:
            break
    ipList[nr] = i
print(ipList,file=sys.stderr)

abPos = 99
laenge = 0
for i in range(len(ipList)):
    if ipList[i] == "0":
        j = i +1
        la = 1
        while True:
            if j >= len(ipList) or not ipList[j] == "0" :
                break
            la += 1
            j += 1
        if la > laenge:
            laenge = la
            abPos = i
if laenge > 1:
    for i in range(abPos,len(ipList)): 
        ipList[i] = ""
        if i+1 >= len(ipList) or not ipList[i+1] == "0":
            break

print(ipList,file=sys.stderr)
for i in ipList:
    erg = erg + i + ":"
erg = erg[:-1]
while True:
    erg = erg.replace(":::","::")
    if not ":::" in erg:
        break


#for i in ipList:
#    if len(erg) == 0:
#        erg = erg + i + ":"
#    else:
#        if erg[-2:] == "::" and i == "":
#            erg = erg
#        else:
#            erg = erg + i + ":"

print(erg)
