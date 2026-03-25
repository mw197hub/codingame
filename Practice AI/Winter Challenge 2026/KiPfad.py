import heapq
import time
import os

class GravitySnakeSolver:
    def __init__(self, grid, snake_start, goal, max_reach):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.snake_start = tuple(snake_start)
        self.goal = goal
        self.max_reach = max_reach

    def get_grounded_index(self, body):
        """Findet das erste Segment, das Boden unter sich hat."""
        for i, (y, x) in enumerate(body):
            if y + 1 < self.rows and self.grid[y+1][x] == 1:
                return i
        return None

    def get_neighbors(self, current_body):
        neighbors = []
        hy, hx = current_body[0]

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ty, tx = hy + dy, hx + dx

            # 1. Basis-Checks
            if not (0 <= ty < self.rows and 0 <= tx < self.cols): continue
            if self.grid[ty][tx] == 1: continue
            if (ty, tx) in current_body[:-1]: continue

            # 2. Bewegung ausführen (Kopf schiebt, Schwanz zieht nach)
            new_body = [(ty, tx)] + list(current_body[:-1])

            # 3. Physik-Simulation (Stabilität vor Sacken)
            while True:
                g_idx = self.get_grounded_index(new_body)
                
                # Absturz wenn kein Halt oder Reichweite überschritten
                if g_idx is None or g_idx > self.max_reach:
                    if any(y + 1 >= self.rows for y, x in new_body): 
                        new_body = None
                        break
                    new_body = [(y + 1, x) for y, x in new_body]
                    continue 

                # Kontrolliertes Sacken des Kopfes
                chy, chx = new_body[0]
                if chy + 1 < self.rows and self.grid[chy+1][chx] == 0:
                    potential = [(chy + 1, chx)] + list(new_body[:-1])
                    p_g_idx = self.get_grounded_index(potential)
                    # Nur sacken, wenn danach noch stabil
                    if p_g_idx is not None and p_g_idx <= self.max_reach:
                        if (chy + 1, chx) in new_body[1:]: break
                        new_body = potential
                        continue 
                break 

            if new_body:
                neighbors.append(tuple(new_body))
        return neighbors

    def solve(self):
        # A* Suche
        pq = [(0, 0, self.snake_start)]
        visited = {self.snake_start: 0}
        came_from = {self.snake_start: None}
        
        while pq:
            _, cost, current_body = heapq.heappop(pq)
            if current_body[0] == self.goal:
                path = []
                while current_body:
                    path.append(current_body)
                    current_body = came_from.get(current_body)
                return path[::-1]

            for next_state in self.get_neighbors(current_body):
                if next_state not in visited or cost + 1 < visited[next_state]:
                    visited[next_state] = cost + 1
                    # Heuristik: Manhattan Distanz des Kopfes zum Ziel
                    h = abs(next_state[0][0] - self.goal[0]) + abs(next_state[0][1] - self.goal[1])
                    heapq.heappush(pq, (cost + 1 + h, cost + 1, next_state))
                    came_from[next_state] = current_body
        return None

def draw_frame(grid, snake, goal):
    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0])):
            if (r, c) == goal: row += " X "
            elif (r, c) in snake: row += f" {snake.index((r,c))} "
            elif grid[r][c] == 1: row += "###"
            else: row += " . "
        print(row)

# Dein Spielfeld
game_grid = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,1,1], 
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0], 
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1]
]

# Start: Schlange liegt auf Zeile 3, Kopf ist (3,0)
start_snake = ((2, 0), (2, 1), (2, 2), (2, 3))
goal_pos = (0, 6)

# max_reach=3 bedeutet, sie darf sich 3 Segmente weit über Abgründe lehnen
solver = GravitySnakeSolver(game_grid, start_snake, goal_pos, max_reach=99)
path = solver.solve()

if path:
    for i, step in enumerate(path):
        # os.system('cls' if os.name == 'nt' else 'clear') # Windows/Linux clear
        print(f"\nSchritt {i}:")
        draw_frame(game_grid, step, goal_pos)
        time.sleep(0.2)
else:
    print("Kein Pfad gefunden. Erhöhe ggf. max_reach oder die Körperlänge.")
