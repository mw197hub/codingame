import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
zfloor=-3;zpos=-1;zM=1
while True:
    inputs = input().split()
    floor = int(inputs[0])  
    pos = int(inputs[1])  
    direction = inputs[2]  
    print(direction,file=sys.stderr)
    if (pos == 1 and zM==-1) or (pos==width-1 and zM==1):
        print("BLOCK");zM = zM * -1
    else:
        print("WAIT")


    print(" floor: " + str(floor) + "  pos: " + str(pos),file=sys.stderr)
    print("zfloor: " + str(zfloor) + " zpos: " + str(zpos),file=sys.stderr)