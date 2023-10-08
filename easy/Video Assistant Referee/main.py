# https://www.codingame.com/ide/puzzle/video-assistant-referee

import sys,math



pitchList=['###################################################', '#........................#........................#', '#.......................a#........................#', '#...............b.o......#........................#', '#######..................#..................#######', '#.....#......a...b.......b...........a......#.....#', '#.....#......b.......a..a#....b.............#.....#', '#..b..#........A.........#..................#.....#', '#.....#...........b....b.#..............a...#.....#', '#.....#....A.............#..................#.....#', '#######.......b..........#..................#######', '#.....................a..#.......b................#', '#........................#..........a.............#', '#........................#....b...................#', '###################################################']
pitchList=['###################################################', '#........................#........................#', '#.......................a#........................#', '#...............b.o......#........................#', '#######..................#..................#######', '#.....#......a...b.......b...........a......#.....#', '#.....#......b.......a..a#....b.............#.....#', '#..b..#........A.........#..................#.....#', '#.....#...........b....b.#..............a...#.....#', '#.....#....a.............#..................#.....#', '#######.......b..........#..................#######', '#.....................a..#.......b................#', '#........................#..........a.............#', '#........................#....b...................#', '###################################################']
pitchList=['###################################################', '#........................#........................#', '#.............a..........#........................#', '#..............a.........#........................#', '#######....b.............#..................#######', '#.....#..................#.........b........#.....#', 'b...a.ba.................#..................#.....#', '#....abba................#.....aB...........#.....#', '#.....bb.................#..................#.....#', '#....baa.................#........O.........#.....#', '#######.a................#..................#######', '#..a.....................#........................#', '#........................#........................#', '#........................#........................#', '###################################################']



anz=0
offside=False
ballX=0
ballY=0
teamA=True
passivA,passivB,aktivA,aktivB=[],[],[],[]
for i in range(len(pitchList)):
    pitch = pitchList[i]
    pos = pitch.find("o")
    if pos > -1:
        ballX = pos;teamA=True    
        ballY=i    
    pos = pitch.find("O")
    if pos > -1:
        ballX = pos;teamA=False
        ballY=i
    for k in range(len(pitch)):
        if pitch[k] == "a":
            passivA.append(k)
        if pitch[k] == "A":
            aktivA.append(k)
        if pitch[k] == "b":
            passivB.append(k)
        if pitch[k] == "B":
            aktivB.append(k)                                

if ballY==0 or ballY==14:
    anz=0;offside=False
else:
    if teamA:
        passivB = sorted(passivB)
        vorB = passivB[1]        
        for a in sorted(aktivA):
            if (a < vorB and a > ballX) and a < 25:
                anz+=1
        if anz > 0:
            offside = True
        for a in sorted(passivA):
            if (a < vorB and a > ballX) and a < 25:
                anz+=1
    else:
        passivA = sorted(passivA,reverse=True)
        vorA = passivA[1]
        for b in sorted(aktivB,reverse=True):
            if (b > vorA and b < ballX) and b > 25 :
                anz+=1
        if anz > 0:
            offside = True
        for b in sorted(passivB,reverse=True):
            if (b > vorA and b < ballX) and b > 25:
                anz+=1


if anz == 0:
    print("No player in an offside position.")
else:
    print("{} player(s) in an offside position.".format(anz))
if offside:
    print("VAR: OFFSIDE!")
else:
    print("VAR: ONSIDE!")