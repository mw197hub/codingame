import sys,math

sensorList=[['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['0', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '0'], ['1', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '0'], ['1', '1', '0', '0'], ['1', '1', '0', '0'], ['1', '0', '1', '0'], ['1', '0', '1', '0'], ['1', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '0', '0', '1'], ['0', '0', '0', '1'], ['0', '1', '0', '1'], ['1', '1', '0', '0'], ['1', '1', '0', '0'], ['1', '1', '0', '0'], ['1', '1', '1', '0'], ['1', '0', '1', '1']]

#sensorList=[['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['0', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '0', '1', '1'], ['0', '0', '1', '0'], ['0', '0', '1', '1'], ['0', '1', '1', '1'], ['0', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '0', '1'], ['1', '1', '0', '0'], ['1', '0', '0', '0'], ['1', '0', '1', '0'], ['0', '0', '1', '0'], ['0', '0', '1', '1'], ['0', '1', '1', '1'], ['0', '1', '1', '1'], ['0', '0', '0', '1'], ['0', '0', '0', '1'], ['1', '0', '0', '0'], ['1', '1', '0', '0'], ['1', '1', '1', '0'], ['1', '1', '1', '0'], ['1', '1', '0', '0'], ['0', '1', '0', '0'], ['0', '0', '0', '1'], ['0', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '0', '1', '1'], ['1', '0', '1', '0'], ['1', '1', '0', '0'], ['1', '1', '0', '0'], ['1', '0', '0', '0'], ['1', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '1'], ['1', '0', '1', '1'], ['1', '0', '1', '1'], ['0', '0', '0', '1'], ['0', '0', '0', '1'], ['0', '1', '0', '0'], ['0', '1', '0', '0'], ['0', '1', '0', '1'], ['1', '1', '0', '1'], ['1', '1', '0', '0'], ['1', '0', '0', '0'], ['1', '0', '1', '0'], ['1', '0', '1', '0'], ['0', '0', '1', '0'], ['0', '0', '1', '1'], ['0', '0', '1', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '0'], ['1', '1', '0', '0'], ['1', '0', '0', '0'], ['1', '0', '1', '0'], ['1', '0', '1', '0'], ['1', '0', '1', '0'], ['0', '0', '1', '0'], ['0', '0', '1', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '1'], ['0', '1', '0', '0']]



ergList=[]
auto=0
left,right=-1,-1
for i in range(len(sensorList)):
    if left >= 0:
        if sensorList[i][3] == '0':
            auto = i - left + 1
            break
    if right >= 0:
        if sensorList[i][2] == '0':
            auto = i - right + 1
            break

    if sensorList[i][0] == '0' and left < 0:
        left=i
    if sensorList[i][1] == '0' and right < 0:        
        right=i
print(auto)

for i in range(len(sensorList)-auto+1):
    links=0;rechts=0
    for j in range(auto):
        if sensorList[i+j][0] == '0': # and sensorList[i+j][3] == '0':
            links+=1
        if sensorList[i+j][1] == '0': # and sensorList[i+j][2] == '0':
            rechts+=1
    if links == auto:
        ergList.append(str(i+auto+auto-2)+"L")
    if rechts == auto:
        ergList.append(str(i+auto+auto-2)+"R")

for erg in ergList:
    print(erg)
