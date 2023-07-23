# https://www.codingame.com/ide/puzzle/euclids-algorithm-with-complex-numbers

import sys,math
import cmath

def fmt(z):
    y = z.imag
    x = z.real
    if x == 0:
        print("{}j".format(int(y)),end="")
    else:
        if y > 0:
            print("({}+{}j)".format(int(x),int(y)),end="")
        elif y < 0:
            print("({}-{}j)".format(int(x),int(-y)),end="")
        else:
            print("({}+0j)".format(int(x)),end="")

def closest(n):
    c = math.ceil(n)
    f = math.floor(n)
    d = abs(n-c)
    if d <= 0.5:
        return c
    else:
        return f

def gcd(z1,z2):
    z = complex(z1 / z2)
    y = z.imag;x=z.real
    cx = closest(x)
    cy = closest(y)
    q = complex(cx,cy)
    r = complex(z1-z2 * q)

    fmt(z1);print(" = ",end="")
    fmt(z2);print(" * ",end="")
    fmt(q);print(" + ",end="")
    fmt(r);print("")

    if r.real == 0 and r.imag == 0:
        return z2
    return gcd(z2,r)


xa,ya,xb,yb=2,0,1,-1            #1
xa,ya,xb,yb=-38,-26,-43,-7      #2

z1 = complex(xa,ya)
z2 = complex(xb,yb)
gcdWert = gcd(z1,z2)
#print(type(gcdWert))
print("GCD(",end="")
fmt(z1)
print(",",end="")
fmt(z2)
print(") = ",end="")
fmt(gcdWert)
