import sys
import math

grafity = -3.711

class Point():
    x,y = 0,0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def update(ship,vec, rotate,power, fuel, inRotate, inPower):
   # grafity = 3.711
    deltaRotate = inRotate - rotate
    if deltaRotate > 15:
        rotate += 15
    elif deltaRotate < -15:
        rotate -= 15
    else:
        rotate = inRotate

    if fuel < inPower:
        inPower = fuel
    deltaPower = power - inPower
    if deltaPower < -1:
        power += 1
    elif deltaPower > 1:
        power -=1
    else:
        power = inPower
    fuel = fuel - power

    fRotation = -rotate / 180 * math.pi
    powerX = power * math.sin(fRotation)
    powerY = power * math.cos(fRotation)
    bewegung = Point(0,0)
    bewegung.x = powerX
    bewegung.y = grafity + int(powerY)
    vec.x = round(vec.x + bewegung.x)
    vec.y = round(vec.y + bewegung.y)
    ship.x += vec.x
    ship.y += vec.y

    return ship,fuel,rotate,vec,power

ziel = Point(1000,2100)
vec = Point(-50,0)
ship = Point(6500,2700)
rotate = 90
power = 0
fuel = 1000
inRotate = -5
inPower = 4

for i in range(6):
    inRotate = -5
    inPower = 4
    ship, fuel, rotate, vec, power= update(ship,vec, rotate,power, fuel, inRotate, inPower)

print("ship: " + str(ship.x) + " - " + str(ship.y))
print("Bewegung hs: " + str(vec.x) + "  vs: " + str(vec.y))
print(fuel)
print(rotate)
print(power)