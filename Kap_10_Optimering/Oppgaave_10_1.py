"""
Dette skriptet plottar grafen til ein funksjon på eit lukka intervall.
I tillegg estimerar det masksimalverdie til funksjonen på dette 
intervallet.
"""

# Bibliotek
import numpy as np
from matplotlib import pyplot as plt

# Funksjonsuttrykk
def funk(x):
    return x**3 + 4*np.sin(x**2)

# DefinisjonsomrÃ¥de
xMin = 0
xMax = 2

# Talet pÃ¥ punkt (bÃ¥de plotting og maksimering)
Npkt = 100

# Vektorar til plotting
xVektor = np.linspace(xMin, xMax, Npkt)
yVektor = funk(xVektor)

# Finn ekstremalverdi
MaxVerdi = funk(xMin)
xForMax = xMin

# GÃ¥r gjennom "alle" x-verdiane
for x in xVektor:
    y = funk(x)
    if y > MaxVerdi:
        MaxVerdi = y
        xForMax = x
        
# Skriv resultatet til skjerm:
print(f'Maksimalverdi: {MaxVerdi:.3f}')
print(f'Funksjonen er maksimal for x = {xForMax:.4f}')  

# Plottar
plt.figure(1)
plt.clf()
# Plottar funksjonen
plt.plot(xVektor, yVektor, 'k-')
# Plottar ekstremalpunkt
plt.plot(xForMax, MaxVerdi, 'ro', markersize = 8, markerfacecolor = 'none')
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 15)
plt.grid()
plt.show()
      
