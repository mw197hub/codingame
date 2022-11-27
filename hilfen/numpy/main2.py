import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(h, w, maxit=20, r=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime

plt.clf()
#plt.imshow(mandelbrot(400, 400))
#plt.show()

x = np.arange(0, 10, 2)
y = np.arange(5)
m = np.vstack([x,y])
xy = np.hstack([x,y])
v = np.stack([x,y])
#print(x)
#plt.plot(x,y)
#plt.show()

#np.save('filename', a)
#b = np.load('filename.npy')
# np.savetxt('new_file.csv', csv_arr)
# np.loadtxt('new_file.csv')




