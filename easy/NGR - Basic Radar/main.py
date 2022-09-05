import sys
import math

carDict = {'FH-790-HH': 615000, 'ET-318-NQ': 421000, 'BV-670-GV': 406000, 'DV-046-YY': 487000, 'FZ-792-EC': 349000, 'BP-301-UL': 624000, 'BV-047-TT': 437000, 'FT-918-CZ': 767000, 'DZ-507-JZ': 731000, 'DF-857-ZR': 437000}

carDict={}
n = int(input())
for i in range(n):
    inputs = input().split()
    plate = inputs[0]
    radarname = inputs[1]
    timestamp = int(inputs[2])
    if plate in carDict:
        geschwindigkeit =  int(13000 / (abs(carDict[plate] - timestamp) / 1000) * 3.6)
        if geschwindigkeit > 130:
            carDict[plate] = geschwindigkeit
        else:
            carDict.pop(plate)
    else:
        carDict[plate] = timestamp
print(carDict,file=sys.stderr)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for car,g in sorted(carDict.items()):
    print(car + " " + str(g))