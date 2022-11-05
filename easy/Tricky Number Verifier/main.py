#  https://www.codingame.com/training/easy/tricky-number-verifier

import sys,math,copy,string
from dateutil.parser import parse

def digit(zahl):
    summe = int(zahl[0]) * 3 + int(zahl[1]) * 7 + int(zahl[2]) * 9 + int(zahl[4]) * 5 + int(zahl[5]) * 8 + int(zahl[6]) * 4 + int(zahl[7]) * 2 + int(zahl[8]) * 1 + int(zahl[9]) * 6
    return summe % 11

nList=['1231210106', '5378241298', '3872231176']
#nList=['1234310406', '1334101308', '9873290202', '1334100008', '1334001298']
nList=['1230290204', '4543290205', '5555290200', '8035290200', '5555290201', '1457290220', '1003290208']

for n in nList:
    if len(n) == 10 and n.isdigit() and not n[0] == "0":                              
        try:
            jahrH = "20"
            if int(n[8:]) > 22:
                jahrh='19'
           # print(jahrH+n[8:]+"-"+n[6:8]+"-"+n[4:6])
            (parse(jahrH+n[8:]+"-"+n[6:8]+"-"+n[4:6]))
            d = digit(n)
            if str(d) == n[3]:
                print("OK")
            else:
                if d == 10:
                   # print(n[0:2]+str(int(n[2])+1)+n[4:])
                    wert = int(n[0:3]) +1
                    dNew = digit(str(wert)+'0'+n[4:])
                    print(str(wert)+str(dNew)+n[4:])
                else:
                    print(n[0:3]+str(d)+n[4:])
        except:
            print("INVALID DATE")                    
    else:
        print("INVALID SYNTAX")