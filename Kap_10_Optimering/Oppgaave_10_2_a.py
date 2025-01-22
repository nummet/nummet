"""
Dette skriptet plottar ein funksjon av to variable som eit fargekart.
Funksjonsuttrykket og grensene for x og y er hardkoda i 
starten av skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 

# Funksjon som vi vil plotte
def funk(x,y):
    return 1/(x**2-x*y+2*y**2+x+y+1)

# Grenser for x og y (hardkoda)
xMin = -3
xMax = 1
yMin = -3
yMax = 1

# Vektorar og matriser med funksjonsverdiar 
# Vi brukar 200 punkt både for x og y
x = np.linspace(xMin, xMax, 200)
y = np.linspace(yMin, yMax, 200)
X, Y = np.meshgrid(x, y)

# Matrise med z-verdiar
Z = funk(X, Y)

# Plottar funksjonen som fargekart
plt.figure(1)
plt.clf()
plt.rc('xtick', labelsize=15) 
plt.rc('ytick', labelsize=15) 
plt.pcolormesh(X, Y, Z, shading = 'auto')
# Set på søyle som viser fargekodinga
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 15)
plt.colorbar()
plt.show()
