#  https://www.codingame.com/ide/puzzle/an-adventure-in-the-fantasy-world

import sys,math

s='ULULRDDLRU'
mDict={'-2#-3': ['enemy', 'goblin'], '-1#0': ['money', '83G'], '2#-1': ['enemy', 'goblin'], '-2#2': ['enemy', 'slime'], '-1#1': ['money', '31G'], '-4#-2': ['enemy', 'slime'], '-3#0': ['enemy', 'goblin'], '-4#-1': ['money', '17G'], '1#-3': ['money', '60G'], '3#0': ['enemy', 'slime'], '1#-2': ['enemy', 'slime'], '3#-1': ['enemy', 'goblin'], '-1#-3': ['enemy', 'slime'], '3#3': ['enemy', 'goblin']}
s="DRLUUUULDRLRURLLLLLLDLDULRULDL"
mDict={'0#-9': ['enemy', 'slime'], '-10#9': ['money', '22G'], '6#3': ['enemy', 'goblin'], '2#-5': ['money', '83G'], '-4#-8': ['money', '97G'], '1#-7': ['money', '66G'], '-10#3': ['enemy', 'slime'], '4#1': ['enemy', 'goblin'], '-4#-7': ['money', '7G'], '9#6': ['money', '76G'], '6#6': ['enemy', 'slime'], '-7#-2': ['money', '97G'], '-9#10': ['money', '4G'], '-5#-5': ['enemy', 'goblin'], '-9#9': ['money', '92G'], '4#8': ['money', '6G'], '5#-5': ['money', '6G'], '8#3': ['money', '11G'], '-8#10': ['money', '69G'], '-4#1': ['money', '64G'], '-6#-1': ['enemy', 'slime'], '-3#-8': ['enemy', 'goblin'], '-9#3': ['enemy', 'goblin'], '-9#6': ['enemy', 'slime'], '2#6': ['money', '96G'], '8#-3': ['enemy', 'goblin'], '-9#5': ['money', '32G'], '7#6': ['money', '2G'], '-1#9': ['enemy', 'goblin'], '5#-6': ['money', '16G'], '1#-1': ['money', '44G']}



x,y,gold=0,0,50
rDict={'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
ende=False
for b in s:
    r = rDict[b]
    x += r[0];y+=r[1]
    pos = str(x)+"#"+str(y)
    if pos in mDict:
        pList = mDict[pos]
        if pList[0] == "money":
            gold+= int(pList[1][:-1])
            mDict.pop(pos)
        else:
            if pList[1] == "goblin" and gold >= 50:
                gold-=50
            else:
                print(str(x)+" "+str(y)+" "+str(gold)+"G"+" "+pList[1])
                ende=True
                break
if not ende:
    print("GameClear "+str(x)+" "+str(y)+" "+str(gold)+"G")