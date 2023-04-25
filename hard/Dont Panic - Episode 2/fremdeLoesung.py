def all_less_than(a, b):
    return all(ia <= ib for ia, ib in zip(a, b))

def is_valid_path(pair):
    return all_less_than(pair[0], limits)

def find_path(path_groups):
    new_groups = {}
    for floor in range(exit_y + 1):
        # Paths are grouped by their last position in the floor and their last direction
        for (pos, direction), paths in path_groups.items():
            current = positions.index(pos)
            # For each group, extend every path forwards then backwards
            for dir_, action in [(direction, []), (-direction, [((floor, pos), 'BLOCK')])]:
                for step in positions[current::dir_]:
                    detour = abs(exit_x - step) + abs(step - pos) - abs(exit_x - pos) + 3*len(action)
                    # Every path is indexed by its length in rounds, the number of blocked clones and elevators built
                    possibilities = {(nr+detour, nc+len(action), ne): p+action for (nr, nc, ne), p in paths.items()}
                    new_groups.setdefault((step, dir_), {}).update(possibilities)
                    # Stop at the first elevator that we did not block
                    if (floor, step) in elevators and (step, dir_) != (pos, -direction):
                        break

        # Make all paths climb one floor and keep only the valid and most promising ones
        for (pos, direction), paths in new_groups.items():
            up = [((floor, pos), 'ELEVATOR')] if (floor, pos) not in elevators else []
            cost = len(up)
            paths = [[(nr+3*cost, nc+cost, ne+cost), p+up] for (nr, nc, ne), p in paths.items() if not p or p[-1][0] != (floor, pos)]
            paths = sorted(filter(is_valid_path, paths))
            minimal_paths = {}
            for i, (costs, path) in enumerate(paths):
                shorter_paths = [all_less_than(c, costs) for c, _ in paths[:i]]
                if not any(shorter_paths):
                    minimal_paths[costs] = path
            new_groups[(pos, direction)] = minimal_paths
        path_groups, new_groups = new_groups, {}
        
    return path_groups.get((exit_x, 1)) or path_groups.get((exit_x, -1))

#10
input1="13 69 109 11 47 100 4 36"
input2=['1 62', '9 17', '6 23', '2 43', '2 9', '3 24', '8 63', '5 4', '6 9', '3 60', '1 24', '6 35', '7 48', '2 23', '4 23', '1 17', '8 1', '10 3', '2 3', '8 23', '1 36', '1 4', '2 24', '1 50', '4 9', '10 23', '3 17', '3 30', '9 2', '11 50', '10 45', '6 3', '11 45', '11 4', '8 9', '2 56']
input3="0 6 RIGHT"
#3
input1="6 13 100 5 10 10 5 0"
input2=[]
input3="0 1 RIGHT"
# 6
input1="10 19 47 9 9 41 0 17"
input2=['8 9', '1 4', '7 17', '4 3', '6 9', '2 9', '0 3', '4 9', '6 3', '1 17', '7 4', '0 9', '5 4', '3 4', '3 17', '2 3', '5 17']
input3="0 6 RIGHT"
# 1
#input1="2 13 100 1 11 10 1 0"
#input2=[]
#input3="0 2 RIGHT"



height, width, rounds, exit_y, exit_x, n_clones, n_additional_elevators, n_elevators = [int(i) for i in input1.split()]
# The exit is an elevator too ;)
elevators =  [(exit_y, exit_x)] + [tuple(map(int, input2[i].split())) for i in range(n_elevators)]

start_y, start_x, direction = input3.split()
start_y = int(start_y)
start_x = int(start_x)
start_pos = (start_x, 1 if direction == 'RIGHT' else -1)
minimum_rounds = exit_y + abs(start_x - exit_x)

# Only test columns with an elevator, the exit or the generator to reduce computing time
positions = sorted({elev[1] for elev in elevators} | {start_x})
limits = (rounds-1, n_clones-1, n_additional_elevators)

solution = find_path({start_pos: {(minimum_rounds, 0, 0): []}})
solution = dict(solution[min(solution)])

pos = (start_y, start_x)
while True:
    action = solution.pop(pos, 'WAIT')
    print(action)
    y, x, _ = input().split()
    pos = (int(y), int(x))
