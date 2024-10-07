# https://www.codingame.com/ide/puzzle/swatch-internet-time

import math,sys,string,time
from decimal import Decimal, ROUND_HALF_UP


rawtime="02:24:00 UTC+01:00"
rawtime="17:57:46 UTC-08:00"
rawtime="01:23:45 UTC+11:25"
rawtime="03:32:42 UTC-07:30"
rawtime="09:59:59 UTC-05:00"
rawtime="15:11:11 UTC-08:00"
rawtime="17:26:42 UTC+05:30"
###

hour=int(rawtime[0:2])
min=int(rawtime[3:5])
sec=int(rawtime[6:8])

utcHour=int(rawtime[13:15])
utcMin=int(rawtime[16:18])

if rawtime[12] == "+":
    hour = hour - utcHour +1
    min = min - utcMin
    if hour < 0:
        hour = 23 + hour
        if min < 0:
            min = 60 + min        
    elif min < 0:
        min = 60 + min
        hour = hour -1
else:
    hour = hour + utcHour +1
    if hour > 24:
        hour = hour -24
    min = min + utcMin
    if min > 60:
        min = min - 60
        hour = hour +1

erg=Decimal((3600*hour + 60*min + sec)/86.4)
erg = erg.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
if erg >= 1000:
    erg=erg-1000

print("@{:.2f}".format(erg))