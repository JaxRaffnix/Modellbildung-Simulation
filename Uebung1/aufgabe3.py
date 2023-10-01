from matplotlib import pyplot as plt
from math import pi 
import numpy as np

x_axis = np.linspace(-pi/2, 5/2*pi, 100)
sin = np.sin(x_axis)

plt.plot(x_axis, sin)

ax = plt.gca()
ax.grid(True)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))

plt.title("Zweidimensionale Funktionen")
plt.xlabel("$y_1$")
plt.ylabel("Ordinate")
plt.show()
