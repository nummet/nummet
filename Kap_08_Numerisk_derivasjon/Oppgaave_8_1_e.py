""" Dette skriptet estimerar den deriverte for ein funskjon
ved hjelp av midtpunktsformelen for numerisk derivasjon. 
Den samanliknar også estimatet med det eksakte svaret.
Input er funksjonen vi skal derivere, steglengda h og
den eksakte deriverte.
"""

# Importerar NumPy
import numpy as np

def funk(x):
    """Funksjonen som skal deriverast"""
    return np.sin(x**2)

def funk_d(x):
    """Derivert (eksakt)"""
    return 2*x*np.cos(x**2)

# Estimerer den deriverte og sjekkar feilen
a = 1
h = 0.5
estimat = (funk(a+h) - funk(a))/h
feil = np.abs(estimat - funk_d(a))
print(f'h = {h:.4f}, estimat: {estimat:.4f}, \
feil: {feil:.2e}')

