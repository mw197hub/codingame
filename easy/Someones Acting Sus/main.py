import sys
import math

f='ABCDEF'
cList=['ABC', 'AFE', 'CDC', 'DBC', 'AAA']

f='QWERTYUIOP'
cList=['Q#E#TR', 'Q##I#U', 'Q##Y#O', 'I#II#P', 'Q####Y', 'W##Y#O', 'O##TRE', '######']

f='WEUHFNALP'
cList=['####WW#L', 'F##P####', '#######A', 'A###EW#L', '#W#####N', 'PE#####W', 'N##E####', 'L##L###U']

f='YHKLURWFBAXSENCJIGMOQ'
cList=['##AA##S#S#####XA#XS##EN#S###JJI#IJ#J#NCNC#I##J#CJC']
cList=['###QY##K###YH#Y#Y##HK####K#LKHH##HK##KH#H#KHY##OQY']
cList=['Y##OQ']


print(len(f),file=sys.stderr)
for c in cList:
    anz=0
    if c[0] == "#":
        anz+=1
    pos1=f.find(c[0])
    sus=False
    for i in range(1,len(c)):
        pos2=f.find(c[i])
        if c[i] == "#":
            anz+=1
        else:
            pos = abs(pos1-pos2)
            if pos1 > -1 and pos > 1+anz and not pos >= len(f)-1 -anz:
                sus=True
                break
            anz=0
            pos1=pos2
    if sus:
        print("SUS")
    else:
        print("NOT SUS")