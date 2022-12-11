import sys,math
import matplotlib.pyplot as plt
import numpy as np

def funktion(x):
    return x**3 - x - 2

a,b=1,2
diff=0.0001
erg=a+b
anz = 0

#while abs(erg) > diff:
while not abs(erg) == 0:
    anz+=1
    c = (a + b) / 2
    erg = funktion(c)
    print('{}   a: {}  b: {}  c: {}  f: {}'.format(anz,a,b,c,erg))
    if erg < 0:
        a = c
    else:
        b = c

#x = np.arange(-10, 10, 1)
#y = np.zeros(len(x))
#for i in range(len(x)):
#    y.put(i) = funktion(x)
x,y = [],[]
for i in range(-1000,1001,1):
    x.append(i/100)
    y.append(funktion(i/100))
plt.clf()
plt.plot(x,y)
plt.show()