import sys,math,string,copy,time

startTime=time.time()

#w, h = [int(i) for i in input().split()]
#grid = [[int(j) for j in input().split()] for _ in range(h)]
#1   = 1
w,h=10,10
grid=[[0, 0, 0, 0, 0, 0, 0, 0, 9, 0], [0, 0, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 20, 0, 0, 8, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 6, 0, 0, 0], [10, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 0, 6, 0, 0, 0, 8, 0], [0, 0, 0, 0, 0, 0, 6, 0, 0, 0]]

#3    = 
w,h=20,20
grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0], [18, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 6, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 0, 0], [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 6, 0, 0, 8, 0, 0, 6, 0, 0, 0, 0, 0, 0], [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 12, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 16, 0, 0, 10, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 6, 0, 0, 8, 0, 8, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 26, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0]]



rectangles=[] # All possible rectangles in all posible positions
partial_content=[[0]*w for _ in range(h)] # how many non-empty cells
# are in the top-left corner of the grid
prev_content=lambda x,y : partial_content[y][x] if x >= 0 and y >= 0 else 0

for x in range(w):
    for y in range(h):
        partial_content[y][x] = (1 if grid[y][x] > 0 else 0) \
            + prev_content(x - 1, y) + prev_content(x, y - 1) \
            - prev_content(x - 1, y - 1)

for x in range(w):
    for y in range(h):
        s = grid[y][x]
        if s == 0:
            continue
        for sx in range(1, s+1):
            if s % sx != 0:
                continue
            sy = s // sx
            for x1 in range(max(0, x - sx + 1), x + 1):
                for y1 in range(max(0, y - sy + 1), y + 1):
                    x2 = x1 + sx - 1
                    y2 = y1 + sy - 1
                    if x2 >= w or y2 >= h:
                        continue
                    count = prev_content(x2, y2) - prev_content(x1 - 1, y2) \
                        - prev_content(x2, y1 - 1) + prev_content(x1 - 1, y1 - 1)
                    if count == 1:
                        rectangles.append((x1, y1, x2, y2))
        
C = {}
for x in range(w):
    for y in range(h):
        C[(x, y)] = set()
R = {}
for i, r in enumerate(rectangles):
    R[i] = []
    for x in range(r[0], r[2]+1):
        for y in range(r[1], r[3]+1):
            R[i].append((x, y))
            C[(x, y)].add(i)

def solve(X, Y, solution=[]):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()

def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)

solutions = []
decorations = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for sol in solve(C, R):
    decorated_sol = [[None]*w for _ in range(h)]
    index = 0
    for y in range(h):
        for x in range(w):
            if decorated_sol[y][x] is None:
                for r in [rectangles[i] for i in sol]:
                    if r[0]<=x<=r[2] and r[1]<=y<=r[3]:
                        for x1 in range(r[0], r[2]+1):
                            for y1 in range(r[1], r[3]+1):
                                decorated_sol[y1][x1] = decorations[index]
                        index += 1
                        break
    solutions.append(decorated_sol)

solutions.sort()
print(len(solutions))
for row in solutions[0]:
    print(''.join(row))

print("Zeit: {}".format(time.time()-startTime),file=sys.stderr)
