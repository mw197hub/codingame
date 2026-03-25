from typing import List, Tuple, Dict, Optional, Set
import sys,time

# ---------- Datenmodelle ----------
class Node:
    def __init__(self, x:int, y:int, req:int, idx:int):
        self.x=x; self.y=y; self.req=req; self.idx=idx; self.links=0
    def rem(self)->int: return self.req - self.links
    def __repr__(self):
        return f"N{self.idx}({self.x},{self.y},req={self.req},links={self.links})"

class Edge:
    def __init__(self, a:int, b:int, cells:List[Tuple[int,int]], idx:int):
        self.a=a; self.b=b; self.cells=cells; self.count=0; self.idx=idx
    def other(self,u:int)->int:
        return self.b if u==self.a else self.a
    def remcap(self)->int:
        return 2 - self.count

# Union-Find für schnelle Konnektivität
class UF:
    def __init__(self,n:int): self.p=list(range(n))
    def find(self,a:int):
        while self.p[a]!=a:
            self.p[a]=self.p[self.p[a]]
            a=self.p[a]
        return a
    def union(self,a:int,b:int):
        ra,rb = self.find(a), self.find(b)
        if ra!=rb: self.p[rb]=ra

# ---------- Hilfsfunktionen zum Parsen ----------
def parse_grid(grid:List[str]):
    nodes=[]; pos2idx={}
    h=len(grid); w=len(grid[0]) if h>0 else 0
    idx=0
    for y,row in enumerate(grid):
        for x,ch in enumerate(row):
            if ch.isdigit():
                nodes.append(Node(x,y,int(ch), idx))
                pos2idx[(x,y)] = idx
                idx += 1
    return nodes, pos2idx, w, h

def find_edges(nodes:List[Node], pos2idx:Dict[Tuple[int,int],int], w:int, h:int):
    edges=[]; seen=set(); idx=0
    for n in nodes:
        x,y = n.x,n.y
        # right
        cx = x+1; cells=[]
        while cx < w:
            if (cx,y) in pos2idx:
                j = pos2idx[(cx,y)]
                a,b = n.idx, j
                if (a,b) not in seen:
                    edges.append(Edge(a,b,cells.copy(), idx)); idx+=1
                    seen.add((a,b)); seen.add((b,a))
                break
            cells.append((cx,y)); cx+=1
        # down
        cy = y+1; cells=[]
        while cy < h:
            if (x,cy) in pos2idx:
                j = pos2idx[(x,cy)]
                a,b = n.idx, j
                if (a,b) not in seen:
                    edges.append(Edge(a,b,cells.copy(), idx)); idx+=1
                    seen.add((a,b)); seen.add((b,a))
                break
            cells.append((x,cy)); cy+=1
    return edges

# ---------- Solver (heuristisch + forced moves) ----------
class HashiSolver:
    def __init__(self, grid:List[str]):
        self.grid = grid
        self.nodes, self.pos2idx, self.w, self.h = parse_grid(grid)
        self.edges = find_edges(self.nodes, self.pos2idx, self.w, self.h)
        # adjacency: node -> edge indices
        self.adj = [[] for _ in range(len(self.nodes))]
        for i,e in enumerate(self.edges):
            e.idx = i
            self.adj[e.a].append(i)
            self.adj[e.b].append(i)
        self.occupied: Dict[Tuple[int,int], int] = {}  # cell -> edge idx occupying it
        self.steps = 0
        self.solution = None

    # capacity sum for node (remaining capacity across incident edges)
    def node_capacity(self, v:int) -> int:
        s = 0
        for ei in self.adj[v]:
            s += self.edges[ei].remcap()
        return s

    # forward checks: node capacity and connectivity of nodes that still need links
    def forward_feasible(self) -> bool:
        # capacity check
        for v in range(len(self.nodes)):
            if self.nodes[v].rem() > self.node_capacity(v):
                return False
        # connectivity check: edges with remcap>0 connect nodes that still need >0 into one component
        uf = UF(len(self.nodes))
        for e in self.edges:
            if e.remcap() > 0:
                uf.union(e.a, e.b)
        comps = set()
        for v in range(len(self.nodes)):
            if self.nodes[v].rem() > 0:
                comps.add(uf.find(v))
        return len(comps) <= 1

    # mark/unmark occupied cells for an edge when its count transitions 0<->>0
    def occupy_edge_cells(self, ei:int, set_occupied:bool):
        e = self.edges[ei]
        if set_occupied:
            for c in e.cells:
                self.occupied[c] = ei
        else:
            # remove only the cells occupied by this edge (others would never be present because crossing forbidden)
            for c in e.cells:
                if self.occupied.get(c) == ei:
                    del self.occupied[c]

    # check if we can set edge ei to newcount (taking crossing and node caps into account)
    def can_set_edge(self, ei:int, newcount:int) -> bool:
        e = self.edges[ei]
        if not (0 <= newcount <= 2): return False
        da = newcount - e.count
        if self.nodes[e.a].links + da > self.nodes[e.a].req: return False
        if self.nodes[e.b].links + da > self.nodes[e.b].req: return False
        # if we are increasing from 0 to >0, ensure no crossing on intermediate cells
        if e.count == 0 and newcount > 0:
            for c in e.cells:
                occ = self.occupied.get(c)
                if occ is not None and occ != ei:
                    return False
        return True

    # apply setting edge count (does not do forward checks)
    def set_edge(self, ei:int, newcount:int):
        e = self.edges[ei]
        prev = e.count
        if prev == 0 and newcount > 0:
            self.occupy_edge_cells(ei, True)
        if prev > 0 and newcount == 0:
            self.occupy_edge_cells(ei, False)
        delta = newcount - prev
        e.count = newcount
        self.nodes[e.a].links += delta
        self.nodes[e.b].links += delta

    # undo is simply set_edge back to prevcount (we rely on calling code to remember prev)
    # ---------- Forced propagation ----------
    def propagate_forced(self) -> bool:
        """Apply forced moves until quiescent. Return False if contradiction found."""
        changed = True
        while changed:
            changed = False
            # 1) If node has rem() == 0 -> skip
            # 2) If node has only one incident edge with remcap>0, it must take as many as needed there (up to edge capacity)
            for v in range(len(self.nodes)):
                r = self.nodes[v].rem()
                if r <= 0: continue
                avail_edges = [ei for ei in self.adj[v] if self.edges[ei].remcap() > 0]
                if not avail_edges:
                    return False
                if len(avail_edges) == 1:
                    ei = avail_edges[0]
                    e = self.edges[ei]
                    # we must place enough on this edge to satisfy this node (but limited by edge remcap and the other node's need)
                    max_put = min(e.remcap(), self.nodes[e.other(v)].rem())
                    need = r
                    put = min(max_put, need)
                    if put <= 0: return False
                    newcount = e.count + put
                    if not self.can_set_edge(ei, newcount): return False
                    self.set_edge(ei, newcount)
                    changed = True
                    # after setting, continue the propagation loop
            # 3) If for a node, sum of remcaps of a subset equals rem(), more advanced forcing could be applied,
            #    but we implement a simpler check: if rem() == sum of remcap of all incident edges, set all those to full
            for v in range(len(self.nodes)):
                r = self.nodes[v].rem()
                if r <= 0: continue
                avail = [ei for ei in self.adj[v] if self.edges[ei].remcap() > 0]
                total = sum(self.edges[ei].remcap() for ei in avail)
                if total == r:
                    # must fill all avail edges to capacity (or as needed)
                    for ei in avail:
                        e = self.edges[ei]
                        other_need = self.nodes[e.other(v)].rem()
                        will_put = min(e.remcap(), other_need)
                        if will_put <= 0:
                            return False
                        newcount = e.count + will_put
                        if not self.can_set_edge(ei, newcount): return False
                        self.set_edge(ei, newcount)
                        changed = True
        return True

    # ---------- Heuristic selection ----------
    def select_most_constrained_node(self) -> Optional[int]:
        """Select node with rem()>0 and minimum number of available edges (MRV)."""
        best = None
        best_metric = None
        for v in range(len(self.nodes)):
            r = self.nodes[v].rem()
            if r <= 0: continue
            avail = [ei for ei in self.adj[v] if self.edges[ei].remcap() > 0]
            if not avail:
                return None
            metric = (len(avail), sum(self.edges[ei].remcap() for ei in avail))
            if best is None or metric < best_metric:
                best = v; best_metric = metric
        return best

    # ---------- Connectivity final check ----------
    def final_connected(self) -> bool:
        uf = UF(len(self.nodes))
        for e in self.edges:
            if e.count > 0:
                uf.union(e.a, e.b)
        root = uf.find(0) if len(self.nodes)>0 else 0
        for i in range(len(self.nodes)):
            if uf.find(i) != root:
                return False
        return True

    # ---------- Recursive backtracking ----------
    def backtrack(self) -> bool:
        self.steps += 1
        # quick overshoot check
        for n in self.nodes:
            if n.links > n.req:
                return False
        # if all satisfied, check connectivity
        if all(n.links == n.req for n in self.nodes):
            if self.final_connected():
                self.solution = [(self.nodes[e.a].x, self.nodes[e.a].y,
                                  self.nodes[e.b].x, self.nodes[e.b].y, e.count)
                                 for e in self.edges if e.count > 0]
                return True
            else:
                return False
        # forward check
        if not self.forward_feasible():
            return False
        # forced propagation
        if not self.propagate_forced():
            return False
        # choose node to branch on
        node = self.select_most_constrained_node()
        if node is None:
            return False
        # get candidate edges with positive remcap incident to node
        cand_edges = [ei for ei in self.adj[node] if self.edges[ei].remcap() > 0]
        # sort edges by shortness (fewer cells) and by partner remaining need (bigger needs first)
        cand_edges.sort(key=lambda ei: (len(self.edges[ei].cells),
                                       -self.nodes[self.edges[ei].other(node)].rem()))
        # for branching: we'll try to assign counts on these edges in a small combinatorial manner:
        # prefer larger assignments first (try to satisfy node quickly)
        # We'll attempt combinations: for each edge we can set 0..remcap; but we restrict branching using node.rem()
        rem_need = self.nodes[node].rem()
        # build list of (ei, max_put)
        bounds = [(ei, min(self.edges[ei].remcap(), self.nodes[self.edges[ei].other(node)].rem())) for ei in cand_edges]
        # Simple recursive combinatoric over incident edges but pruning heavily by feasibility
        assign_stack: List[Tuple[int, List[int]]] = []  # (position, assigned_list)
        # We'll do DFS ourselves to allow undo without deep copy
        def dfs_assign(pos:int, assigned:List[int]) -> bool:
            if sum(assigned) > rem_need:
                return False
            if pos == len(bounds):
                if sum(assigned) != rem_need:
                    return False
                # apply assignments to edges and recurse globally
                prev_states = []
                for (ei,_),put in zip(bounds, assigned):
                    prev_states.append((ei, self.edges[ei].count))
                    newcount = self.edges[ei].count + put
                    if not self.can_set_edge(ei, newcount):
                        # rollback
                        for ei2,prevc in prev_states:
                            self.set_edge(ei2, prevc)
                        return False
                    self.set_edge(ei, newcount)
                # recurse
                ok = self.backtrack()
                if ok: return True
                # undo
                for ei,prevc in reversed(prev_states):
                    self.set_edge(ei, prevc)
                return False
            ei, max_put = bounds[pos]
            # try larger puts first (heuristic)
            for put in range(max_put, -1, -1):
                assigned.append(put)
                if dfs_assign(pos+1, assigned):
                    return True
                assigned.pop()
            return False

        return dfs_assign(0, [])

    # ---------- API ----------
    def solve(self, verbose:bool=False, max_steps:Optional[int]=None) -> Optional[List[Tuple[int,int,int,int,int]]]:
        # initial forced propagation before backtracking
        if not self.propagate_forced():
            return None
        ok = self.backtrack()
      #  if verbose:
      #      print(f"Steps: {self.steps}", file=sys.stderr)
        return self.solution if ok else None

# ---------- ASCII Visualisierung ----------
def draw_solution(grid:List[str], solution:List[Tuple[int,int,int,int,int]]):
    board = [list(row) for row in grid]
    for x1,y1,x2,y2,c in solution:
        if x1 == x2:
            for y in range(min(y1,y2)+1, max(y1,y2)):
                board[y][x1] = '|' if c==1 else '║'
        elif y1 == y2:
            for x in range(min(x1,x2)+1, max(x1,x2)):
                board[y1][x] = '-' if c==1 else '='
    return [''.join(row) for row in board]

# ---------- Beispiel-Ausführung ----------
if __name__ == "__main__":
    start=time.time()
    big_grid = [
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
   # big_grid=['2..2.1.', '.3..5.3', '.2.1...', '2...2..', '.1....2']
   # big_grid=['25.1', '47.4', '..1.', '3344']
    big_grid=['22221', '2....', '2....', '2....', '2....', '22321', '.....', '.....', '22321', '2....', '2....', '2.131', '2..2.', '2222.']

    solver = HashiSolver(big_grid)
    sol = solver.solve(verbose=True)
    if sol is None:
        print("Keine Lösung gefunden (oder Timeout/zu schwer).")
        # optional debug prints
        # print("Nodes:", solver.nodes)
        # print("Edges:", solver.edges)
    else:
        print("Gefundene Brücken (x1,y1,x2,y2,count):")
        for t in sol:            
            print("{} {} {} {} {}".format(t[0],t[1],t[2],t[3],t[4]))
        vis = draw_solution(big_grid, sol)
        print("\nASCII-Visualisierung:")
        for row in vis:
            print(row)

print("Zeit: {}".format(time.time()-start),file=sys.stderr)