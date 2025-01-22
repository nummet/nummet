"""Implementering av trapesmetoden og Simpsons metode for numerisk
integrasjon. Integrasjonsgrensene a og b, oppdelinga n 
og integranden, funk, blir gitt heilt i toppen av 
implementeringa. For å gi n brukar vi input-funksjonen.
"""

# Importerar NumPy
import numpy as np

# Integrasjonsgrenser
a = -1
b = 1

def funk(x):
    """Integranden"""
    return np.sin(x**2)

# Oppdeling
n = int(input('Gi oppdelinga n: '))

h = (b-a)/n                  # Steglengda

# Trapesmetoden
# Bidrag frå endane
T = h/2*(funk(a)+funk(b))

# Resten av bidraga
for i in range(1, n):
    xi = a+i*h
    T = T+h*funk(xi)


#Simpsons metode
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


# Skriv svara til skjerm
print(f'T = {T:.15f}')      # Trapesmetoden
print(f'S = {S:.15f}')      # Simpsons metode
