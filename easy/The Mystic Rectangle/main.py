import sys
import math

moveX = 0.3
moveY = 0.4
moveXY = 0.5

x, y = 50,15
u, v = 65,145

diffx = abs(x - u)
if diffx > 100:
    diffx = 200 - diffx
diffy = abs(y - v)
if diffy > 75:
    diffy = 150 - diffy

zw = diffx * moveXY
zw2 = abs(diffx - diffy) * moveY
if diffx > diffy:
    zw = diffy * moveXY
    zw2 = abs(diffx - diffy) * moveX
zw = zw + zw2
print("{0:.1f}".format(zw))