"""Skript som lagar plott av folkeveksten på 1900-talet ut frå ein gitt 
tabell, som er hardkoda inn i skriptet. Midtpunktsformelen for numerisk 
derivasjon er brukt for alle dei aktuelle åra - bortsett frå det første og 
det siste.
"""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Fontstorleik på plotta
plt.rcParams.update({'font.size': 15})

# Gir vektorar med år og folketal (i milliardar):
h = 10
aar = range(1900, 2001, h)
folk = np.array([1.65, 1.75, 1.86, 2.07, 2.30, 
                 2.52, 3.02, 3.70, 4.45, 5.30, 6.12])

# Plottar folketal
plt.figure(1)
plt.plot(aar, folk, 'k-', linewidth=2)
plt.xlabel('År')
plt.ylabel('Folketal i milliardar')
plt.grid(visible = True)
plt.show()

# Reknar ut dei deriverte
folk_deriv = np.zeros(11)         # Allokerer
# For år 1900
folk_deriv[0] = (folk[1]-folk[0])/h
# For åra 1910-1990
for n in range(1, 10):
    folk_deriv[n] = (folk[n+1]-folk[n-1])/(2*h)
# For år 2000
folk_deriv[10] = (folk[10]-folk[9])/h

# Plottar vekstfarten
plt.figure(2)
# Reknar om til millionar/år
plt.plot(aar, folk_deriv*1e3, 'k-', linewidth=2)
plt.xlabel('År')
plt.ylabel('Vekst i folketal i millionar per år')
plt.grid(visible = True)
plt.show()

# Plottar relativ vekstfart
plt.figure(3)
plt.plot(aar, folk_deriv/folk*100, 'k-', linewidth=2)
plt.xlabel('År')
plt.ylabel('Relativ vekst i prosent per år')
plt.grid(visible = True)
plt.show()    