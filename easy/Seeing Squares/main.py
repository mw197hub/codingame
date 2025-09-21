#https://www.codingame.com/ide/puzzle/seeing-squares

import sys,math

yMax=3;xMax=5;rowList=[['+', '-', '-', '-', '+'], ['|', ' ', ' ', ' ', '|'], ['+', '-', '-', '-', '+']]  #1
yMax=3;xMax=9;rowList=[['+', '-', '-', '-', '+', '-', '-', '-', '+'], ['|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'], ['+', '-', '-', '-', '+', '-', '-', '-', '+']] #2
yMax=15;xMax=11;rowList=[['+', '-', '+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['+', '-', '+', '-', '+', '-', '+', ' ', ' ', ' ', ' '], [' ', ' ', '+', '-', '+', ' ', '+', '-', '-', '-', '+'], [' ', ' ', '+', '-', '-', '-', '+', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', '+', '+', '+', '-', '-', '+'], [' ', ' ', ' ', ' ', '+', '+', '+', '+', ' ', ' ', ' '], [' ', ' ', '+', '-', '+', '-', '+', ' ', ' ', ' ', ' '], [' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' '], ['+', '-', '+', '-', '+', '-', '+', ' ', ' ', ' ', ' '], ['|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' '], ['+', '+', '-', '-', '+', '-', '-', '-', '-', '+', ' '], [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '], [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '], [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '], [' ', '+', '-', '-', '-', '-', '-', '-', '-', '+', ' ']] #13

yMax=38;xMax=33;rowList=[] #14
datei = open('C:\\Users\\marku\\Python\\codingame\\easy\\Seeing Squares\\input.txt','r', encoding='utf-8')

yMax=98;xMax=97;rowList=[] #14
datei = open('C:\\Users\\marku\\Python\\codingame\\easy\\Seeing Squares\\input2.txt','r', encoding='utf-8')

for zeile in datei:
    rL=[]
    for r in zeile:
        rL.append(r)
    rowList.append(rL[:])

    

anzahl=0
for y in range(len(rowList)):
    for x in range(len(rowList[0])):
        if rowList[y][x] == "+" and y < len(rowList) -1:
            lList,hList=[],[]
            for x1 in range(x+1,xMax):
                if rowList[y][x1] == " " or rowList[y][x1] == "|":
                    break
                if rowList[y][x1] == "+":
                    if x1 - x >= 2 and (x1-x)//2 == (x1-x)/2:
                        for y1 in range(y+1,yMax):
                            if rowList[y1][x] == " " or rowList[y1][x1] == " " or rowList[y1][x] == "-" or rowList[y1][x1] == "-":
                                break
                            if rowList[y1][x] == "+" and rowList[y1][x1] == "+":
                                ende=True
                                for x2 in range(x+1,x1):
                                    if rowList[y1][x2] == " " or rowList[y1][x2] == "|":
                                        ende=False;break
                                if ((y1 - y+1)-2)*2+1 == (x1-x+1)-2 and ende:
                                    anzahl+=1
                               #     print("{},{} # {},{}".format(y,x,y1,x1),file=sys.stderr)
                               #     for yA in range(y,y1+1):
                               #         for xA in range(x,x1+1):
                               #             print(rowList[yA][xA],end="")
                               #         print("")

print(anzahl)
