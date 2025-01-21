"""Dette er ei implementering av Newtons metode der iterasjonane blir
gjort i ei for-løkke.
Startverdi, antal iterasjonar, funksjonsuttrykk og den deriverte av denne er 
input. Som output blir den estimerte løysinga og talet på iterasjonar skrivne
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

# Antal iterasjonar
N = 5

for n in range(1, N+1):
    # Iterasjonsskjema
    x = x-funk(x)/funk_deriv(x)

# Skriv svaret til skjerm
print(f'x = {x:.5f}')
