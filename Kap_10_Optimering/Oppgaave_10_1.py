""" Dette skriptet estimerar maksimalverdien for ein funksjon.
Input er maksimal og minimal x-verdi - i tillegg til sjølve 
funksjonsuttrykket.
"""

# Importerar NumPy
import numpy as np

def funk(x):
    """Funksjonsuttrykk"""
    return x**3 + 4*np.sin(x**2)

# Definisjonsområde
x_min = 0
x_max = 2

# Talet på punkt
n_pkt = 100

# Vektorar med x- og y-verdiar
x_vektor = np.linspace(x_min, x_max, n_pkt)
y_vektor = funk(x_vektor)

# Initierer ekstremalverdi
max_verdi = funk(x_min)
x_for_max = x_min

# Går gjennom "alle" x-verdiane
for x in x_vektor:
    y = funk(x)
    if y > max_verdi:
        max_verdi = y
        x_for_max = x
        
# Skriv resultatet til skjerm:
print(f'Maksimalverdi: {max_verdi:.4f}')
print(f'Funksjonen er maksimal for x = {x_for_max:.4f}')  