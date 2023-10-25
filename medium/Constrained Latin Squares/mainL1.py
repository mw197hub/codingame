import sys,math,copy,time
zeit = time.time()


iList=['123','200','300']
#iList=['000','123','312']
iList=['2000007','0403000','0030000','0006004','1500000','0000020','0100070']


#iList=['087604321','800000002','700000003','600523000','000302005','401230006','300000007','200000008','103050780']




n=len(iList)
grid = [list(map(int, list(iList[i]))) for i in range(n)]

avail_in_row = [[1] * n for _ in range(n)]
avail_in_col = [[1] * n for _ in range(n)]
a=0
for x, y in [(x,y) for y in range(n) for x in range(n) if grid[x][y] > 0]:
    avail_in_row[x][grid[x][y]-1] = 0
    avail_in_col[y][grid[x][y]-1] = 0

zeros_cord = [(x,y) for y in range(n) for x in range(n) if grid[y][x] == 0]
zeros_cord.sort(key=lambda x: sum(avail_in_col[x[0]]) + sum(avail_in_row[x[1]]))

result = 0

def DFS(i,result):
    global avail_in_col, avail_in_row

    if i == len(zeros_cord):
        result += 1
        return result

    x, y = zeros_cord[i]

    for m in range(n):
        if avail_in_col[x][m] > 0 and avail_in_row[y][m] > 0:
            avail_in_col[x][m] = 0
            avail_in_row[y][m] = 0
            result = DFS(i+1,result)
            avail_in_col[x][m] = 1
            avail_in_row[y][m] = 1
    return result

result = DFS(0,result)
print(result)

print("Zeit: {}".format(time.time()-zeit),file=sys.stderr)  
