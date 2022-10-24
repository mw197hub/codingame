import sys
import math

def escape_count(n, c: complex) -> int:
    z = 0
    for iteration in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return iteration
    return n

m=275
c='0.465+0.354i'

cN=[]
if "+" in c:
    cN = c[:-1].split("+")
else:
    pos = c[1:-1].find("-")
    cN.append(c[0:pos+1])
    cN.append(c[pos+1:-1])
print(cN,file=sys.stderr)
cNew =complex(float(cN[0]),float(cN[1]))
erg = (escape_count(m,cNew))
if erg == m:
    print(m)
else:
    print(erg+1)