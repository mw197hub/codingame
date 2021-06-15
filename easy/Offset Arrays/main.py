import sys
import math

n = 3


#x = "A[CC[-2]]"
#lineList = ["A[-1..1] = 1 2 3", 'B[3..7] = 3 4 5 6 7', 'CC[-2..1] = 1 2 3 4']

x = "ARR[-4]"
lineList = ["ARR[-5..-3] = 11 22 33"]

sucheList = {}

for line in lineList:
    name = line[:line.find('[')]
    start = line[line.find('[')+1:line.find('.')]
    ende = line[line.find('..') +2:line.find(']')]
    #print(name + " " + start + " " + ende,file=sys.stderr)
    posList = {}
    numList = line[line.find('=')+2:].split(' ')
    pos = 0
    for i in range(int(start),int(ende)+1):
        posList[i] = int(numList[pos])
        pos += 1
    sucheList[name] = posList
print(sucheList,file=sys.stderr)

erg = 9999999
nameList = x.split("[")
nameList.pop()

pos = x.find(']')
while True:
    pos -= 1
    if x[pos] == "[":
        break

while True:
    if erg == 9999999:
        wert = x[pos+1:x.find(']')]
    else:
        wert = erg
    name = nameList.pop()
    buchList = sucheList[name]
    erg = buchList[int(wert)]
    pos = pos - len(name) -1
    if pos <= 0:
        break

print(str(erg))