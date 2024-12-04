"""Skript som finn løysingane av andregradslikninga,
a x^2 + b x + c = 0.
Koeffisientane a, b og c blir lest inn frå skjerm.
"""

# Importerer NumPy-biblioteket
import numpy as np

# Les inn koeffisientane
a = float(input('Gi verdien for a: '))
b = float(input('Gi verdien for b: '))
c = float(input('Gi verdien for c: '))

# Reknar ut løysingane
x1 = (-b-np.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b+np.sqrt(b**2-4*a*c))/(2*a)

# Skriv løysingane til skjerm
print(f'x1 = {x1}')
print(f'x2 = {x2}')