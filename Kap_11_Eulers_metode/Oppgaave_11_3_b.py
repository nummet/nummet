"""Implementering av Eulers fraomver-metode.

Input: Startkravet y(x0)=y0 og F(x,y),
som definerer differensiallikninga ved
y'=F(x,y).
"""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Startkrav og maksimal x-verdi
x0 = 0
y0 = 0
x_max = 5

def F(x,y):
    """Differensiallikning"""
    return np.sin(x+y**2)

# Steglengda
N = int(input('Gi talet på steg: '))
h = (x_max-x0)/N

# Vektor med x-verdiar
x_vektor = np.linspace(x0, x_max, N+1)

# Initerer x og y
x = x0
y = y0

# Allokerar
x_vektor = np.zeros(int(np.floor(N/10)))
y_vektor = np.zeros(int(np.floor(N/10)))

# for-løkke som implementerer Eulers metode
x_vektor[0] = x0
y_vektor[0] = y0
indeks = 0
for n in range(0, N):
    # Eulers framovermetode
    y = y+F(x,y)*h
    if np.mod(n, 10) == 0:
        # Oppdaterer vektor med x- og y-verdiar
        x_vektor[indeks] = x
        y_vektor[indeks] = y
        indeks = indeks+1
    # Oppdaterer x
    x = x+h

# Plottar resultatet
plt.figure(1)
plt.clf()
plt.plot(x_vektor, y_vektor, 'b-', linewidth=1)
plt.grid(visible=True)
plt.show()
