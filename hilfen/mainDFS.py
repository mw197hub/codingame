
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

def dfs(visited,graph, node):
    if node not in visited:
      #  print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

tabelle = []
graph = {}
visited = set()


##   Beispiel
z1= '##########'
z2= '#...#....#'
z3= '###.##.#.#'
z4= '#.#..###.#'
z5= '####.#...#'
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
print(len(tabelle))

aufbauGraph(tabelle,graph, len(z1))
print(graph)

dfs(visited,graph,'1-1')
print(len(visited))