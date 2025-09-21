#https://www.codingame.com/ide/puzzle/grandmas-serial-keys

import sys,math

username="johndoe"  #1
username="I_L_I_K_E_C_O_D_I_N_G"
username="MWWWWWWWWWWWWWWWWWWWWWWWWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAAHHHHAAAAAAAAHHHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAAHHHHAAAAAAAAHHHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAAHHHHAAAAAAAA"




############

wert=0;seed=""
for b in username:
    wert+=ord(b)
wert= wert * len(username)
seed =str(wert^20480)

wert=0;seed=""
for b in username:
    wert+=ord(b)
wert= wert * len(username)
seed =str(wert^20480)

s1,s2,s3,s4="","","",""
s1=int(seed)&65535
s2=int(seed)>>16
s3=(ord(username[0])+ord(username[-1]))*len(username)
s4=int(s1)+int(s2)+int(s3)
s4=s4%65536
s1=f'{int(s1):x}'
s2=f'{int(s2):x}'
s3=f'{int(s3):x}'
s4=f'{int(s4):x}'

print("{}-{}-{}-{}".format(s1.rjust(4,'0').upper(),s2.rjust(4,'0').upper(),s3.rjust(4,'0').upper(),s4.rjust(4,'0')).upper())
