import sys
import math

n = 8
datei = "C:\\Users\\wiedm\\Python\\codingame\\easy\\if then else\\input1.txt"
# 4

n = 11
datei = "C:\\Users\\wiedm\\Python\\codingame\\easy\\if then else\\input2.txt"
# 3

n = 30
datei = "C:\\Users\\wiedm\\Python\\codingame\\easy\\if then else\\input4.txt"
# 13

befehle = ["if","else","endif","end"]
inputList = []
ergList = []
ebene = 0
ergStr = ""
f = open(datei, "r")
for x in f:
    if len(x) > 0:
        inputList.append(x[:-1])
print(inputList,file=sys.stderr)

for z in inputList:
    if z in befehle:
        ergList.append(z)
ergList.append("")
inputList.clear()
for i in range(len(ergList)-1):
    inputList.append(ergList[i]+ergList[i+1])

print(inputList,file=sys.stderr)

for z in inputList:
    if z == "ifelse":
        ergStr += "( 1 + "
    if z == "elseendif":
        ergStr += "1 )"
    if z == "endifif":
        ergStr += " * "
    if z == "endifendif":
        ergStr += ")"
    if z == "ifif":
        ergStr += "("
  #  if z == "elseif":
  #      ergStr += "?1"
    if z == "endifelse":
        ergStr += "+"



ergStr = ergStr[:]

if len(ergStr) == 0:
    print("1")
else:
    print(ergStr,file=sys.stderr)
    print(eval(ergStr))