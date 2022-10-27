import sys
import math

packet='101001010'
packet='100100111100001001001011001010100111011110011110101100011100011'
packet='10100010101001011'

lengthDict={'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':10,'1011':11,'1100':12,'1101':13,'1111':14}

pos=0;start=False
while pos < len(packet):
    id = packet[pos:pos+3]
    pos+=3
    length = packet[pos:pos+4]
    pos+=4
    l = lengthDict[length]
    inhalt= packet[pos:pos+l]
    pos+=l
    if id == "101":
        start=True
        print('001'+length+inhalt,end="")
    #elif start:
    #    print('001'+length+inhalt,end="")
print("")

print(int('1011',2)) # 2er Basis