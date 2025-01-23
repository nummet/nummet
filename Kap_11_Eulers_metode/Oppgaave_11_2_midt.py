"""Implementering av Eulers midtpunktsmetode.

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

# for-løkke som implementerer Eulers midtpunktsmetode
y_vektor = np.zeros_like(x_vektor)
y_vektor[0] = y0
for indeks in range(0, N):
    # Eulers midtpunktsmetode
    x_hatt = x+h/2
    y_hatt = y+F(x,y)*h/2
    y = y+F(x_hatt,y_hatt)*h
    # Oppdaterer vektor med y-verdiar
    y_vektor[indeks+1] = y
    # Oppdaterer x
    x = x+h

# Plottar resultatet
plt.figure(1)
plt.clf()
plt.plot(x_vektor, y_vektor, 'b-', linewidth=1)
plt.grid(visible=True)
plt.show()
