# https://www.codingame.com/ide/puzzle/leap-of-sheep

import sys,math

import sys

def solve(N,heights):
    
    # Precomputing: Das Minimum auf der rechten Seite für jede Position
    # right_min[j] wird das absolute Minimum aller Elemente rechts von j sein
    right_min = [float('inf')] * N
    current_min = float('inf')
    for k in range(N - 1, -1, -1):
        right_min[k] = current_min
        if heights[k] < current_min:
            current_min = heights[k]
            
    max_difficulty = -1
    left_min = float('inf')
    
    # Wir iterieren über alle möglichen mittleren Hügel j
    # Ein gültiger mittlerer Hügel kann nicht der erste (0) oder letzte (N-1) sein
    for j in range(1, N - 1):
        # Aktualisiere das absolute Minimum aller Elemente links von j
        if heights[j-1] < left_min:
            left_min = heights[j-1]
            
        hj = heights[j]
        
        # Ein gültiger Sprung ist nur möglich, wenn der aktuelle Hügel hj
        # strikt größer ist als das jeweils kleinste Element links und rechts
        if hj > left_min and hj > right_min[j]:
            difficulty = 2 * hj - left_min - right_min[j]
            if difficulty > max_difficulty:
                max_difficulty = difficulty
                
    # Ausgabe der maximalen Schwierigkeit
    print(max_difficulty)

if __name__ == '__main__':
    solve(5,[3,5,4,6,1])
