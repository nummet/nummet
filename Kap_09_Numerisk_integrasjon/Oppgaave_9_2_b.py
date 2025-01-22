"""Implementering av trapesmetoden for numerisk
integrasjon. Integrasjonsgrensene a og b, oppdelinga n 
og integranden, funk, blir gitt heilt i toppen av 
implementeringa. For å gi n brukar vi input-funksjonen.
"""

# Importerar NumPy
import numpy as np

# Nøyaktig integral
integral = 2/7

# Integrasjonsgrenser
a = -1
b = 1

def funk(x):
    """Integranden"""
    return x**6

# Oppdeling
n = int(input('Gi oppdelinga n: '))

h = (b-a)/n                  # Steglengda

# Bidrag frå endane
T = h/2*(funk(a)+funk(b))

# Resten av bidraga
for i in range(1, n):
    xi = a+i*h
    T = T+h*funk(xi)

# Skriv svaret til skjerm
print(f'T = {T:.4f}')

# Finn feilen og skriv til skjerm
feil = abs(T - integral)
print(f'feil = {feil:.4e}')