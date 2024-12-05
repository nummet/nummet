"""Dette er ei implementering av Newtons metode der iterasjonane blir
gjort i ei while-løkke.
Startverdi, presisjon funksjonsuttrykk og den deriverte av denne er input.
Som output blir den estimerte løysinga og talet på iterasjonar skrivne
til skjerm.
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

# Presisjon
pres = 1e-5

# Initerer talet på iterasjonar
iterasjonar = 0

# Lagar ein variabel for "gamal" x-verdi (tilfeldig tal)
x_gml = 100

while abs(x-x_gml) > pres:
    # Kopierer den gamle x
    x_gml = x
    # Iterasjonsskjema
    x = x-funk(x)/funk_deriv(x)
    # Tel iterasjonar
    iterasjonar = iterasjonar+1

# Skriv svaret til skjerm
print(f'x = {x:.5f}')

# Skriv talet på iterasjonar til skjerm
print(f'iterasjonar = {iterasjonar}')