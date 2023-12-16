# https://www.codingame.com/ide/puzzle/reverse-polish-notation

import sys,math

instrList=['1', '3', 'ADD']  # 1
instrList=['2', '4', 'ADD', '5', 'MUL', '-4'] # 2
instrList=['2', '5', '7', '6', 'SWP'] # 3
instrList=['4', 'ADD'] # 4
instrList=['1', '2', '3', '4', '3', 'ROL'] # 5
instrList=['1', '0', 'DIV']  # 6
instrList=['1', '1', '0', 'DIV'] # 7

instrList=['-3','6','5','MUL','ADD','6','SUB','3','DIV']  # 2 vali
instrList="-4 7 10 6 3 ROL 4 SWP DUP".split(" ")  # 3 vali
instrList="1 SUB".split(" ") # 4 vali

befList=['ADD','SUB','MUL','MOD','DIV','POP','DUP','SWP','ROL']
ergList=[]
fehler=False
for i in range(len(instrList)):
    if instrList[i] in befList:
        if instrList[i] == "DUP":
            if len(ergList) >= 1:                       
                ergList.append(ergList[-1])
            else:       
                ergList.pop()
                fehler=True;break
        if instrList[i] == "POP":
            if len(ergList) >= 1:
                ergList.pop()           
            else:  
                ergList.pop()
                fehler=True;break
        if instrList[i] == "MOD" and ergList[-1] > 0:
            if len(ergList) >= 2:
                summe = ergList[-1] % ergList[-2]
                ergList.pop()           
                ergList.pop()
                ergList.append(summe)
            else:
                ergList.pop()           
                ergList.pop()
                fehler=True;break
        if instrList[i] == "ADD":
            if len(ergList) >= 2:
                summe = ergList[-1] + ergList[-2]
                ergList.pop()           
                ergList.pop()
                ergList.append(summe)
            else:
                ergList.pop()           
                ergList.pop()
                fehler=True;break
        if instrList[i] == "SUB":
            if len(ergList) >= 2:
                summe = ergList[-2] - ergList[-1]
                ergList.pop()           
                ergList.pop()
                ergList.append(summe)
            else:
                ergList.pop()           
                fehler=True;break
        if instrList[i] == "MUL":
            if len(ergList) >= 2:
                summe = ergList[-1] * ergList[-2]
                ergList.pop()           
                ergList.pop()
                ergList.append(summe)
            else:
                ergList.pop()           
                ergList.pop()
                fehler=True;break
        if instrList[i] == "DIV":
            if len(ergList) >= 2 and ergList[-1] > 0:
                summe = int(ergList[-2] / ergList[-1])
                ergList.pop()           
                ergList.pop()
                ergList.append(summe)
            else:
                ergList.pop()           
                ergList.pop()
                fehler=True;break            
        if instrList[i] == "SWP":
            if len(ergList) >= 2:
                w1=ergList.pop()
                w2=ergList.pop()
                ergList.append(w1)
                ergList.append(w2)
            else:
                ergList.pop()           
                ergList.pop()
                fehler=True;break
        if instrList[i] == "ROL":            
            if len(ergList) >= 1:
                anz = ergList.pop()
                if len(ergList) >= anz:
                    w = ergList.pop(-anz)
                    ergList.append(w)
                else:        
                    ergList.pop()
                    fehler=True;break
            else:
                ergList.pop()           
                ergList.pop()
                fehler=True;break
    else:
        ergList.append(int(instrList[i]))

    print(ergList,file=sys.stderr)

if fehler:
    erg=""
    for e in ergList:
        erg += str(e)+" "
    print(erg + "ERROR")
else:
    erg=""
    for e in ergList:
        erg += str(e)+" "
    print(erg[:-1])
