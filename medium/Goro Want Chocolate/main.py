# https://www.codingame.com/ide/puzzle/goro-want-chocolate

import sys,math
sys.setrecursionlimit(2000)

def solve_iterative(h: int, w: int) -> int:
    # DP-Tabelle: dp[a][b] = minimale Anzahl Quadrate für ein a x b Rechteck
    dp = [[0] * (w + 1) for _ in range(h + 1)]

    for a in range(1, h + 1):
        for b in range(1, w + 1):
            if a == b:
                dp[a][b] = 1
            else:
                # Startwert: schlechtester Fall = lauter 1x1-Quadrate
                best = a * b

                # vertikale Schnitte
                for c in range(1, b // 2 + 1):
                    best = min(best, dp[a][c] + dp[a][b - c])

                # horizontale Schnitte
                for c in range(1, a // 2 + 1):
                    best = min(best, dp[c][b] + dp[a - c][b])

                dp[a][b] = best

    return dp[h][w]

h=3;w=5 #1 4
h=51;w=13 #2 10

print(solve_iterative(h, w))