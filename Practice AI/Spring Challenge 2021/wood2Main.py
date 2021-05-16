import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Cell:
    def __init__(self, cell_index, richness, neighbors):
        self.cell_index = cell_index
        self.richness = richness
        self.neighbors = neighbors

def sucheTree(treeList,suchWert):
    for key,wert in treeList.items():
        if wert == suchWert:
            return key
    return 999

cellList = {}
treeList = {}

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    print(str(index)+","+str(richness)+","+str(neigh_0)+","+str(neigh_1)+","+str(neigh_2)+","+str(neigh_3)+","+str(neigh_4)+","+str(neigh_5),file=sys.stderr)
    cellList[index] = Cell(index,richness,[neigh_0, neigh_1,neigh_2,neigh_3,neigh_4,neigh_5])


# game loop
while True:
    treeList = {}
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        if is_mine:
            treeList[cell_index] = size
    number_of_possible_moves = int(input())
    for i in range(number_of_possible_moves):
        possible_move = input()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(treeList,file=sys.stderr)
    print(possible_move + "   Tage: " + str(day) + " nutrients: " + str(nutrients),file=sys.stderr)

    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    restTage = 6 - day
    if restTage > 3:
        if sun >= 3:
            key = sucheTree(treeList,1)
            print("GROW " + str(key))
        else:
            print("WAIT")
    elif restTage > 1:
        if sun >= 7:
            key = sucheTree(treeList,2)
            print("GROW " + str(key))
        else:
            print("WAIT")
    else:
        key = sucheTree(treeList,3)
        if key < 100:
            print("COMPLETE " + str(key))
        else:
            print("WAIT")

