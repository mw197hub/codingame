import sys
import math

s = '27'
s = '0800795705000904561000705000000905000'  # 400005555567778999 1000000000000000000
#s = '0000000000100000000000'
#s = '10000000000000000000'
s = '79380248390522737902'                  # 20 200223334577788999
#s = '00000'
#s = '9'
#s = '9407809450087866606'
s = '99'
s = '00'

a = ""
b = ""
fehler = False
max = 1000000000000000000
zList,nullList = [], []
for w in s:
    z = w
    if z == '0':
        nullList.append(z)
    else:
        zList.append(z)
zList.sort()
print(zList,file=sys.stderr)

if '1' in zList and len(nullList) >= 18:
    b = '1000000000000000000'
    zList.remove('1')
    for _ in range(18):
        nullList.remove('0')
else:
    laenge = len(zList)-1
    if len(zList) + len(nullList) == 19 and len(nullList) > 0:
        laenge = len(zList)
        
    for _ in range(laenge):
        b = str(zList.pop()) + b
        if len(b) == 18:
            break
    if len(b) == 0 and len(nullList) > 0:
        b = nullList.pop(0)
    else:
        for _ in range(len(nullList)):
            if len(b) == 18 or len(nullList) == 1:
                break
            b = b[0] + "0" + b[1:]
            nullList.pop()


for w in zList:
    a = a + w
    if len(a) == 1:
        for _ in range(len(nullList)):
            a = a + nullList.pop()
if len(nullList) == 1:
    a = nullList.pop()
print(a,file=sys.stderr)
print(len(b),file=sys.stderr)
print(b,file=sys.stderr)

aOut = ''.join(map(str,a))
bOut = ''.join(map(str,b))
if len(a) < 1 or len(b) < 1 or int(a) < 0 or int(a) > int(b) or len(nullList) > 0:
    fehler = True

if fehler:
    print("-1 -1")
else:
    print(aOut + " " + bOut)