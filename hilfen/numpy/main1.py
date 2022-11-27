import numpy as np
from numpy import pi
import sys, math
import matplotlib.pyplot as plt


a = np.arange(15).reshape(3, 5)
#print(a.ndim)

b = np.array([(1.5, 2, 3), (4, 5, 6)])
#print(b.dtype)
b = np.zeros((2,3), dtype=np.int64)
#print(b)
b= np.arange(10, 30, 5)
#print(b)

a=np.linspace(0, 2, 12)
#print(a)
x = np.linspace(0, 2 * pi, 100) 
f=np.sin(x)
#print(f)

#   np.set_printoptions(threshold=sys.maxsize

a = np.array([20, 30, 40, 50])
#if a.any()<35:
    #print("a")

rg = np.random.default_rng(1)
a = rg.random((2, 3))
#print(a[0][0])

a = np.arange(10)**2
#print(a)

a = np.arange(12).reshape(3, 4)
b = a > 4
#print(b.base is a)
#print(a[b])

