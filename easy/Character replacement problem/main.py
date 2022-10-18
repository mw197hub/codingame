import sys
import math

sList=['ox', 'xx', 'pq']
n=3
m='oweuaxoqp'

sList=['zz', 'ia','zi', 'ao']
n=4
m='zzzziiiiaaaazzzz'

sList=['zz', 'zi', 'ia', 'az']
n=4
m='zzzziiiiaaaazzzz'

error=False
sDict={}
for s in sList:
    if s[0] == s[1]:
        a=0
    elif s[0] in sDict:
        error=True
    else:        
        if s[1] in sDict:
            sDict[s[0]] = sDict[s[1]]            
        else:
            sDict[s[0]] = s[1]
            for a,b in sDict.items():
                if s[0] == b:
                    sDict[a] = s[1]

for a,b in sDict.items():
    if a == b:
        error = True

if error:
    print("ERROR")
else:
    for a,b in sDict.items():    
        m = m.replace(a,b)
    for i in range(0,len(m),n):
        print(m[i:i+n])