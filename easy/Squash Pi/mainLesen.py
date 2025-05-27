import sys,math,decimal
from decimal import Decimal, getcontext
import zlib

getcontext().prec = 300000 + 10


#datei = open('C:\Users\marku\Python\codingame\easy\Squash Pi\Pi','r')
datei = open("Pi",'r')

zahlPi=0
for zeile in datei:
	
	zahlPi = int(zeile[0]+zeile[2:])

#number = zahlPi
#hex_value = hex(number)
#print(hex_value)
#datei = open('HexPi', 'w')
#datei.write(str(hex_value))

#zahlZip = zlib.compress(bytes(str(zahlPi),'UTF-8'))
#datei = open('ZipPi', 'w')
#datei.write(str(zahlZip))
#print(zahlZip)