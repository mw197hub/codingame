# https://www.codingame.com/ide/puzzle/nd-vector-sorting

import sys,math
import operator



coordList={1: [1, 0], 2: [0, 1]}  #1
coordList={1: [533897480, -613226257, 342166228], 2: [533897480, 254786100, 414564234], 3: [533897480, 254786100, -228769559], 4: [533897480, 254786100, 330086295], 5: [533897480, -426805636, -228141293], 6: [533897480, -805442806, -135129331]}  #2


erg=""
sorted_x = sorted(coordList.items(), key=operator.itemgetter(1))
for s in sorted_x:
    erg=erg+ str(s[0]) + " "
print(erg[:-1])