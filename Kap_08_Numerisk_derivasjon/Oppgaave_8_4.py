"""Skript som bestemmer skjæringspunktet mellom eksponentialfunksjonen og 
gammafunksjonen. Til det brukar vi Newtons metode og numerisk derivasjon. 
Skriptet plottar konvergensen av svaret mot h-verdien som blir brukt i 
derivasjonen.
"""

# Importerer bibliotek - inkludert math-biblioteket
import numpy as np
import matplotlib.pyplot as plt
import math

# Gir presisjon og h-verdiane
pres = 1e-5
h_vektor = np.arange(2, 0.0, -0.1)
# Startverdi
x0 = 8

indeks = 0
# Tom vektor med same lengda som h_vektor
svar = np.zeros_like(h_vektor)  

# Bestemmer x ved Newtons metode for kvar av h-verdiane
for h in h_vektor:
    # Initerer x_0 og gamal x-verdi
    x = x0
    x_gml = 10
    while abs(x-x_gml) > pres:
        x_gml = x
        # Den deriverte av gamma
        derivert = (math.gamma(x+h) - math.gamma(x-h))/(2*h)
        # Iterasjonsformel (Newtons metode)
        x = x-(math.gamma(x) - np.exp(x))/ \
            (derivert-np.exp(x))
    svar[indeks] = x
    indeks = indeks+1

# Plottar løysingane som funksjon av h
plt.plot(h_vektor, svar, 'kx-', linewidth=2)
plt.xlabel('h')
plt.ylabel('Løysing')
plt.show()