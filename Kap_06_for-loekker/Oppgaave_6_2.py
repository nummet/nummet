# Importerer NumPy
import numpy as np

# Set grenser
a = -5
b = 10

# Funksjon for ledda i summen
def ledd(i):
    return 1/np.sqrt(i**2 + 1)

# Set summen til 0
s = 0

for i in range(a, b+1):     # Bestemmer summasjonsgrensene
    s = s + ledd(i)         # Legg til eit ledd

# Skriv summen til skjerm:
print(f's = {s:.4f}')