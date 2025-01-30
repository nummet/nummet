"""Denne implementeringa estimerar temperaturfordelinga for ei metall-
plate der kant-temperaturane er fikserte. Den gjer det ved å dele det inndre
av plata inn i eit rutenett og anta at kvar temperatur er gjennomsnittet av
nabo-temperaturane.
"""
 
# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Fontstorleik i plotta
plt.rcParams.update({'font.size': 15})

# Tilordnar koeffisientmatrisa og høgresida
A = np.array([[4, -1, -1, 0],
              [-1, 4, 0, -1],
              [-1, 0, 4, -1],
              [0, -1, -1, 4]])
b = np.array([40, 70, 30, 60])

# Inverterer og løyser likninga
Ainv = np.linalg.inv(A)
x = np.matmul(Ainv, b)

# Skriv svaret til skjerm
print(x)   

# Plottar temeperaturfordelinga
# Rutenett
xy_vektor = np.linspace(0, 1, 4)
[X, Y] = np.meshgrid(xy_vektor, xy_vektor)
# Matrise med temperaturar
Z = np.array([[20, 30, 30, 35],
             [10, x[0], x[1], 40],
             [10, x[2], x[3], 40],
             [15, 20, 20, 30]])

# Figur med flateplott
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
ax.plot_surface(X, Y, Z, cmap = cm.viridis)
ax.xaxis.set_inverted(True)             # Denne er neppe særleg intuitiv ...
ax.set_zlabel('Temperatur [$^\circ$C]') # Namn på z-akse
plt.show()