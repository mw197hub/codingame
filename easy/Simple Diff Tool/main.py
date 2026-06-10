# https://www.codingame.com/ide/puzzle/simple-diff-tool

import sys,math

#1
art="BY_CONTENT";oriList=['CodinGame is a fun website to learn programming skills.', 'It supports a large set of programming languages.', 'The progression path is divided in four parts: development speed, algorithms, optimisation and artificial intelligence.'];newList=['CodinGame is a fun website to learn programming skills.', 'It supports a large set of programming languages.', 'The progression path is divided in four parts: development speed, algorithms, optimisation and artificial intelligence.', 'Some experience points are awarded on tasks achievement']
#2
art="BY_NUMBER";oriList=['CodinGame is a fun website to learn programming skills.', 'It supports a large set of programming languages.', 'The progression path is divided in four parts: development speed, algorithms, optimisation and artificial intelligence.'];newList=['CodinGame is a fun website to learn programming skills.', 'It supports a large set of programming languages.', 'Some experience points are awarded on tasks achievement', 'The progression path is divided in four parts: development speed, algorithms, optimisation and artificial intelligence.']

#4
art="BY_NUMBER";oriList=['CodinGame is a fun website to learn programming skills.', 'It supports a large set of programming languages.', 'The progression path is divided in four parts: development speed, algorithms, optimisation and artificial intelligence.'];newList=['CodinGame is a fun website to learn programming skills.', 'The progression path is divided in four parts: development speed, algorithms, optimisation and artificial intelligence.']

# in java geklaut


ausgabe="No Diffs"

if art == "BY_CONTENT":
    for i in range(len(oriList)):
        ori = oriList[i]
        if ori in newList:
            for k in range(len(newList)):
                new = newList[k]
                if new == ori:
                    if not i == k:
                        print("MOVE: " + ori+ " @: " + str(i)+" >>> @: "+str(k))
        else:
            print("DELETE: "+ori)
    for i in range(len(newList)):
        new = newList[i]
        if not new in oriList:
            print("ADD: "+new)
else:
    for i in range(len(oriList)):   
        ori = oriList[i]
        if i < len(newList):
            new = newList[i]
            if not ori == new:
                print("CHANGE: "+ori+" ---> "+new)
    for i in range(len(oriList)):
        ori = oriList[i]
        if not ori in newList:
            print("DELETE: "+ori)        
    for i in range(len(newList)):
        new = newList[i]
        if not new in oriList:
            print("ADD: "+new)        


