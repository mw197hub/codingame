import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
print("floors: " + str(nb_floors) + " weite: " +str(width) + " runden: " + str(nb_rounds),file=sys.stderr)
print("exitF: " + str(exit_floor) + " exitPos: " + str(exit_pos),file=sys.stderr)
listEle = {exit_floor: exit_pos}
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    listEle[elevator_floor] = elevator_pos

print(listEle,file=sys.stderr)

while True:
    inputs = input().split()
    clone_floor = int(inputs[0]) 
    clone_pos = int(inputs[1]) 
    direction = inputs[2]  
    print("floor: " + str(clone_floor) + " pos: " + str(clone_pos) + " direction: "  + str(direction),file=sys.stderr)
    if clone_floor in listEle:
        print(listEle,file=sys.stderr)
        akt_pos = listEle.pop(clone_floor)
        print("akt: " + str(akt_pos) + " clone_pos: " + str(clone_pos) + " richtung: " + direction,file=sys.stderr)
        if (clone_pos < akt_pos and direction == "LEFT") or (clone_pos > akt_pos and direction == "RIGHT"):
            print("BLOCK")
        else:
            print("WAIT")
    else:
        print("WAIT")
