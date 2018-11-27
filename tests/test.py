
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 10000)
z = np.linspace(-2, 2, 10000)
r = z ** 2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
z = np.zeros((512, 512))
z[100, :] = 100
x = np.linspace(0, 512, 512)
y = np.linspace(0, 512, 512)
x, y = np.meshgrid(x, y)
# Plot the surface
ax.plot_surface(x, y, z, color='r')

plt.show()
