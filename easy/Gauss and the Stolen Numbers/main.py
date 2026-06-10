# https://www.codingame.com/ide/puzzle/gauss-and-the-stolen-numbers

import sys,math

import sys
import math

def solve(N,S,Q):
    
    # 1. Berechne die theoretische Gesamtsumme aller Zahlen von 1 bis N
    total_sum = N * (N + 1) // 2
    
    # 2. Berechne die theoretische Gesamtsumme der Quadrate von 1 bis N
    total_squares = N * (N + 1) * (2 * N + 1) // 6
    
    # 3. Bestimme die Summe (A) und die Quadratsumme (B) der zwei fehlenden Zahlen
    A = total_sum - S          # x + y = A
    B = total_squares - Q      # x^2 + y^2 = B
    
    # 4. Nutze die binomische Formel, um das Produkt (P) der Zahlen zu bestimmen:
    # (x + y)^2 = x^2 + 2xy + y^2  =>  A^2 = B + 2P  =>  P = (A^2 - B) / 2
    P = (A**2 - B) // 2        # x * y = P
    
    # 5. Löse die quadratische Gleichung t^2 - A*t + P = 0
    # Die Diskriminante ist D = A^2 - 4*P
    D = A**2 - 4 * P
    sqrt_D = math.isqrt(D)     # Ganzzahlige Quadratwurzel
    
    # Die beiden Nullstellen sind die gesuchten Zahlen
    x = (A - sqrt_D) // 2
    y = (A + sqrt_D) // 2
    
    # Ausgabe in aufsteigender Reihenfolge
    print(f"{x} {y}")

if __name__ == '__main__':
    solve(10,44,312)
