#https://www.codingame.com/ide/puzzle/the-experience-for-creating-puzzles

import sys,math

level=10;xp=300;n=1 #1
level=1;xp=10;n=5 #2

wert=0
punkte=xp-(300*n)
while punkte <= 0:
    level+=1
    punkte+=int(level*math.sqrt(level)*10)

    
print(level)
print(int(punkte))

