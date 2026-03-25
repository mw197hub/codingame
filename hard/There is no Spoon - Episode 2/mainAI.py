"""
Hashiwokakero (Bridges) Solver mit ASCII-Visualisierung

Funktionen:
- Löst ein beliebiges Grid mit Hashiwokakero-Regeln
- Kreuzungsprüfung, max. 2 Brücken pro Paar, Konnektivität
- Ausgabe der Lösung als Koordinaten
- ASCII-Visualisierung direkt im Terminal

"""
from typing import List, Tuple, Dict, Optional

class Node:
    def __init__(self, x:int, y:int, req:int, idx:int):
        self.x=x; self.y=y; self.req=req; self.idx=idx; self.links=0
    def rem(self): return self.req - self.links

class Edge:
    def __init__(self, a:int, b:int, cells:List[Tuple[int,int]], idx:int):
        self.a=a; self.b=b; self.cells=cells; self.count=0; self.idx=idx

class UF:
    def __init__(self,n): self.p=list(range(n))
    def find(self,a):
        while self.p[a]!=a:
            self.p[a]=self.p[self.p[a]]; a=self.p[a]
        return a
    def union(self,a,b):
        ra,rb=self.find(a),self.find(b)
        if ra!=rb: self.p[rb]=ra

# Parser und Edge-Finder
def parse_grid(grid:List[str]):
    nodes=[]; pos2idx={}
    h=len(grid); w=len(grid[0]) if h>0 else 0
    idx=0
    for y,row in enumerate(grid):
        for x,ch in enumerate(row):
            if ch.isdigit():
                nodes.append(Node(x,y,int(ch), idx))
                pos2idx[(x,y)]=idx; idx+=1
    return nodes,pos2idx,w,h

def find_edges(nodes,pos2idx,w,h):
    edges=[]; seen=set(); idx=0
    for n in nodes:
        x,y=n.x,n.y
        # rechts
        cx=x+1; cells=[]
        while cx<w:
            if (cx,y) in pos2idx:
                j=pos2idx[(cx,y)]; a,b=n.idx,j
                if (a,b) not in seen:
                    edges.append(Edge(a,b,cells.copy(),idx)); idx+=1
                    seen.add((a,b)); seen.add((b,a))
                break
            cells.append((cx,y)); cx+=1
        # unten
        cy=y+1; cells=[]
        while cy<h:
            if (x,cy) in pos2idx:
                j=pos2idx[(x,cy)]; a,b=n.idx,j
                if (a,b) not in seen:
                    edges.append(Edge(a,b,cells.copy(),idx)); idx+=1
                    seen.add((a,b)); seen.add((b,a))
                break
            cells.append((x,cy)); cy+=1
    return edges

# Solver
def solve_grid(grid:List[str]):
    nodes,pos2idx,w,h=parse_grid(grid)
    edges=find_edges(nodes,pos2idx,w,h)
    for i,e in enumerate(edges): e.idx=i
    adj=[[] for _ in range(len(nodes))]
    for i,e in enumerate(edges):
        adj[e.a].append(i); adj[e.b].append(i)
    occupied: Dict[Tuple[int,int], int] = {}
    solution=None

    def cap(v):
        return sum(2-edges[ei].count for ei in adj[v])

    def feasible():
        for v in range(len(nodes)):
            if nodes[v].rem() > cap(v): return False
        uf=UF(len(nodes))
        for e in edges:
            if 2-e.count>0: uf.union(e.a,e.b)
        comps=set()
        for v in range(len(nodes)):
            if nodes[v].rem()>0: comps.add(uf.find(v))
        return len(comps)<=1

    def backtrack(i:int):
        nonlocal solution
        if solution is not None: return True
        if all(n.links==n.req for n in nodes):
            uf=UF(len(nodes))
            for e in edges:
                if e.count>0: uf.union(e.a,e.b)
            roots=set(uf.find(v) for v in range(len(nodes)))
            if len(roots)==1:
                solution=[(nodes[e.a].x,nodes[e.a].y,nodes[e.b].x,nodes[e.b].y,e.count) for e in edges if e.count>0]
                return True
            return False
        if i>=len(edges): return False
        if not feasible(): return False
        e=edges[i]
        max_add=min(2-e.count,nodes[e.a].rem(),nodes[e.b].rem())
        for add in range(max_add,-1,-1):
            newc=e.count+add; crossing=False
            if newc>0:
                for c in e.cells:
                    occ=occupied.get(c)
                    if occ is not None and occ!=e.idx: crossing=True; break
            if crossing: continue
            prev=e.count
            if prev==0 and newc>0:
                for c in e.cells: occupied[c]=e.idx
            if prev>0 and newc==0:
                for c in e.cells:
                    if occupied.get(c)==e.idx: del occupied[c]
            e.count=newc
            nodes[e.a].links += (newc-prev)
            nodes[e.b].links += (newc-prev)
            if backtrack(i+1): return True
            nodes[e.a].links -= (newc-prev)
            nodes[e.b].links -= (newc-prev)
            if prev==0 and newc>0:
                for c in e.cells:
                    if occupied.get(c)==e.idx: del occupied[c]
            if prev>0 and newc==0:
                for c in e.cells: occupied[c]=e.idx
            e.count=prev
        return False

    ok=backtrack(0)
    return solution if ok else None,w,h

# ASCII Visualisierung
def draw_solution(grid:List[str], solution:List[Tuple[int,int,int,int,int]], w:int,h:int):
    board=[list(row) for row in grid]
    for x1,y1,x2,y2,c in solution:
        if x1==x2:
            for y in range(min(y1,y2)+1,max(y1,y2)):
                if c==1: board[y][x1]='|'
                else: board[y][x1]='║'
        elif y1==y2:
            for x in range(min(x1,x2)+1,max(x1,x2)):
                if c==1: board[y1][x]='-'
                else: board[y1][x]='='
    return [''.join(row) for row in board]

if __name__=="__main__":
    grid=[
        '3..2.2..1....3........4',
        '.2..1....2.6.........2.',
        '..3..6....3............',
        '.......2........1..3.3.',
        '..1.............3..3...',
        '.......3..3............',
        '.3...8.....8.........3.',
        '6.5.1...........1..3...',
        '............2..6.31..2.',
        '..4..4.................',
        '5..........7...7...3.3.',
        '.2..3..3..3............',
        '......2..2...1.6...3...',
        '....2..................',
        '.4....5...3............',
        '.................2.3...',
        '.......3.3..2.44....1..',
        '3...1.3.2.3............',
        '.2.....3...6.........5.',
        '................1......',
        '.1.......3.6.2...2...4.',
        '5...............3.....3',
        '4...................4.2'
    ]
    grid=['3.4.6.2.', '.1......', '..2.5..2', '1.......', '..1.....', '.3..52.3', '.2.17..4', '.4..51.2']
    grid=['2..2.1.', '.3..5.3', '.2.1...', '2...2..', '.1....2']
    grid=['25.1', '47.4', '..1.', '3344']
    
    sol,w,h=solve_grid(grid)
    if sol is None:
        print("Keine Lösung gefunden.")
    else:
        print("Gefundene Brücken (x1,y1,x2,y2,count):")
        for s in sol:
            print(s)
        print("\nASCII-Darstellung:")
        vis=draw_solution(grid,sol,w,h)
        for row in vis:
            print(row)