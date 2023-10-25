import sys
import time

LETTERS = set('ABCDEFGHIJKLMNOP')

# Global variables strictly for solution statistics printed at the end.
calls_to_solve = 0
singleton_count = 0
single_candidate_count = 0

start = time.time()

class SudokuSolver():

    def __init__(self, grid):
        
        size = len(grid)

        self.grid  = dict()
        self.rows  = [SudokuGroup() for _ in range(size)]
        self.cols  = [SudokuGroup() for _ in range(size)]
        self.boxes = [SudokuGroup() for _ in range(size)]

        # Build the grid of cells and put each cell into the appropriate Sudoku Groups - row, col, box
        for row in range(size):
            for col in range(size):
                box = row // 4 * 4 + col // 4
                cell = SudokuCell(grid[row][col], [self.rows[row], self.cols[col], self.boxes[box]])
                self.grid[(row, col)] = cell
                self.rows[row].members.append(cell)
                self.cols[col].members.append(cell)
                self.boxes[box].members.append(cell)


    def solve(self):

        # Global variables strictly for solution statistics printed at the end.
        global calls_to_solve
        global singleton_count
        global single_candidate_count

        calls_to_solve += 1

        while True:
            candidates = {loc:self.grid[loc].candidates() for loc in self.grid if self.grid[loc].value == '.'}
            unresolved_locs = sorted(candidates.keys(), key=lambda cell:len(candidates[cell]))

            if unresolved_locs:
                loc = unresolved_locs[0]

                # If any location has zero candidates, a previous guess in the backtracking was wrong.
                if len(candidates[loc]) == 0:
                    return False

                # Any location with only one candidate can be filled in.
                elif len(candidates[loc]) == 1:
                    self.grid[loc].value = candidates[loc].pop()
                    single_candidate_count += 1
                    continue

            # If all unknown cells have more than one candidate, then check for singletons. A singleton is a
            # cell that has a candidate that no member of one of its groups also has. For instance, a cell
            # might have 'A' as a candidate, but no other cell in the same row also has 'A' as a candidate.
            # If that is the case the cell in question must be 'A' becuase 'A' must be in the row somewhere.
            singleton_found = False
            for loc in candidates:
                if singleton_found := self.grid[loc].is_singleton():
                    singleton_count += 1
                    break

            # Continue with logic if a singleton was found.
            if singleton_found:
                continue


            # When logic has been exhausted, start making guesses with the cell with fewest number of candidates.
            if not (game_solved := len(unresolved_locs) == 0):
                for value in candidates[unresolved_locs[0]]:
                    cell_to_try = unresolved_locs[0]
                    self.grid[cell_to_try].value = value
                    print("Versuch {}".format(value),file=sys.stderr)
                    if not (game_solved := self.solve()):
                        
                        # Reset the grid if solution is not found.
                        for cell in unresolved_locs:
                            self.grid[cell].value = '.'
                    else:
                        break

            return game_solved


class SudokuCell():

    def __init__(self, value, groups):
        self.value = value
        self.groups = groups


    def is_singleton(self):

        for group in self.groups:
            candidates = self.candidates()
            for cell in group.members:
                if cell != self and cell.value == '.':
                    candidates -= cell.candidates()

            if len(candidates) == 1:
                self.value = candidates.pop()
                return True

        return False


    def candidates(self):
        remaining_candidates = LETTERS.copy()
        for group in self.groups:
            remaining_candidates -= group.known_values()

        return remaining_candidates


class SudokuGroup():

    def __init__(self):
        self.members = []

    def known_values(self):
        return set(cell.value for cell in self.members)

g=[['.', 'L', 'E', 'K', '.', 'G', '.', '.', '.', '.', '.', 'N', 'O', '.', 'C', '.'], ['.', '.', 'M', '.', 'H', '.', 'J', 'O', 'B', 'D', 'G', '.', 'F', 'E', 'N', 'K'], ['J', '.', '.', 'C', '.', 'B', 'A', 'N', '.', 'E', 'K', '.', '.', '.', '.', 'I'], ['.', 'B', 'G', '.', '.', 'K', '.', '.', 'C', '.', 'J', '.', '.', 'D', 'P', 'M'], ['.', 'H', 'A', '.', 'F', 'L', '.', '.', 'K', '.', '.', 'M', '.', 'P', '.', '.'], ['.', '.', '.', 'O', 'A', '.', '.', '.', '.', '.', 'D', '.', 'I', 'K', '.', 'G'], ['.', '.', 'K', 'D', 'J', '.', 'C', 'B', 'F', 'A', 'I', 'G', '.', 'M', 'H', 'L'], ['.', 'M', '.', '.', '.', '.', '.', 'E', 'P', 'J', 'N', 'O', '.', 'A', '.', '.'], ['G', '.', '.', '.', 'I', 'A', '.', 'D', 'E', '.', 'C', 'J', 'P', '.', '.', '.'], ['A', 'K', '.', '.', '.', '.', 'G', 'H', 'N', 'M', '.', '.', 'L', 'I', 'J', '.'], ['.', '.', 'D', 'J', 'O', 'N', '.', '.', 'G', 'L', '.', 'B', 'K', 'H', '.', 'F'], ['.', 'N', '.', '.', '.', 'J', '.', 'K', '.', 'F', '.', '.', '.', 'G', 'A', 'B'], ['D', '.', '.', 'A', '.', '.', 'F', 'J', '.', '.', 'L', 'I', 'M', '.', 'K', '.'], ['E', '.', 'L', 'F', 'C', 'D', 'B', '.', 'O', '.', 'M', '.', 'N', '.', 'I', '.'], ['.', 'J', 'I', '.', '.', '.', '.', 'P', 'D', '.', '.', '.', '.', '.', 'L', '.'], ['.', '.', '.', '.', '.', 'H', '.', 'I', 'J', '.', '.', '.', '.', 'C', 'B', 'A']] # 1 
g=[['.', 'C', '.', '.', '.', '.', '.', '.', 'E', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'J', '.', '.', 'A', '.', 'B', 'F', 'P', '.', '.', '.', 'K', 'L', 'D'], ['.', '.', 'I', '.', 'D', '.', 'N', 'J', '.', 'A', '.', '.', 'E', 'B', '.', 'G'], ['L', '.', '.', 'A', '.', '.', '.', '.', 'J', '.', '.', 'N', '.', '.', '.', 'O'], ['D', 'H', '.', 'M', 'B', 'J', 'C', 'P', '.', '.', 'F', '.', '.', 'I', 'K', 'A'], ['.', '.', '.', 'L', '.', 'N', 'M', '.', '.', 'O', 'D', '.', '.', '.', '.', 'C'], ['.', '.', 'N', '.', 'I', '.', '.', '.', '.', '.', '.', '.', '.', 'G', '.', '.'], ['B', '.', '.', 'F', '.', '.', 'O', 'G', 'I', 'C', 'P', '.', '.', 'L', 'D', 'M'], ['.', 'G', '.', 'E', '.', '.', '.', 'D', '.', '.', '.', 'I', 'M', '.', 'O', 'K'], ['.', 'A', '.', '.', 'G', '.', 'P', '.', '.', '.', '.', 'F', 'L', 'H', 'C', 'N'], ['.', 'F', '.', '.', '.', '.', 'H', 'O', 'M', '.', 'B', '.', 'G', '.', 'E', '.'], ['M', 'O', 'P', '.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', 'A', '.'], ['.', '.', 'M', 'I', '.', 'B', '.', 'F', '.', 'H', 'O', 'E', 'K', '.', 'G', '.'], ['.', 'B', '.', 'D', 'C', '.', 'E', '.', 'N', '.', 'L', '.', '.', 'F', 'M', '.'], ['G', '.', '.', '.', '.', '.', '.', 'N', 'C', '.', '.', 'P', '.', 'A', '.', 'E'], ['.', 'E', 'F', 'H', '.', '.', '.', 'I', '.', '.', 'G', '.', '.', '.', 'N', '.']] # 6

#g=[['.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', 'H', 'A', 'L', '.', '.', 'N'], ['.', '.', 'N', '.', '.', '.', '.', '.', 'D', '.', '.', '.', 'O', 'E', 'F', '.'], ['.', '.', 'K', '.', 'A', '.', '.', 'J', '.', '.', 'N', 'O', '.', 'B', '.', 'P'], ['.', '.', '.', 'C', 'L', '.', 'D', '.', '.', 'G', '.', 'E', '.', 'M', '.', 'J'], ['.', '.', '.', 'J', 'H', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', 'E'], ['.', 'N', '.', 'K', '.', '.', '.', '.', '.', 'I', '.', '.', 'J', 'G', 'O', 'D'], ['.', 'O', 'M', '.', '.', 'I', 'E', 'C', 'N', 'B', '.', 'G', 'H', '.', '.', '.'], ['H', 'B', '.', '.', '.', 'D', '.', '.', 'P', '.', 'J', '.', 'N', 'F', 'C', 'I'], ['.', 'H', 'A', '.', 'M', 'E', '.', '.', '.', '.', '.', '.', 'K', 'N', '.', 'C'], ['D', '.', '.', 'E', 'N', 'B', '.', 'H', '.', 'P', 'O', 'L', '.', '.', '.', '.'], ['N', 'M', '.', 'B', '.', '.', 'O', '.', 'J', 'K', '.', '.', 'D', '.', '.', '.'], ['.', 'P', 'L', '.', '.', '.', '.', 'D', '.', '.', '.', '.', '.', 'A', '.', 'O'], ['.', 'E', '.', 'H', 'D', 'C', '.', '.', '.', '.', '.', 'F', 'P', 'K', '.', '.'], ['.', 'C', '.', '.', 'E', 'A', 'N', '.', 'O', 'L', '.', 'P', '.', 'I', '.', '.'], ['I', 'A', '.', 'N', 'G', '.', 'P', 'M', '.', '.', 'K', 'D', '.', '.', 'E', '.'], ['.', '.', 'O', '.', 'I', 'H', '.', '.', '.', '.', '.', 'N', 'A', 'C', '.', '.']] # 3



solver = SudokuSolver(g)
solver.solve()

for row in range(16):
    print(*[solver.grid[(row, col)].value for col in range(16)], sep='')


print(f'\nCalls to solve for backtracking = {calls_to_solve - 1}', file=sys.stderr, flush=True)
print(f'Cells resolved by identifying single candidate = {single_candidate_count}', file=sys.stderr, flush=True)
print(f'Cells resolved by identifying what I call "singletons" = {singleton_count}', file=sys.stderr, flush=True)
print(f'\n{int((time.time()-start)*1000)} ms', file=sys.stderr, flush=True)