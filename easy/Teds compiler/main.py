#  https://www.codingame.com/ide/puzzle/teds-compiler

import sys,math

line='<><><><<<<>>>>>>><<<<>>>><><><>><<<<>>>><>>><><<<<>>>><><><>><<<><<<<>>>><><><>><<<><><><><><<<<>>>>' # 14
#line='<<>>>'
#line='><<>>'

erg=0;auf,zu=0,0
for i in range(len(line)):
    if line[i] == "<":
        auf+=1
    else:
        zu+=1
        if zu > auf:
            break        
    if auf >= zu:
        erg+=1

print(erg)
