import sys 
import math
import statistics


erg,sumX,sumY=0,3,3
xyList = [[0, 0], [1, 1], [2, 2]]

erg,sumX,sumY=0,1970420718,876391419   # 6  erg = 6066790161
xyList = [[-28189131, 593661218], [102460950, 1038903636], [938059973, -816049599], [-334087877, -290840615], [842560881, -116496866], [-416604701, 690825290], [19715507, 470868309], [846505116, -694479954]]
xList = [-416604701, -334087877, -28189131, 19715507, 102460950, 842560881, 846505116, 938059973]
yList = [-816049599, -694479954, -290840615, -116496866, 470868309, 593661218, 690825290, 1038903636]

xyList = sorted(xyList, key=lambda x: [x[0],x[1]])
print(xyList)
print(sorted(xList))
print(sorted(yList))

medianX = int(statistics.median(xList))
medianY = int(statistics.median(yList))
print("median: " + str(medianX)+ " - " + str(medianY),file=sys.stderr)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("x-laenge: " + str(xyList[len(xyList)-1][0])+ " bis " + str(xyList[0][0]),file=sys.stderr)
erg = xyList[len(xyList)-1][0] - xyList[0][0]

for xy in xyList:
   # erg += abs(xy[0]-startX)
    erg += abs(xy[1]-medianY)

print(str(erg))




