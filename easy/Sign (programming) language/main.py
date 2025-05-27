# https://www.codingame.com/ide/puzzle/sign-programming-language

import math,sys,re

def sucheEnde(porgramm,pos):
    for i in range(pos,len(programm)):
        if programm[i] == "/":
            return i


programm='/$+-^/'
programm='/$$$$//*/**/'
programm='$/$$$$///./$'
programm='/$$/$/*$//$$/'  #10
programm='$/*$/*$$/*/*//*$$/*$$' #12
#programm='/*$$/$$$$//*/**$//*$$/***/$/*/*/' #13

erg=0
pos=0
befehle=0
while(True):
    print(programm[pos:pos+2],file=sys.stderr)
    if programm[pos:pos+2] == '/$':
        pos+=2;befehle+=1
        ende = sucheEnde(programm,pos)
        erg+= ende - pos
        pos= ende +1
    if programm[pos:pos+2] =='//':
        pos+=2;befehle+=1
        ende = sucheEnde(programm,pos)
        erg-= ende - pos
        pos= ende + 1
    if programm[pos:pos+3] == '/**':
        pos+=3;befehle+=1
        ende =sucheEnde(programm,pos)
        erg = erg * (ende-pos +1 )
        pos= ende + 1
    if programm[pos:pos+3] == '/*/':
        pos+=3;befehle+=1
        ende = sucheEnde(programm,pos)
        erg = erg * ((ende - pos)*-1)
        pos = ende + 1
    if programm[pos:pos+3] == '/*$':
        pos+=3;befehle+=1
    if programm[pos:pos+1] == '$':
        pos+=1
        if befehle > 0 and pos == len(programm):
            erg = erg + befehle
            break
        else:
            befehle = 0
    if pos >= len(programm):
        break


print(erg)


PATTERN = re.compile(r"/\$([^/]*)/|//([^/]*)/|/\*\*([^/]*)/|/\*/([^/]*)/|(\$)|/\*\$")

program = programm
reg = 0
count = 0
counting = False

while program:
    match = PATTERN.match(program)
    assert match is not None

    if match[1] is not None:
        reg += len(match[1])
    elif match[2] is not None:
        reg -= len(match[2])
    elif match[3] is not None:
        reg *= len(match[3]) + 1
    elif match[4] is not None:
        reg *= -len(match[4])
    elif match[5] is not None:
        if counting:
            reg += count
            counting = False
        else:
            count = -1
            counting = True
    
    count += 1
    program = program[match.end():]

print(reg)