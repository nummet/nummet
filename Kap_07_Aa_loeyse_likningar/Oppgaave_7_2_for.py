"""Dette er ei implementering av Newtons metode der iterasjonane blir
gjort i ei for-løkke.
Startverdi, antal iterasjonar, funksjonsuttrykk og den deriverte av denne er 
input. Den estimerte løysinga blir skrive til skjerm.
"""

# Inporterer numpy
import numpy as np

# Funksjonen vi skal estimere nullpunktet for
def funk(x):
   return np.sqrt(x)-np.cos(x)
   
    
# Bestemmer x_0
x = 3

# Antal iterasjonar
N = 7

for n in range(1, N+1):
    # Iterasjonsskjema
    x = funk(x)

# Skriv svaret til skjerm
print(f'x = {x:.5f}')
