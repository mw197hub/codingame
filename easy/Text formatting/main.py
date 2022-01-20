import sys
import math
import string


intext = "one,two,three."
intext = "one,two,three.four,five, six."
intext = "one , TWO  ,,  three  ..  four,fivE , six ."
intext = "when a father gives to his son,,, Both laugh; When a son gives to his father, , , Both cry...shakespeare"




satzAnfang = True
vorBuchstabe = ""
nachBuchstabe = ""
erg = ""
for i in range(len(intext)):
    b = intext[i]
    if i+1 < len(intext):
        nachBuchstabe = intext[i +1]
   # print(b,file=sys.stderr)
    if b == " ":
        if vorBuchstabe in [',','.',';']:
            erg += " "
        if vorBuchstabe.lower() in string.ascii_lowercase and nachBuchstabe.lower() in string.ascii_lowercase:
            erg += " "
    else:
        if vorBuchstabe in [',','.',';']:
            erg += " "
        if satzAnfang and b.lower() in string.ascii_lowercase:
            erg += b.upper()
            satzAnfang = False
        else:
            if b in [',','.',';'] and vorBuchstabe in [" ",",",".",';']:
                erg = erg
            else:
                erg += b.lower()
                if b in ['.',',',';'] and i+1 < len(intext) and not intext[i +1] == " ":
                    erg += " "                    
                    

    if erg[-2:] == ". ":
        satzAnfang = True
    vorBuchstabe = erg[-1:]

if erg[:-1] == " ":
    print(erg[:-1])
else:
    print(erg)