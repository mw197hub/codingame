# https://www.codingame.com/ide/puzzle/lines-intersections

import sys,math

def get_intersection(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2
    
    # Nenner der Determinante (Prüfung auf Parallelität/Identität)
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    if denom == 0:
        return None # Linien sind parallel oder identisch
    
    # Formel für den Schnittpunkt zweier Geraden
    intersect_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    intersect_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    
    # Runden auf 3 Dezimalstellen zur Vermeidung von Floating-Point-Ungenauigkeiten
    res_x = round(float(intersect_x), 3) + 0.0
    res_y = round(float(intersect_y), 3) + 0.0
    
    return (res_x, res_y)
    #return (round(float(intersect_x), 3), round(float(intersect_y), 3))


####
####

lines=[[-6, -5, 12, 12], [4, -44, 9, 19], [4, -44, 50, 19]] #1
lines=[[0, 0, 4, 0], [4, 0, 4, 4], [4, 4, 0, 4], [0, 4, 0, 0]] #4


intersections = set()

    # Alle Paare vergleichen
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        point = get_intersection(lines[i], lines[j])
        if point is not None:
            intersections.add(point)

    # Sortieren: primär nach x, sekundär nach y
sorted_points = sorted(list(intersections))

    # Ausgabe
print(len(sorted_points))
for x, y in sorted_points:
        # Formatierung auf exakt 3 Nachkommastellen
    print(f"{x:.3f} {y:.3f}")