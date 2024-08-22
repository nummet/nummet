"""
Dette skriptet gjer finn det globale maksimalpunktet for ein to-variabel 
funksjon på ein "brute force" måte; vi samplar funsjonsverdiar for 
massevis av x- og y-verdiar og ser kva kobinasjon av x og y som gir størst
funksjonsverdi på dei aktuelle intervalla - med den aktuelle oppdelinga.

Alle inputs, inkludert funksjonsuttrykket, er hardkoda i starten av skriptet.
"""

# Importere NumPy
import numpy as np

# Funksjonen vi skal minimere
def funk(x, y):
    return 1/(x**2-x*y+2*y**2+x+y+1)

# Intervall for variablane
xMin = -3
xMax = 1
yMin = -3
yMax = 0

# Antal punkt for variablane (same for begge)
Npkt = 1000

# Vektorar med verdiar for x og y
xVektor = np.linspace(xMin, xMax, Npkt)
yVektor = np.linspace(yMin, yMax, Npkt)

# Initierar MaxVerdi - den største verdien
# Initerar også indeksane til x og y-verdiane
MaxVerdi = funk(xMin, yMin)
MaxPunktX = xMin
MaxPunktY = yMin

# Går gjennom alle x- og y-verdiane
for x in xVektor:
    for y in yVektor:
      funkVerdi = funk(x, y)
      # Oppdaterar maksimalverdi hvis funksjonsverdien er større
      if funkVerdi > MaxVerdi:
          MaxVerdi = funkVerdi
          MaxPunktX = x
          MaxPunktY = y
    
print(f'Global maksimalverdi: {MaxVerdi:.4f}')
print(f'Maksimalpunkt: x = {MaxPunktX:.4f}, y = {MaxPunktY:.4f}')