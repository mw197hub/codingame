import sys
import math
import random
from typing import NoReturn

class dna():
    nr = 0
    wert = 0
    def __init__(self,nr,wert):
        self.nr = nr
        self.wert = wert

dnaList = {}

for i in range(10):
    n = random.randint(0,100)
    dnaList[i] = dna(i,n)

for nr in reversed(sorted(dnaList,key = lambda nr: dnaList[nr].wert)):
    dnaO = dnaList[nr]
    print(str(nr) + "   wert: " + str(dnaO.wert))


'''
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


studi1 = Student('john', 'A', 15)
studi2 = Student('dave', 'B', 99)
studi3 = Student('jane', 'B', 12)

student_Dict = {}
student_Dict[studi1.name] = studi1
student_Dict[studi2.name] = studi2
student_Dict[studi3.name] = studi3

for key in sorted(student_Dict, key = lambda name: student_Dict[name].age):
    print(key)
'''