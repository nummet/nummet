"""
Dette skriptet gjer lineær regresjon på eit sett med datapunkt via minste
kvadrat-metoden. Minimeringa som inngÃ¥r blir gjort med gradient-metoden.

Alle inputs, inkludert sjølve data-settet, er hardkoda i starten av skriptet.
"""

# Bibliotek
import numpy as np
from matplotlib import pyplot as plt

# Datasett
Xdata = [1, 1.5, 2, 3, 3.7, 5] 
Ydata = [1, 2, 3 , 4, 5, 7]
AntalPunkt = len(Ydata)

# Paramerar for gradient-metoden
h = 1e-3            # For endeleg-differanse estimat
gamma = 1e-2        # LÃ¦ringsraten
GradMin = 1e-4      # Stopp-kriterium for gradienten

# Startpunkt for parametrane
a = 1
b = 0

# Funksjonen vi skal minimere - summen av kvadrata av feilen
def S(a, b):
    S = 0
    for index in range(0, AntalPunkt):
        x = Xdata[index]
        y = Ydata[index]
        S = S + (y - (a*x+b))**2
    return S

# Initiere GradLengde - for å komme i gong
GradLengde = 1e2

# Gradient-metoden
while GradLengde > GradMin:
    # Estimerar gradienten - ved midspunktsmetoden
    dSda = (S(a+h, b) - S(a-h, b))/(2*h)
    dSdb = (S(a, b+h) - S(a, b-h))/(2*h)
    
    # Lengda av gradienten
    GradLengde = np.sqrt(dSda**2 + dSdb**2)

    # Skriv GradLengde til skjerm - for å følge framdrifta
    print(f'Lengda av gradienten: {GradLengde:.5e}')
    
    # Oppdaterar parametrane
    a = a - gamma*dSda
    b = b - gamma*dSdb
    

# Skriv optimale parametrar til skjerm
print('Optimale parametrar:')
print(f'a = {a:.2f}')
print(f'b = {b:.2f}')
        
# Plottar punkta og modellen med tilpassa parametrar
# (Eigentleg hadde vi klart oss med to punkt for linja)
xx = np.linspace(Xdata[0]-1, Xdata[-1]+1, 5)
plt.figure(1)
plt.clf()
# Datapunkta
plt.plot(Xdata, Ydata, 'kx')
# Modellen
plt.plot(xx, a*xx + b, 'r--', linewidth = 2)
# Tekst og rutenett
plt.xlabel('X', fontsize = 15)
plt.ylabel('Y', fontsize = 15)
plt.grid()
plt.show()