import sys
import math


landList = []
x,hSpeed,vSpeed,outputAngle,outputThrust = 0,0,0,0,0
flat = [0,0,0]

maxHorizontalSpeed = 100
desiredSpeedWhenNear = 20
farDistance = 2000
distanceX, isFar, isOverLandingArea  = 0,0,0
desiredDirection, currentDirection,isMovingToDesiredDirection,isMovingUp  = 0,0,0,0
desiredInitialSpeed = 0

def getDistanceX():
    return abs(flat[1] - x)
def getIsFar():
    print(str(distanceX),file=sys.stderr)
    if distanceX > farDistance:
        return True
    return False
def getIsOverLandingArea():
    if x >= flat[0] and x <= flat[2]:
        return True
    return False
def getSign(wert1):
    if wert1 == 0:
        return 0
    elif wert1 > 0:
        return 1
    return -1
def getIsMovingToDesiredDirection():
    if desiredDirection == currentDirection:
        return True
    return False
def getIsMovingUp():
    if vSpeed > 0:
        return True
    return False 
def GetDesiredAngle(desiredSpeedX,maxAngle):
    desiredVelocity = desiredSpeedX * desiredDirection
    desiredAcceleration = desiredVelocity - hSpeed
    return -max(-maxAngle, min(maxAngle, desiredAcceleration * 2))

n = int(input())  
for i in range(n):
    land_x, land_y = [int(j) for j in input().split()]
    landList.append([land_x,land_y])

for i in range(len(landList)-1):
        if landList[i][1] == landList[i+1][1]:
            flat[0] = landList[i][0]
            flat[2] = landList[i+1][0]
            flat[1] = (flat[0] + flat[2]) / 2
runde = 0
while True:
    x, y, hSpeed, vSpeed, f, r, p = [int(i) for i in input().split()]
    distanceX = getDistanceX()
    isFar = getIsFar()
    isOverLandingArea = getIsOverLandingArea()
    desiredDirection = getSign(flat[1] - x)
    currentDirection = getSign(hSpeed)
    isMovingToDesiredDirection = getIsMovingToDesiredDirection()
    isMovingUp = getIsMovingUp()
    
    if runde == 0:
        if isMovingToDesiredDirection:
            desiredInitialSpeed = abs(hSpeed)
        else:
            desiredInitialSpeed = maxHorizontalSpeed
        print("0 0")
    else:
        outputThrust = 4
        if isOverLandingArea:
            if abs(vSpeed) < 40 and hSpeed == 0:
                outputThrust = 3
            outputAngle = GetDesiredAngle(0,33)
        else:
            if isMovingUp:
                outputThrust = 3
            if isFar:
                outputAngle = GetDesiredAngle(desiredInitialSpeed,61)
            else:
                outputAngle = GetDesiredAngle(desiredSpeedWhenNear,45)
        print(str(outputAngle)+" " + str(outputThrust))
    print(str(isFar) + " - " + str(isOverLandingArea) + " - " + str(isMovingToDesiredDirection),file=sys.stderr)
    runde += 1