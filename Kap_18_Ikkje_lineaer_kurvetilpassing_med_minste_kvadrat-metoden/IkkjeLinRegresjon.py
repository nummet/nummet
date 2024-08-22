"""
Dette skriptet optimerar parametrane for ein modelle for eit gitt data-sett. 
Modellen er ein kombinasjon av ein trigonometrisk og ein lineær funksjon.

Parametrane i modellen blir bestemt ved først å minimere summen av kvadrata av 
feilen og så minimere denne ved hjelp av gradient-metoden.

Alle inputs, inkludert sjølve data-settet, er hardkoda i starten av skriptet.
"""

# Bibliotek
import numpy as np
from matplotlib import pyplot as plt

# Datasett
Ydata = [-3.9, -2.3, -1.2, 0.1, -1, -3.8, -5.3, -3.7, -1.3,
         0.2, 1.5, 2.7, 1.5, -1.1, -2.6, -1.1, 0.8, 2.6, 
         4.3, 5.0, 3.9, 0.8, -0.5, 1.1, 3.3]
NumPoints = len(Ydata)
Xdata = np.linspace(0, 3, NumPoints)

# Paramerar for gradient-metoden
h = 1e-3            # For endeleg-differnase estimat
gamma = 1e-4        # Læringsraten
GradMin = 1e-4      # Stopp-kriterium for gradienten
ItCountMax = 1e5    # Avgrensing på antal iterasjonar

# Startpunkt for parametrane
a = 4
b = 6
c = 0.4
d = 3
e = -5

# Modell vi vil tilpasse til data
def f(x, a, b, c, d, e):
    return a*np.cos(b*(x - c)) + d*x + e

# Funksjonen vi skal minimere - summen av kvadrata av feilen
# for kvart punkt
def S(a, b, c, d, e):
    S = 0
    for index in range(0, len(Xdata)):
      S = S + (Ydata[index] - \
               f(Xdata[index], a, b, c, d, e))**2
    return S

# Initere GradLengde og ItCount - for å komme i gong
GradLengde = 1e2
ItCount = 0

# Gradient-metoden
while GradLengde > GradMin and ItCount < ItCountMax:
    # Estimerar gradienten - ved midspunktsmetoden
    dSda = (S(a+h, b, c, d, e) - S(a-h, b, c, d, e))/(2*h)
    dSdb = (S(a, b+h, c, d, e) - S(a, b-h, c, d, e))/(2*h)
    dSdc = (S(a, b, c+h, d, e) - S(a, b, c-h, d, e))/(2*h)
    dSdd = (S(a, b, c, d+h, e) - S(a, b, c, d-h, e))/(2*h)
    dSde = (S(a, b, c, d, e+h) - S(a, b, c, d, e-h))/(2*h)
    
    # Lengda av gradienten
    GradLengde = np.sqrt(dSda**2 + dSdb**2 + dSdc**2 + 
                         dSdd**2 + dSde**2)
    # Skriv GradLengde til skjerm - for å følge framdrifta
    print(f'Lengda av gradienten: {GradLengde:.5e}')
    
    # Oppdaterar parametrane
    a = a - gamma*dSda
    b = b - gamma*dSdb
    c = c - gamma*dSdc
    d = d - gamma*dSdd    
    e = e - gamma*dSde
    
    # Tel antal iterasjonar
    ItCount = ItCount + 1

if ItCount == ItCountMax:
    print('Dette ser ikkje ut til å konvergere')
else:
    # Skriv optimale parametrar til skjerm
    print('Optimale parametrar:')
    print(f'a = {a:.2f}')
    print(f'b = {b:.2f}')
    print(f'c = {c:.2f}')
    print(f'd = {d:.2f}')
    print(f'e = {e:.2f}')
    # Skriv minimal(?) funksjonsverdi til skjerm:
    Smin = S(a, b, c, d, e)
    print(f'Minimalverdi for S: {Smin:.2e}')
        
    # Plottar punkta og modellen med tilpassa parametrar
    # x- og y-verdiar for plotting av modell
    xx = np.linspace(Xdata[0], Xdata[-1], 200)
    yy = f(xx, a, b, c, d, e)
    plt.figure(2)
    plt.clf()
    # Datapunkta
    plt.plot(Xdata, Ydata, 'kx')
    # Modellen
    plt.plot(xx, yy, 'g-', linewidth = 2)
    # Tekst og rutenett
    plt.xlabel('X', fontsize = 15)
    plt.ylabel('Y', fontsize = 15)
    plt.grid()
    
    plt.show()