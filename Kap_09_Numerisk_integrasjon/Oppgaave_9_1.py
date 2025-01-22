"""Implementering som reknar ut venstre og høgre Riemann-summar. Det 
reknar også ut gjennomsnittet av dei, altså eit trapes-estimat av 
det aktuelle integralet.
"""

# Importerar NumPy
import numpy as np


# Talet på rektangel
n = int(input('Kor mange rektangel? '))

def funk(x):
    """Integranden"""
    return x**3

# Grenser
a = 1
b = 3

# Bestemmer h og initierer venstre-summen V
h = (b-a)/n
V = 0

for i in range(0, n):
    xi = a+i*h              # Oppdaterer x
    V = V+h*funk(xi)        # Oppdaterer V

# Skriv summen V til skjerm
print(f'V = {V:.4f}')

# Initierar høgre-summen H
H = 0
for i in range(1, n+1):
    xi = a+i*h              # Oppdaterer x
    H= H+h*funk(xi)        # Oppdaterer H

# Skriv summen H til skjerm
print(f'H = {H:.4f}')

# Reknar ut gjennomstnittet og skriv til skjerm
T = (V+H)/2
print(f'T = {T:.4f}')
