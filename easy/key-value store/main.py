# https://www.codingame.com/ide/puzzle/key-value-store

import sys,math

sList=['SET os-name=windows', 'SET os-arch=x64', 'GET os-name os-arch']
sList=['KEYS','SET e=e','SET m=m','SET a=a ','SET g=g','SET -=-'  ,'SET n=n'  ,'SET i=i'  ,'SET d=d'  ,'SET o=o'  ,'SET c=c '  ,'GET e m a g - n i d o c']

varDict={};erg="";keyList=[]
for s in sList:
    befehle=s.split(" ")
    if befehle[0] == "GET":
        for b in befehle[1:]:
            if b in varDict:
                erg+=varDict[b]+" "
            else:
                erg+="null "
        print(erg[:-1]);erg=""
    if befehle[0] == "EXISTS":
        for b in befehle[1:]:
            if b in varDict:
                erg+="true "
            else:
                erg+="false "
        print(erg[:-1]);erg=""
    if befehle[0] == "KEYS":
        if len(keyList) == 0:
            print("EMPTY")
        else:
            for k in keyList:
                erg+=k+" "
            print(erg[:-1]);erg=""
    if befehle[0] == "SET":
        for b in befehle[1:]:
            t = b.split("=")
            if len(t) > 1:
                if not t[0] in keyList:
                    keyList.append(t[0])
                varDict[t[0]] = t[1]
