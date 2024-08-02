"""
Dette skriptet plottar ei flate i rommet.
Funksjonsuttrykket og grensene for x og y er hardkoda i 
starten av skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm

# Funksjon som vi vil plotte
def funk(x,y):
#    return np.cos(x**2 + 0.5*y**2)*np.exp(-(x-1)**2-(y-2)**2)
    return 1/(x**2-x*y+2*y**2+x+y+1)

# Grenser for x og y (hardkoda)
xMin = -1
xMax = 0
yMin = -1
yMax = 0

# Vektorar og matriser med funksjonsverdiar 
# 200 punkt både for x og y
x = np.linspace(xMin, xMax, 200)
y = np.linspace(yMin, yMax, 200)
X, Y = np.meshgrid(x, y)

# Matrise med z-verdiar
Z = funk(X, Y)

# Figur med flateplott
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
ax.plot_surface(X, Y, Z, cmap = cm.summer)
ax.set_xlabel('x', fontsize = 15)
ax.set_ylabel('y', fontsize = 15)
ax.set_zlabel('z', fontsize = 15)
plt.show()