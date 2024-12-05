"""Dette er ei implementering av Newtons metode der iterasjonane blir
gjort i ei while-løkke.
Startverdi, presisjon funksjonsuttrykk og den deriverte av denne er input.
Den estimerte løysinga blir skrive til skjerm.
"""

# Inporterer numpy
import numpy as np

# Funksjonen vi skal estimere nullpunktet for
def funk(x):
   return np.sqrt(x)-np.cos(x)
   
# Den deriverte av funksjonsuttrykket
def funk_deriv(x):
    return 1/(2*np.sqrt(x))+np.sin(x)
    
# Bestemmer x_0
x = 1

# Antal iterasjonar
N = 5

# Initerer talet på iterasjonar
iterasjonar = 0

# Lagar ein variabel for "gamal" x-verdi (tilfeldig tal)
x_gml = 100

for n in range(1, N+1):
    # Kopierer den gamle x
    x_gml = x
    # Iterasjonsskjema
    x = x-funk(x)/funk_deriv(x)

# Skriv svaret til skjerm
print(f'x = {x:.5f}')