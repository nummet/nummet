"""Implementering av Eulers midtpunktsmetode.

Input: Startkravet y(x0)=y0 og F(x,y),
som definerer differensiallikninga ved
y'=F(x,y).

I dette tilfellet har problemet ei kjend, eksakt analytisk løysing.
Vi plottar det numeriske estimatet saman med denne.
"""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Startkrav og maksimal x-verdi
x0 = 0
y0 = 1
x_max = 2

def F(x,y):
    """Differensiallikning"""
    return 3/2*np.sqrt(x)*y

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

# Eksakt løysing
def Eksakt(x):
    return np.exp(x**(3/2))

# Plottar resultatet
plt.figure(1)
plt.clf()
# Plottar eksakt løysing
x_eksakt = np.linspace(x0, x_max)
plt.plot(x_eksakt, Eksakt(x_eksakt), 'k-', linewidth=1, label = 'Eksakt')
# Plottar numerisk estimat
plt.plot(x_vektor, y_vektor, 'b-', linewidth=1, label = 'Numerisk')
plt.legend()
plt.grid(visible=True)
plt.show()
