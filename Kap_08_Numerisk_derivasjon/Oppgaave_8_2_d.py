"""Skript som lagar plott av folkeveksten på 1900-talet ut frå ein gitt 
tabell, som er hardkoda inn i skriptet. Midtpunktsformelen for numerisk 
derivasjon er brukt for alle dei aktuelle åra.
"""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Fontstorleik på plotta
plt.rcParams.update({'font.size': 15})

# Gir vektorar med år og folketal (i milliardar):
h = 10
aar = range(1905, 2001, h)
folk = np.array([1.65, 1.75, 1.86, 2.07, 2.30, 
                 2.52, 3.02, 3.70, 4.45, 5.30, 6.12])

# Reknar ut dei deriverte
folk_deriv = np.zeros(10)         # Allokerer
h_ny = 5
# For åra 1905 - 1995
for n in range(1, 10):
    folk_deriv[n] = (folk[n+1]-folk[n-1])/(2*h_ny)

# Plottar vekstfarten
plt.figure(1)
# Reknar om til millionar/år
plt.plot(aar, folk_deriv*1e3, 'k-', linewidth=2)
plt.xlabel('År')
plt.ylabel('Vekst i folketal i millionar per år')
plt.grid(visible = True)
plt.show()