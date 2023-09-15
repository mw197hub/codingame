import sys
import binascii,codecs
import string

s="37 21 37 27 16 29"
#s="6 10 16 10 84 35 84 42 11 38"
#s="-42 191 184 -15 184 -19 185 -19 186 -15 -42 190 92 93"

string.digits
abc= list(string.printable)
#abc = list(string.ascii_uppercase+string.ascii_lowercase)
print(abc)
#print(chr(int('72')),end="")
stList=s.split(" ")

for st in stList:
    wert = int(st)
    rest = wert%len(abc)
    print(abc[rest],end="")
    

