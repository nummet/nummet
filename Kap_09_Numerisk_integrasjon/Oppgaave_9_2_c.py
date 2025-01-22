"""Implementering av trapesmetoden. Integrasjonsgrensene a og b, oppdelinga 
n og integranden funk blir gitt heilt i toppen av koden.
For å gi oppdelinga n brukar vi input-funksjonen.
"""

# Importerer bibliotek
import numpy as np

# Nøyaktig integral
integral = 2/7

# Integrasjonsgrensene
a = -1
b = 1

def funk(x):
    """Integranden"""
    return x**6

# Oppdeling (kontrollerer at n er eit partal)
n = int(input('Gi oppdelinga n: '))

if round(n/2) != n/2:
    raise ValueError('n må vere eit partal')

h = (b-a)/n                  # Steglengda

# Bidrag frå endane
S = h/3*(funk(a)+funk(b))

# Oddetalsbidrag:
for i in range(1, n, 2):
    xi = a+i*h
    S = S+h/3*4*funk(xi)

# Partalsbidrag
for i in range(2, (n-1), 2):
    xi = a+i*h
    S = S+h/3*2*funk(xi)

# Skriv svaret til skjerm
print(f'S = {S:.7f}')

# Finn feilen og skriv til skjerm
feil = abs(S - integral)
print(f'feil = {feil:.4e}')