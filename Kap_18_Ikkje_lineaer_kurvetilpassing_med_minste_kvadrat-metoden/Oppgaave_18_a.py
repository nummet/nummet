"""Dette skriptet plottar eit data-sett saman med ein parametrisert funksjon
vi ønsker å tilpasse slik at funksjonen blir ei god tilnærming til punkta i 
data-settet.

I skriptet blir parametrane fiksert og funksjonen plotta - slik at vi kan sjå 
og vurdere i kor stor grad dei er samanfallande.

Alle inputs, inkludert sjølve data-settet, er hardkoda i starten av skriptet.
"""

# Bibliotek
import numpy as np
from matplotlib import pyplot as plt

# Fontstorleik i plotta
plt.rcParams.update({'font.size': 15})

# Datasett
Ydata = [-3.9, -2.3, -1.2, 0.1, -1, -3.8, -5.3, -3.7, -1.3, 0.2, 1.5, 2.7, 
         1.5, -1.1, -2.6, -1.1, 0.8, 2.6, 4.3, 5.0, 3.9, 0.8, -0.5, 1.1, 3.3]
NumPoints = len(Ydata)
Xdata = np.linspace(0, 3, NumPoints)

# Startpunkt for parametrane
a = 4
b = 6
c = 0.4
d = 3
e = -5

# Modell vi vil tilpasse til data
def f(x, a, b, c, d, e):
    return a*np.cos(b*(x - c)) + d*x + e 


# Plottar punkta og modellen med tilpassa parametrar
# x- og y-verdiar for plotting av modell
xx2 = np.linspace(Xdata[0], Xdata[-1], 200)
yy2 = f(xx2, a, b, c, d, e)
plt.figure(1)
plt.clf()
plt.rc('xtick') 
plt.rc('ytick') 
plt.plot(Xdata, Ydata, 'kx')
plt.plot(xx2, yy2, 'r-')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(visible=True)
plt.show()
