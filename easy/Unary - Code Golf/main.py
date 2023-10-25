# https://www.codingame.com/ide/puzzle/chuck-norris-codesize

import sys,math

def toBinary(a):
  l,m=[],[];e=""
  for i in a:
    l.append(ord(i))
  for i in l:
    #m.append(int(bin(i)[2:]))
    z=str(int(bin(i)[2:]))    
    z="0000000"[:len(z)*-1]+z
    e+=z
  print(e)
  return e

message="%"

wert=toBinary(message)
alt,erg="",""
for w in wert[:]:
    if w == alt:
       erg+="0"
    else:
        erg += " 0 0" if w == "1" else " 00 0"
        alt=w
print(erg[1:])
    

#print(toBinary(message))
#bi = bytes(message,'UTF-8')
#print(bi)
#print(bin(int('55', base=8))[2:])
#print(int(str(ord("%")),16))
#print(bin(int(str(int(str(ord("%")),16)), base=8))[2:])

#w1="".join(list(str(int(bin(ord(x))[2:])) for x in message))
w1=list(str(int(bin(ord(x))[2:])).zfill(7) for x in message)
#w1="".join("0000000"[:len(x)*-1]+x for x in w1)
print((w1))

#w1=("".join(str(int(bin(ord(x))[2:]))) for x in message)
#w2="0000000"[:len(w1)*-1]+w1
#print(w2)

w=list(str(int(bin(ord(x))[2:])) for x in message)

e,a="",""
for t in "".join(x.zfill(7)for x in w): 
 if t!=a:
  e+=[' 00 ',' 0 '][int(t)];a=t
 e+="0"
print(e[1:])

'''
te1=format(14,(bin(int(str(int(str(ord("%")),16)), base=8))[2:]))
print(type(te1))
#print(te1)
print(format(14, '08b'))
te1=(bin(int(str(int(str(ord("%")),16)), base=8))[2:]).zfill(7)
print(te1)
'''