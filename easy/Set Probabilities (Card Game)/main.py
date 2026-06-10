# https://www.codingame.com/ide/puzzle/set-probabilities-card-game

import sys,math

def is_set(c1, c2, c3):
    for i in range(4):
        if (c1[i] + c2[i] + c3[i]) % 3 != 0:
            return False
    return True

def get_needed_card(c1, c2):
    needed = []
    for i in range(4):
            # Die dritte Karte c3[i] muss (3 - (c1[i] + c2[i])) % 3 sein
        needed.append((3 - (c1[i] + c2[i]) % 3) % 3)
    return tuple(needed)

#######




n=2;input_data=['2 SOLID RED SQUIGGLE', '1 OUTLINED GREEN SQUIGGLE']

    


mappings = [
    {"1": 0, "2": 1, "3": 2},
    {"OUTLINED": 0, "STRIPED": 1, "SOLID": 2},
    {"RED": 0, "GREEN": 1, "PURPLE": 2},
    {"DIAMOND": 0, "OVAL": 1, "SQUIGGLE": 2}
    ]

table_cards = []
for i in range(n):
    features = input_data[i].split()
    card = tuple(mappings[j][features[j]] for j in range(4))
    table_cards.append(card)



    # 1. Prüfen, ob bereits ein Set auf dem Tisch liegt
found_existing_set = False
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if is_set(table_cards[i], table_cards[j], table_cards[k]):
                found_existing_set = True
                break
        if found_existing_set: break
    if found_existing_set: break

if found_existing_set:
    print("1.0000")
    exit(0)

    # 2. Wenn kein Set da ist, berechne fehlende Karten
needed_cards = set()
table_set = set(table_cards)
    
for i in range(n):
    for j in range(i + 1, n):
        needed = get_needed_card(table_cards[i], table_cards[j])
            # Die Karte darf nicht bereits auf dem Tisch liegen (sollte sie laut Logik eh nicht)
        if needed not in table_set:
            needed_cards.add(needed)

    # Wahrscheinlichkeit berechnen
remaining_in_deck = 81 - n
if remaining_in_deck <= 0:
    print("0.0000")
    exit(0)
else:
    prob = len(needed_cards) / remaining_in_deck
    print(f"{min(prob, 1.0):.4f}")


