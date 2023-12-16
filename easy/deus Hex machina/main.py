# https://www.codingame.com/ide/puzzle/deus-hex-machina

import sys,math


def setFlip(number,vertiFlip):
    erg = ""
    for n in number:
        erg+=vertiFlip[n]
    #print(erg,file=sys.stderr)
    return erg
    #return number


number="15"
#number="666"
number="babe"
#number="555689abde1222"


horiFlip={}
vertiFlip={}

s="123456789abcdef0"
h="#9b#d6e8#a2##510"
v="153#2e#8a9#c#6#0"
for i in range(len(s)):
    horiFlip[s[i]] = h[15-i]
    vertiFlip[s[i]] = v[i]

#print(horiFlip,file=sys.stderr)
#print(vertiFlip,file=sys.stderr)

#vertical → horizontal → vertical → horizontal → vertical
#number=setFlip(number,vertiFlip)
#number=setFlip(number,horiFlip)
#number=setFlip(number,vertiFlip)
#number=setFlip(number,horiFlip)
#number=setFlip(number,vertiFlip)
print(number)


h = lambda d: "015##2a#8e6d#b9#"[int(d, 16)]
v = lambda d: "0153#2e#8a9#c#6#"[int(d, 16)]
flip_h = lambda n: ''.join(map(h, n))[::-1]
flip_v = lambda n: ''.join(map(v, n))


instructions = bin(int(number, 16))[2:]
apply_h, apply_v = (flip % 2 for flip in map(instructions.count, "01"))
nan = apply_h and '#' in flip_h(set(number)) or apply_v and '#' in flip_v(set(number))
if nan:
    print("Not a number")
else:
    if apply_h:
        number = flip_h(number)
    if apply_v:
        number = flip_v(number)
    print(number[:1000])

print((instructions))