"""Implementering av halveringsmetoden for likninga f(x)=0
der f er kontinuerleg på [a,b] og f(a) og f(b) har ulike
forteikn.
"""

# Importerer NumPy
import numpy as np

# Grenser
a = 0
b = np.pi/2

def null_funk(x):
    """Gir funksjonen som skal vere null"""
    return np.sqrt(x)-np.cos(x)
    
# Funksjonsverdiar
fa = null_funk(a)
fb = null_funk(b)

# Startar for-løkke som blir køyrd 10 gonger
for i in range(1,11):
    c = (a+b)/2      # Midtpunktet
    fc = null_funk(c)# Funksjonsverdi i midtpunktet
    if fa*fc<0:
        b = c        # Set ny b til c
    else:
        a = c        # Set ny a til c

# Reknar ut nytt midtpunkt og skriv svaret til skjerm
x = (a+b)/2
print(f'x = {x:.4f}')