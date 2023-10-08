# https://ide.codingame.com/21609455?id=67159074dfed33eeaec99fa6e7420adaa0162c2

from json import dumps, loads
from typing import List
import sys,math


mutant_scores={'Quicksnail': 140, 'Meowverine': 246, 'Magnetoast': 157, 'Captain Confetti': 87, 'Backstreet Boy': 228};threshold=200

for mutant in sorted(mutant_scores.items(), key=lambda item: item[1],reverse=True):
    name=mutant[0];wert=mutant[1]
    if wert <= threshold:
        print(name)
        break
