""" Dette skriptet estimerar den deriverte for ein funskjon
på tre ulike måtar: med fram- og bakoverformelen og med midtpunktsformelen 
for numerisk derivasjon. 
Feilen blir rekna ut ved å samanlikne direkte med det eksakte svaret. 
Denne feilen blir plotta for ulike verdiar av steglengda h.
Dette plottet blir laga med både lineære og logaritmiske aksar.
"""

# Importerar bibliotek
import numpy as np
import matplotlib.pyplot as plt

def funk(x):
    """Funksjonen som skal deriverast"""
    return np.sin(x**2)

def funk_d(x):
    """Derivert (eksakt)"""
    return 2*x*np.cos(x**2)

# Fontstorleik på plotta
plt.rcParams.update({'font.size': 15})

# Argument-verdi
a = 1

# Eksakt svar
derivert = funk_d(a)

# Vektor med ulike steglengder
h = 0.25**np.arange(1, 8)    # Grov oppdeling

# Tre estimat: framover-, bakover- og midtpunktsformel
fram_formel = np.abs((funk(a+h)-funk(a))/h - derivert)
bak_formel = np.abs((funk(a)-funk(a-h))/h - derivert)
midt_formel = np.abs((funk(a+h)-funk(a-h))/(2*h) - derivert)

# Plottar feilen - lineære aksar
plt.figure(1)
plt.plot(h, fram_formel, 'b-', label = 'Framover')
plt.plot(h, bak_formel, 'g--', label = 'Bakover')
plt.plot(h, midt_formel, 'm-.', label = 'Midt')
plt.legend()
plt.grid(visible=True)
plt.show()    

# Plottar feilen - logaritmiske aksar
plt.figure(2)
plt.loglog(h, fram_formel, 'b-', label = 'Framover')
plt.loglog(h, bak_formel, 'g--', label = 'Bakover')
plt.loglog(h, midt_formel, 'm-.', label = 'Midt')
plt.legend()
plt.grid(visible=True)
plt.show()    