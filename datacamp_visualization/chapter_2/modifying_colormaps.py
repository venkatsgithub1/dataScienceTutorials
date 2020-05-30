import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

X, Y = np.meshgrid(u, v)

Z = np.sin(3*np.sqrt(X**2+Y**2))

plt.subplot(2, 2, 1)
plt.contourf(X, Y, Z, 20, cmap="viridis")

plt.subplot(2, 2, 2)
plt.contourf(X, Y, Z, 20, cmap="gray")

plt.subplot(2, 2, 3)
plt.contourf(X, Y, Z, 20, cmap="autumn")

plt.subplot(2, 2, 4)
plt.contourf(X, Y, Z, 20, cmap="winter")

plt.tight_layout()

plt.show()
