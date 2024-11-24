# https://www.codingame.com/ide/challenge/summer-challenge-2024-olymbits

import sys,math

def bewegung0(pL,gpu,idx,playerDict,move):
    stun=0
    if move == "RIGHT":
        if pL[0] +3 >= len(gpu):
            stun=0
        elif gpu[pL[0]+1] == '#' or gpu[pL[0]+2] == '#' or gpu[pL[0]+3] == "#":
            stun=-1
    if move == "DOWN":
        if pL[0] +2 >= len(gpu):
            stun=0
        elif gpu[pL[0]+1] == '#' or gpu[pL[0]+2] == '#':
            stun=-1
    if move == "LEFT":
        if pL[0] +1 >= len(gpu):
            stun=0
        elif gpu[pL[0]+1] == '#':
            stun=-1
    if move == 'UP':
        if pL[0] +2 >= len(gpu):
            stun=stun
        elif gpu[pL[0]+1] == '#':
            stun=1
        elif gpu[pL[0]+2] == '#':
            stun=-1        
    return stun

def bewegung1(pL,gpu,idx,playerDict,move):
    return 0

def bewegung2(pL,gpu,idx,playerDict,move):
    pos = -1
    for i in range(len(gpu)):
        if move[0] == gpu[i]:
            pos = i
    if pL[1] >= 3 and pos > 1:
        return -1
    if pL[1] < 0:
        return 0
    if pL[1] == 0 and pos == 3:
        return 1
    if pos == 1:
        if pL[1] >= 3:
            return 1        
        return 2
    if pos == 0 and pL[1] >= 3:
        return 1
    return 0

def bewegung3(pL,gpu,idx,playerDict,move):
    if gpu[0] == move[0]:
        return 2
    return -2

def game(idx,gpuDict,playerDict,games,scoreDict,move,pruefGameList):
    bewertung=0
    right=3;down=2;left=1;up=2 # springen
    stunList=[]
    playerList=playerDict[idx]
    gpuList=gpuDict[idx]

    gameWert=0;gameWert1=0
    for i in range(games):
        pL = playerList[i]
        gpu = gpuDict[i]
        if pL[1] == 0 and not gpu == 'GAME_OVER' and i in pruefGameList:
            if i == 0:
                gameWert1 += bewegung0(pL,gpu,idx,playerDict,move)
        if not gpu == 'GAME_OVER' and i in pruefGameList:
            if i == 1:
                gameWert1 += bewegung1(pL,gpu,idx,playerDict,move)
            if i == 2:
                gameWert += bewegung2(pL,gpu,idx,playerDict,move)
            if i == 3:
                gameWert1 += bewegung3(pL,gpu,idx,playerDict,move)
        #print("{} # {}".format(move,gameWert),file=sys.stderr)
          
        
    return gameWert

def bevorGame(scoreList,playerList):
    nuller=[]
    punkteList=[]
    game=0
    for i in range(1,13,3):
        punkte=int(scoreList[i])*3
        punkte+=int(scoreList[i+1])
        if punkte == 0 and playerList[game][1] == 0:
            nuller.append(game)
        punkteList.append(punkte)
        game+=1
    if len(nuller) == 1:
        return nuller[0]
    durchschnitt = sum(punkteList) / 4
    for i in range(4):
        if punkteList[i] < durchschnitt -5:
            return i
    return -1

def nachrangGame(playerDict,idx):
    nachragList=[]
    myList=playerDict[idx]
    for p,playList in playerDict.items():
        if not p == idx:
            for i in range(len(playList)):
                if playList[i][0] - myList[i][0] + (playList[i][1]-myList[i][1]*3) >= 6:
                    if not i in nachragList:
                        nachragList.append(i)  

    return nachragList

def suche(idx,gpuDict,playerDict,games,scoreDict):
    right=3;down=2;left=1;up=2 # springen
    move=['RIGHT','UP','LEFT','DOWN']

    bewertungList=[];pruefGameList=[0,1,2,3]
    bevorzugtesGame=bevorGame(scoreDict[idx],playerDict[idx])
    nachrangigesList=nachrangGame(playerDict,idx)
   # if bevorzugtesGame >= 0:
   #     pruefGameList.clear()
   #     pruefGameList.append(bevorzugtesGame)
   # elif len(nachrangigesList) > 0:
   #     for nach in nachrangigesList:
   #         pruefGameList.remove(nach)
    
    for m in move:
        bewertung = game(idx,gpuDict,playerDict,games,scoreDict,m,pruefGameList)
        bewertungList.append(bewertung)
    
    #print("{}   {}   {}   {}".format(gpuDict[0][playerDict[0][0][0]:playerDict[0][0][0]+4],gpuDict[1][playerDict[0][1][0]:playerDict[0][1][0]+4],gpuDict[2][playerDict[0][2][0]:playerDict[0][2][0]+4],gpuDict[3][playerDict[0][3][0]:playerDict[0][3][0]+4]),file=sys.stderr)
    #print(stunList,file=sys.stderr)
    wert=0;mov="UP"
    for i in range(4):
        if bewertungList[i] > wert:
            mov = move[i];wert=bewertungList[i]
    return mov

##############################################
##############################################

player_idx=0;nb_games=4


scoreDict={0: ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 1: ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 2: ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']}
gpuDict={0: '.......#...#...#....#....#....', 1: '253822123631', 2: 'DLRU', 3: 'RRULUURDDUDDLR'}
playerDict={0: [[2, 0], [8, -3], [2, 3], [1, 1]], 1: [[2, 0], [-3, 8], [2, 3], [1, 1]], 2: [[2, 0], [8, -3], [2, 3], [1, 1]]}
runde=1


# game loop
while True:
    
   # for i in range(3):
   #     score_info = input()
    for i in range(nb_games):
        a=0
    
    move = suche(player_idx,gpuDict,playerDict,nb_games,scoreDict)
    print(move)
    break

    '''
    if pos < len(gpu) -2 and (gpu[pos +1] == "#" or gpu[pos +2] == "#"):
        print("UP")
    else:
        if pos < len(gpu) -3 and gpu[pos +1] == "." and gpu[pos +2] == "." and gpu[pos +3] == ".":
            print("RIGHT")
        else:
            if pos < len(gpu) -2:
                print("DOWN")
            else:
                print("LEFT")
    '''