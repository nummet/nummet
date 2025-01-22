"""Implementeringa estimerer eit integral ved 
Monte Carlo-metoden.
Sjølve integralet, og den analytiske løysninga 
av det, er spesifisert i starten av koden - i 
tillegg til det maksimale talet på trekk.
"""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Integrasjonsgrenser
a = -1
b = 3

def funk(x):
    """Integrand"""
    return x * np.sin(x**2)

# Kjent analytisk svar:
fasit = (np.cos(1)-np.cos(9))/2

# Maksimalt tal på trekk:
n_max = 1000

# Initierer summen
MC_sum = 0

# Lagar klart plott for estimata - saman med eksakt svar
plt.hlines(fasit, 1, n_max, 'k', linestyles = '--')

# Vi utfører uttrekka og legg til summen for kvar gong
for n in range(1, n_max+1):
    x = a+(b-a)*np.random.rand()
    MC_sum = MC_sum+funk(x)
    estimat = (b-a)*MC_sum/n         # Integral-estimat
    plt.plot(n, estimat, 'b.')       # Plottar estimat

plt.xlim(0, n_max)
plt.ylim(-1, 2)
plt.grid(visible=True)
plt.show()

# Skriv svaret til skjerm
print(f'estimat = {estimat:.4f}')