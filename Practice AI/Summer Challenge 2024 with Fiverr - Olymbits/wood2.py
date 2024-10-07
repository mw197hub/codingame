# https://www.codingame.com/ide/challenge/summer-challenge-2024-olymbits

import sys,math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())
print("player_idx={};nb_games={}".format(player_idx,nb_games),file=sys.stderr)

# game loop
while True:
    
    for i in range(3):
        score_info = input()
    for i in range(nb_games):
        inputs = input().split()
        gpu = inputs[0]
        reg_0 = int(inputs[1])
        reg_1 = int(inputs[2])
        reg_2 = int(inputs[3])
        reg_3 = int(inputs[4])
        reg_4 = int(inputs[5])
        reg_5 = int(inputs[6])
        reg_6 = int(inputs[7])
        print("gpu={};reg_0={};reg_1={};reg_2={}".format(gpu,reg_0,reg_1,reg_2),file=sys.stderr)
        pos = reg_0
        if player_idx == 1:
            pos=reg_1
        if player_idx == 2:
            pos=reg_2
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)    
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