"""Dette er ei implementering av firkspunktiterasjon. Iterasjonane blir
gjort i ei for-løkke, og x-verdien blir skriven til skjerm for kvar iterasjon. 
Startverdi, antal iterasjonar og funksjonsuttrykk er input.
"""

# Inporterer numpy
import numpy as np

# Funksjonen vi skal estimere fikspunktet for
def funk(x):
   return (np.cos(x))**2
   
    
# Bestemmer x_0
x = 1

# Antal iterasjonar
N = 7


for n in range(1, N+1):
    # Iterasjonsskjema
    x = funk(x)
    print(f'x = {x:.5f}')