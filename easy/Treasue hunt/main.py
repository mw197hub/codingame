import sys
import math



def bfs(wege, queue, visited, graph, node):
    if node not in visited:
      #  print(node)
        visited.append(node)
        for neighbour in graph[node]:
            bfs(wege, queue, visited,graph,neighbour)
        wege.append(visited[:])
        visited.pop()


def aufbauGraph(tab,graph, h,w):
    start = ""
    for y in range(h):
        for x in range(w):
            wege = []
            if not tab[y][x] == '#':
                feld = str(x) + "-" + str(y)
                if tab[y][x] == "X":
                    start = feld
                for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    x1 = x + new_position[0]
                    y1 = y + new_position[1]
                    if x1 >= 0 and x1 < w and y1 >= 0 and y1 < h:
                        if not tab[y1][x1] == '#':
                            wege.append(str(x1)+"-"+str(y1))
            if len(wege) > 0:
                graph[feld] = wege
    return start


h,w = 3,3
tab = ['X##', '1 5', '3#4']
h,w = 7,12
tab = ['############', '#9 2 #4#4  #', '####1# ###1#', '#3 1 #3 2 1#', '###1######1#', '#3 1 1 1 1X#', '############']

graph = {}
wege = []; visited = []; queue = []
start = aufbauGraph(tab,graph,h,w)
#print(graph,file=sys.stderr)
bfs(wege, queue, visited, graph, start)
erg = 0
for weg in wege:
    sum = 0
    for feld in weg:        
        k = feld.split("-")       
        if tab[int(k[1])][int(k[0])] in ['1','2','3','4','5','6','7','8','9']:
            sum += int(tab[int(k[1])][int(k[0])])
    if sum > erg:
        erg = sum

print(str(erg))