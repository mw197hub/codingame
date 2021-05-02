import sys
import math

ergList = []
n = 5
nList = ['A', 'CBACBACBACBACBACBA', 'CCCCCBBBBBAAAAA', 'BDNIDPD', 'CODINGAME']
#nList = ['CCCCCBBBBBAAAAA']
# 1 3 1 4 4
 
nList = ['C', 'JS', 'VB', 'CPP', 'PHP', 'JAVA', 'PERL', 'RUBY', 'MYSQL', 'PYTHON', 'GROOVY', 'PASCAL', 'POSTGRES', 'HIBERNATE', 'KUBERNETES']
nList = ["POSTGRES"]
# 1 2 1 2 2 2 2 3 2 2 4 3 3 4 4 
for l in nList:
    stackList = []
    for z in l:
        treffer = True
        stackList.sort()
        for i in range(len(stackList)):
            if z <= stackList[i]:
                stackList.remove(stackList[i])
                stackList.append(z)
                treffer = False
                break
        if treffer:
            stackList.append(z)
    
    #print("----",file=sys.stderr)
    #print(str(len(stackList)))
    print(stackList)
    ergList.append(len(stackList))
print(ergList)