visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
 
    if start == goal:
        return "That was easy! Start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)

    return "So sorry, but a connecting path doesn't exist :("
 


# Driver Code

def aufbauTabelle(zeile, tabelle, y):
    i = 0
    while i < len(zeile):
        if zeile[i:i+1] == '.':
            tabelle.append(str(i) + '-' + str(y))       
        i = i +1

def aufbauGraph(tabelle,graph, maxX):
    for tab in tabelle:
        neuTab = []
        x,y = tab.split("-")
        x = int(x)
        y = int(y)
        if x + 1 == maxX:
            s1 = str(0) + "-" + str(y)
        else:
            s1 = str(x+1) + "-" + str(y)
        if x -1 < 0:
            s2 = str(maxX-1) + "-" + str(y)
        else:
            s2 = str(x-1) + "-" + str(y)
        s3 = str(x) + "-" + str(y+1)
        s4 = str(x) + "-" + str(y-1)
        if s1 in tabelle:
            neuTab.append(s1)
        if s2 in tabelle:
            neuTab.append(s2)
        if s3 in tabelle:
            neuTab.append(s3)
        if s4 in tabelle:
            neuTab.append(s4)
        graph[tab] = neuTab

def keyloesen(key):
    x,y = key.split("-")
    return int(x), int(y)

def umsetzen(von,zu):
    x1, y1 = keyloesen(von)
    x2, y2 = keyloesen(zu)
    if x1 > x2:
        return "L"
    if x1 < x2:
        return "R"
    if y1 > y2:
        return "U"
    if y1 < y2:
        return "D"

def aufbauGraph2(tab2,graph2, maxX):
    for y in range(maxX):
        for x in range(maxX):
            feld = str(x) + "-" + str(y)
            wege = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x1 = x + new_position[0]
                y1 = y + new_position[1]
                if x1 >= 0 and x1 < maxX and y1 >= 0 and y1 < maxX:
                    if tab2[y1][x1] == 0:
                        wege.append(str(x1)+"-"+str(y1))
            graph2[feld] = wege



z1= '##########'
z2= '#...#....#'
z3= '###.##.#.#'
z4= '#.#..###.#'
z5= '#.##.#...#'
z6= '#..#.###.#'
z7= '#.##...#.#'
z8= '#..###.#.#'
z9= '#........#'
z10='##########'
print('Start  ' + str(len(z1)))
tabelle = []
aufbauTabelle(z1,tabelle,0)
aufbauTabelle(z2,tabelle,1)
aufbauTabelle(z3,tabelle,2)
aufbauTabelle(z4,tabelle,3)
aufbauTabelle(z5,tabelle,4)
aufbauTabelle(z6,tabelle,5)
aufbauTabelle(z7,tabelle,6)
aufbauTabelle(z8,tabelle,7)
aufbauTabelle(z9,tabelle,8)
aufbauTabelle(z10,tabelle,9)
print(tabelle)
graph = {}
aufbauGraph(tabelle,graph, len(z1))
print(graph)

tab2  = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
graph2 = {}        
aufbauGraph2(tab2,graph2, 10)
print(graph2)
#alle möglichen wege
bfs(visited, graph, '1-1')
print('--------------------------------------------------------------------------\n')
print(visited)
print(' ')
print('--------------------------------------------------------------------------\n')
ergebnis = bfs_shortest_path(graph2, '1-1', '8-8')
print(ergebnis)

move = ""
start = str(1) + "-" + str(1)
for schritt in ergebnis:
    if start != schritt:
        move = move + umsetzen(start,schritt)
    start = schritt

print(move)