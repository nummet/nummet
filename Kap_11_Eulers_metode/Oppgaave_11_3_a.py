"""Enkel implementering av Eulers metode
for startverdiproblemet y'=x+y, y(0)=1.
"""

# Importerer bibliotek
import time
import numpy as np

x0 = 0                         # Startkrav
y0 = 1
x_max = 10

N = int(2e5)                       # Oppdeling
h = (x_max-x0)/N

# Vektor med x-verdiar
x_vektor = np.arange(x0, x_max+h, h)
y_vektor = np.empty(0)

x = x0
y = y0
y_vektor = np.append(y_vektor, y0)
start = time.time()           # Startar klokka
for i in range(0, N):
    y = y+(x+y)*h             # Oppdaterer y
    # Skriv y-verdien til vektor
    y_vektor = np.append(y_vektor, y)
    x = x+h                   # Oppdaterer x

tid = time.time() - start     # Stoppar klokka
print(f'tid = {tid:.4e}')