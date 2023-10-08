import sys,math


size = 9
square_size = int(size**.5)
area = size**2


def pos(x, y):
    return y * size + x


def xy(pos):
    return (pos % size, pos//size)


#board = [int(x) for x in "".join([input() for _ in range(size)])]
board=[1, 2, 0, 0, 7, 0, 5, 6, 0, 5, 0, 7, 9, 3, 2, 0, 8, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 4, 0, 0, 5, 0, 3, 0, 8, 0, 0, 0, 4, 0, 2, 0, 7, 0, 0, 8, 5, 0, 1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 4, 2, 3, 7, 0, 1, 0, 3, 4, 0, 1, 0, 0, 2, 8]
#board=[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0, 7, 0, 0, 9, 0, 2, 0, 0, 0, 5, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 4, 5, 7, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 6, 8, 0, 0, 8, 5, 0, 0, 0, 1, 0, 0, 9, 0, 0, 0, 0, 4, 0, 0]

positions = [set() for x in range(area)]

for i in range(area):
    x, y = xy(i)
    for v in range(size):
        positions[i].add(pos(x, v))
        positions[i].add(pos(v, y))
    top_left = pos(square_size * (x//square_size),
                   square_size * (y//square_size))
    for p in [top_left + pos(dx, dy) for dx in range(square_size) for dy in range(square_size)]:
        positions[i].add(p)


def get_pos(board, pp):
    seen = {board[i] for i in pp}
    return [x for x in range(1, size+1) if x not in seen]


def solve(board, unknown):
    if len(unknown) == 0:
        return True
    p = unknown[0]
    for m in get_pos(board, positions[p]):
        board[p] = m
        if (solve(board, unknown[1:])):
            return True
    board[p] = 0
    return False


solve(board, [p for p, x in enumerate(board) if x == 0])
for y in range(size):
    print("".join([str(board[pos(x, y)]) for x in range(size)]))

