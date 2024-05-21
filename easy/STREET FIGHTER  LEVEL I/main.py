# https://www.codingame.com/training/easy/street-fighter-level-i

import sys,math

# Champ.|Life|Punch|Kick|Special Attack
# KEN   |25  |6    |5   |3*rage
# RYU   |25  |4    |5   |4*rage
# TANK  |50  |2    |2   |2*rage
# VLAD  |30  |3    |3   |2*(rage+opp.rage);opp.rage=0
# JADE  |20  |2    |7   |number of hits made*rage
# ANNA  |18  |9    |1   |damage received*rage
# JUN   |60  |2    |1   |rage; and rage is added to JUN's life

champ1="KEN";champ2="RYU";attackList=[['<', 'KICK'], ['<', 'PUNCH'], ['>', 'KICK'], ['<', 'PUNCH']]
champ1="VLAD";champ2="RYU";attackList=[['<', 'PUNCH'], ['<', 'PUNCH'], ['<', 'KICK'], ['<', 'KICK'], ['<', 'PUNCH'], ['>', 'PUNCH'], ['>', 'KICK'], ['>', 'SPECIAL'], ['>', 'PUNCH'], ['<', 'KICK'], ['>', 'KICK'], ['<', 'KICK'], ['<', 'SPECIAL'], ['>', 'SPECIAL']]
champ1="JUN";champ2="KEN";attackList=[['<', 'PUNCH'], ['<', 'PUNCH'], ['<', 'KICK'], ['<', 'KICK'], ['<', 'PUNCH'], ['>', 'PUNCH'], ['>', 'KICK'], ['>', 'SPECIAL'], ['>', 'PUNCH'], ['<', 'KICK'], ['>', 'KICK'], ['<', 'KICK'], ['<', 'SPECIAL'], ['>', 'SPECIAL'], ['>', 'PUNCH'], ['<', 'PUNCH'], ['<', 'KICK'], ['>', 'PUNCH'], ['<', 'KICK'], ['>', 'PUNCH'], ['<', 'KICK'], ['<', 'SPECIAL'], ['>', 'SPECIAL'], ['>', 'SPECIAL'], ['<', 'KICK'], ['>', 'PUNCH'], ['<', 'KICK'], ['>', 'KICK'], ['<', 'KICK'], ['>', 'SPECIAL']]



fighterDict={"KEN":[25,6,5,0,0],"RYU":[25,4,5,0,0],"TANK":[50,2,2,0,0],"VLAD":[30,3,3,0,0],"JADE":[20,2,7,0,0],"ANNA":[18,9,1,0,0],"JUN":[60,2,1,0,0]}
c1="";c2="";hits=0
for attack in attackList:
    if attack[0] == ">":
        c1=champ1;c2=champ2
    else:
        c1=champ2;c2=champ1
        
    if attack[1] == "SPECIAL":        
        if c1 == "KEN":            
            fighterDict[c2][0]-= fighterDict[c1][3]*3
        elif c1 == "RYU":
            fighterDict[c2][0]-= fighterDict[c1][3]*4
        elif c1 == "TANK":
            fighterDict[c2][0]-= fighterDict[c1][3]*2
        elif c1 == "VLAD":
            fighterDict[c2][0]-= (fighterDict[c2][3]+fighterDict[c1][3])*2
            fighterDict[c2][3] = 0    
        elif c1 == "JADE":
            fighterDict[c2][0]-= fighterDict[c1][3]*fighterDict[c1][4]
        elif c1 == "ANNA":
            fighterDict[c2][0]-= fighterDict[c1][3]*(18 - fighterDict[c1][0])
        elif c1 == "JUN":
            fighterDict[c2][0]-= fighterDict[c1][3]
            fighterDict[c1][0]+= fighterDict[c1][3]
        fighterDict[c1][3] = 0    
        fighterDict[c1][4]+=1    
        fighterDict[c2][3]+=1    
    else:
        fighterDict[c1][4]+=1
        fighterDict[c2][3]+=1
        if attack[1] == "KICK":
            fighterDict[c2][0]-= fighterDict[c1][2]
        else:
            fighterDict[c2][0]-= fighterDict[c1][1]
    if fighterDict[c2][0] <= 0:
        break

if fighterDict[champ1][0] > fighterDict[champ2][0]:
    c1=champ1;c2=champ2
else:
    c1=champ2;c2=champ1
hits = fighterDict[c1][4]

print(fighterDict,file=sys.stderr)


print("{} beats {} in {} hits".format(c1,c2,hits))