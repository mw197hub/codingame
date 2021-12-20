import sys
import math



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
message = "IFMMPAXPSME"
word = "WORLD"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
message = "NQVTMO_S"
word = "WHAT"



erg = ""
for mul in range(1,len(alphabet)):
    for shift in range(1,len(alphabet)):
        for m in message:
            pos = (((alphabet.index(m) + shift) * mul)% len(alphabet))
            erg += (alphabet[pos])
        if word in erg:
            print(erg)
            break
        erg = ""
    if word in erg:
        break
        
