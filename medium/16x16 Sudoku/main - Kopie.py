import sys,math

N = 5
N_2 = N * N
base = ord('A')
vide = '.'

solution = [[' ' for _ in range(N_2)] for _ in range(N_2)]

class dlx_t:
    pass

class Node:
    def __init__(self):
        self.data = dlx_t()
        self.left = None
        self.right = None
        self.up = None
        self.down = None

pool_size = 1 + 4 * N_2 * N_2 + 4 * N_2 * N_2 * N_2
pool = [Node() for _ in range(pool_size)]
root_ = pool[0]
headers_ = pool[1]
nodes_ = pool[1 + 4 * N_2 * N_2]

def InitRoot(root):
    root.left = root.right = None

def InitNode(header, last, node):
    hidx = header - root_
    lidx = last - root_
    idx = node - root_

    node.data.head = hidx
    node.down = hidx
    node.up = header.up
    pool[header.up].down = idx
    header.up = idx

    if last is None:
        node.left = node.right = idx
    else:
        node.left = lidx
        node.right = last.right
        pool[last.right].left = idx
        last.right = idx

    header.data.size += 1

def cover(header):
    pool[header.left].right = header.right
    pool[header.right].left = header.left

    iter = pool[header.down]
    while iter != header:
        iter2 = pool[iter.right]
        while iter2 != iter:
            pool[iter2.up].down = iter2.down
            pool[iter2.down].up = iter2.up
            pool[iter2.data.head].data.size -= 1
            iter2 = pool[iter2.right]
        iter = pool[iter.down]

def uncover(header):
    iter = pool[header.up]
    while iter != header:
        iter2 = pool[iter.left]
        while iter2 != iter:
            pool[iter2.up].down = iter2 - root_
            pool[iter2.down].up = iter2 - root_
            pool[iter2.data.head].data.size += 1
            iter2 = pool[iter2.left]
        iter = pool[iter.up]

    pool[header.left].right = header - root_
    pool[header.right].left = header - root_

def search(root):
    if root.right is None:
        return True

    header = pool[root.right]
    for iter in range(header, root, pool[iter.right]):
        if iter.data.size == 0:
            return False
        if iter.data.size < header.data.size:
            header = iter

    ret = False

    cover(header)
    for iter in range(pool[header.down], header, pool[iter.down]):
        for iter2 in range(pool[iter.right], iter, pool[iter2.right]):
            cover(pool[iter2.data.head])

        if search(root):
            ret = True
            x = (iter - nodes_) // 4
            i = x // (N_2 * N_2)
            j = (x % (N_2 * N_2)) // N_2
            val = (x % N_2) + base
            solution[i][j] = chr(val)

        for iter2 in range(pool[iter.left], iter, pool[iter2.left]):
            uncover(pool[iter2.data.head])

        if ret:
            break
    uncover(header)

    return ret

def display(g):
    for row in g:
        print("".join(row))

def add_row(l, c, val):
    pos = [0] * 4
    k = ord(val) - base
    pos[0] = (l * N_2) + c
    pos[1] = (l * N_2) + k
    pos[2] = (c * N_2) + k
    pos[3] = ((N * (l // N) + c // N) * N_2) + k

    last = None
    for i in range(4):
        nd = nodes_[(l * N_2 * N_2 + c * N_2 + k) * 4 + i]
        InitNode(headers_[i * N_2 * N_2 + pos[i]], last, nd)
        last = nd

def init(g):
    root = root_
    InitRoot(root)

    for i in range(1, 1 + 4 * N_2 * N_2):
        header = pool[i]
        header.left = i - 1
        header.up = header.down = i
        header.data.size = 0
        pool[i - 1].right = i
    pool[1 + 4 * N_2 * N_2].right = None
    root.left = i

    for l in range(N_2):
        for c in range(N_2):
            v = g[l][c]
            if v != vide:
                add_row(l, c, v)
            else:
                for val in range(base, base + N_2):
                    add_row(l, c, chr(val))

    return root

grid=[['.', 'F', 'L', 'J', '.', '.', '.', 'D', '.', '.', 'O', '.', 'E', '.', '.', 'G', 'M', '.', 'K', 'S', 'N', 'R', 'Q', 'X', 'A'], ['.', '.', '.', 'H', 'K', '.', 'C', 'X', 'R', 'O', 'U', 'V', '.', '.', '.', 'Q', 'F', '.', 'B', 'E', 'S', 'J', 'P', '.', '.'], ['R', 'N', 'M', 'Y', '.', 'B', 'Q', 'E', 'T', 'A', '.', 'F', '.', '.', '.', 'X', 'O', 'V', 'P', '.', 'W', '.', 'H', 'D', '.'], ['Q', 'O', '.', '.', 'P', 'M', 'K', '.', 'S', 'Y', 'N', '.', 'I', 'A', 'R', '.', 'L', '.', 'C', '.', '.', '.', '.', 'E', 'B'], ['.', 'E', '.', '.', '.', 'L', '.', '.', 'G', '.', 'B', 'P', 'H', 'Q', 'D', '.', 'R', 'N', '.', 'T', 'Y', 'O', '.', '.', '.'], ['Y', 'T', '.', '.', 'J', 'I', '.', '.', 'U', 'V', 'G', '.', '.', 'B', 'L', '.', 'E', '.', 'X', 'O', 'C', 'M', '.', '.', 'R'], ['H', 'S', '.', '.', '.', '.', 'A', '.', 'K', 'L', 'C', '.', '.', 'O', '.', '.', 'P', 'F', '.', 'W', '.', 'I', '.', 'V', 'Y'], ['X', '.', 'F', 'R', '.', '.', '.', 'O', 'Q', '.', 'I', 'K', 'W', 'T', 'P', 'Y', 'D', '.', 'U', '.', 'A', '.', 'E', 'H', '.'], ['N', '.', '.', '.', '.', 'P', 'Y', 'S', 'F', 'X', '.', 'U', 'Q', '.', '.', 'B', 'V', 'G', 'H', 'C', '.', 'K', 'J', 'O', '.'], ['.', '.', '.', 'L', 'C', '.', '.', '.', 'W', 'D', 'H', '.', '.', 'V', 'M', '.', 'T', '.', 'I', '.', '.', '.', '.', 'N', 'X'], ['.', '.', '.', 'B', '.', '.', 'I', 'Y', 'H', '.', 'D', 'L', 'A', 'X', '.', '.', 'S', 'K', 'W', '.', 'O', '.', '.', '.', '.'], ['.', '.', 'H', 'P', '.', '.', 'N', 'A', '.', '.', '.', '.', '.', 'I', 'Q', 'T', 'G', 'U', '.', '.', 'X', 'Y', 'S', 'W', 'E'], ['K', '.', 'O', '.', 'Y', 'G', 'S', 'Q', 'D', 'B', 'W', '.', '.', '.', '.', '.', '.', 'X', 'E', '.', '.', 'L', 'M', 'R', 'P'], ['U', 'Q', 'N', 'W', 'R', '.', 'P', 'T', 'L', 'E', 'Y', '.', 'O', '.', 'V', 'A', 'H', '.', '.', '.', 'K', 'C', 'I', '.', '.'], ['T', '.', '.', 'X', 'D', 'O', 'W', '.', '.', '.', '.', 'E', '.', 'P', 'N', '.', '.', 'I', '.', 'L', 'G', 'U', '.', 'B', 'H'], ['.', '.', 'R', '.', 'N', 'D', 'G', 'C', '.', '.', '.', '.', 'M', 'E', 'J', 'U', 'K', 'O', 'S', '.', '.', '.', 'F', 'Y', 'W'], ['.', '.', 'G', 'D', 'H', '.', '.', 'R', '.', '.', 'V', '.', '.', 'N', 'C', 'L', '.', 'M', '.', 'Q', 'E', '.', 'X', 'J', '.'], ['.', '.', 'J', '.', 'F', '.', '.', '.', '.', 'Q', 'A', 'W', '.', '.', '.', '.', 'X', 'R', '.', 'P', 'M', 'H', 'O', '.', 'I'], ['.', 'U', '.', 'S', '.', 'J', 'E', 'K', '.', 'N', '.', 'R', '.', 'L', 'I', '.', 'W', 'T', 'Y', 'B', 'V', '.', '.', 'A', '.'], ['V', 'W', '.', '.', '.', '.', 'O', 'L', '.', '.', '.', 'H', 'D', 'K', '.', '.', '.', '.', '.', 'I', '.', 'N', 'R', 'Q', 'U'], ['.', '.', '.', '.', 'T', '.', 'B', 'H', 'N', '.', 'J', 'D', 'C', 'W', '.', 'O', '.', 'E', 'L', '.', '.', '.', 'V', '.', '.'], ['.', 'L', '.', '.', 'B', 'F', 'X', '.', 'A', 'G', 'P', '.', '.', '.', 'K', 'M', '.', '.', 'V', 'H', '.', '.', 'T', '.', '.'], ['.', '.', '.', 'O', '.', 'Y', '.', '.', 'E', '.', '.', 'N', 'V', 'F', 'B', '.', '.', '.', 'T', 'X', '.', '.', 'L', 'K', '.'], ['E', '.', 'K', '.', '.', '.', 'L', 'I', '.', '.', '.', 'S', '.', '.', '.', 'F', '.', '.', '.', 'A', 'D', '.', 'Y', 'G', '.'], ['D', 'X', 'Y', 'V', 'Q', '.', 'J', 'P', 'O', 'T', '.', 'M', 'L', '.', 'A', '.', 'I', 'S', 'N', 'G', 'H', '.', 'B', '.', 'F']]


if __name__ == "__main__":
    grille = [[" " for _ in range(N_2)] for _ in range(N_2)]
    #print(grille,file=sys.stderr)
    for l in range(N_2):
        line = grid[l]
        grille[l] = line

    root = init(grille)
    ok = search(root)

    display(solution)
