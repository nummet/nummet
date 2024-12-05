"""Dette er ei implementering av halveringsmetoden. Her er iterasjonane
implementert ved hjelp av ei while-løkke.
Vidare tel vi talet på iterasjonar og skriv dette til skjerm saman 
med den estimerte løysinga av likninga til slutt.
Input er grensene for intervallet løysinga skal ligga i og funksjonen
som skal vere null. Presisjonen er hadkoda til å vere 10^{-5}; dette
kan lett endrast.
"""

# Importerer numpy
import numpy as np

# Grenser
a = 1
b = 3

def null_funk(x):
    """Gir funksjonen som skal vere null"""
    return x**4 - 4*x**2 - 5

# Funksjonsverdiar
fa = null_funk(a)
fb = null_funk(b)

# Initierer variabel som tel iterasjonane
iterasjonar = 0

# while-løkke for halveringsmetoden
while b-a > 2e-5:
    c = (a+b)/2          # Midtpunktet
    fc = null_funk(c)    # Funksjonsverdi i midtpunktet
    if fa*fc < 0:
        b = c            # Set ny b til c
    else:
        a = c            # Set ny a til c
    iterasjonar = iterasjonar + 1  # Tel iterasjonane

# Reknar ut nytt midtpunkt og skriv svaret til skjerm
x = (a+b)/2
print(f'x = {x:.7f}')

# Skriv talet på iterasjonar til skjerm
print(f'iterasjonar = {iterasjonar}')