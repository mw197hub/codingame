# https://www.codingame.com/ide/puzzle/timer-for-clash-of-code

import sys,math

timeList=['4:47'] #1
timeList=['3:55', '3:48'] #2
timeList=[] # 10

tList=[]
for p in range(len(timeList)):
    t = timeList[p]
    tL = t.split(':')
    sec = int(tL[0])*60 + int(tL[1])
    tList.append(sec)

stop_time = 0
in_clash = 0
cur_time = 300
for i in range(300,-1,-1):
    if i in tList:
        stop_time = i - 256/(2**in_clash)
        if stop_time < 0:
            stop_time = 0
        in_clash += 1
    if i == stop_time or in_clash == 7:
        cur_time = i
        break

if len(timeList) == 0:
        print("NO GAME")
else:
    divide = divmod(cur_time,60)
    print('{}:{}'.format(divide[0],str(divide[1]).zfill(2)))

