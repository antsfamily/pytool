
import pytool
import numpy as np
from matplotlib import pyplot as plt

PI = 3.1415926
f = 500
N = 512
M = 256
t = np.linspace(0, 4, N)

x = np.sin(2*PI*f*t)
N = len(x)
y = np.fft.fft(x)
# print(x)

A = np.zeros((M, N))
for i in range(0, M, 1):
	# A[i, :] = x
	A[i, :] = x + i/512
	# A[i, :] = x*2

B = np.fft.fft2(A)

plt.figure()
plt.subplot(121)
plt.plot(x, '-r')
plt.subplot(122)
plt.plot(np.abs(y), '-b')

pytool.mesh(A)
# pytool.mesh(np.abs(B))

plt.show()


