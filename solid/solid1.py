import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define os pontos do aerofólio
x = np.array([1.0, 0.9, 0.8, 0.6, 0.4, 0.2, 0.0])
y = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0])
z = np.array([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3])

# Cria a figura e os eixos 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a superfície
X, Y = np.meshgrid(x, y)
Z = np.outer(z, np.ones_like(x))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')

# Define os labels dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostra o plot
plt.show()
