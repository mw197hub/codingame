# https://www.codingame.com/ide/puzzle/find-the-winning-strategy

import sys,math



from typing import List, Tuple

def nim_sum(distances: List[int]) -> int:
    result = 0
    for d in distances:
        result ^= d
    return result

def best_move(distances: List[int]) -> Tuple[int, int]:
    """
    Liefert einen gültigen Zug:
    - Falls möglich: einen gewinnbringenden Zug (nim-summe -> 0).
    - Andernfalls: einen beliebigen legalen Zug (erste nicht-leere Reihe, -1).
    Rückgabe: (reihe_index, neuer_abstand) oder (-1, -1) wenn kein Zug möglich.
    """
    total = nim_sum(distances)
    # Gewinnzug falls möglich
    if total != 0:
        for i, d in enumerate(distances):
            target = d ^ total
            if target < d:
                return (i, target)
    # Keine Gewinnstrategie: trotzdem einen legalen Zug zurückgeben
    for i, d in enumerate(distances):
        if d > 0:
            return (i, d - 1)
    return (-1, -1)

def play_game(distances: List[int]):
    distances = distances[:]  # Kopie
    turn = 0  # 0 = du, 1 = Gegner
    print("Start:", distances, "Nim-Summe:", nim_sum(distances))
    while any(d > 0 for d in distances):
        row, new_d = best_move(distances)
        if row == -1:
            print(f"{'Du' if turn==0 else 'Gegner'} kann nicht ziehen.")
            break
        print(f"{'Du' if turn==0 else 'Gegner'}: Reihe {row} {distances[row]}→{new_d} (Nim vorher {nim_sum(distances)})")
        distances[row] = new_d
        print("  Neues Feld:", distances, "Nim:", nim_sum(distances))
        turn = 1 - turn
    print("Spielende. Gewinner:", "Du" if turn == 1 else "Gegner")


# Beispiel: 3 Reihen mit Abständen
if __name__ == "__main__":
    start = [1, 3,5,7,9]  # Abstände in den Reihen
    play_game(start)