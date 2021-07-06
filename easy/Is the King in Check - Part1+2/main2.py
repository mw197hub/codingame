import sys
import math

def pruefeR(king,posF):
    if king[0] == posF[0] or king[1] == posF[1]:
        return True
    return False

def pruefeB(king,posF):
    x = king[0] - posF[0]
    y = king[1] - posF[1]
    if abs(x) == abs(y):
        return True
    return False

def pruefeN(king,posF):
    x = king[0] - posF[0]
    y = king[1] - posF[1]
    if abs(x) == 2 and abs(y) == 1:
        return True
    if abs(x) == 1 and abs(y) == 2:
        return True
    return False

def pruefeQ(king,posF):
    if king[0] == posF[0] or king[1] == posF[1]:
        return True
    x = king[0] - posF[0]
    y = king[1] - posF[1]
    if abs(x) == abs(y):
        return True
    return False