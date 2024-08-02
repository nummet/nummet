"""
Dette skriptet gjer finn lokale ekstremalpunkt for ein to-variabel funksjon
ved hjelp av gradient-metoden.

Alle inputs, inkludert funksjonsuttrykket, er hardkoda i starten av skriptet.
Dei partielle deriverte er estimerte ved hjelp av midspunktsformelen for 
numerisk derivasjon.
"""

# Importere NumPy
import numpy as np

# Funksjonen vi skal minimere
def funk(x, y):
#    return np.cos(x**2 + y**2)*np.exp(-(x-1)**2-(y-2)**2)
    return np.cos(x**2 + 0.5*y**2)*np.exp(-(x-1)**2-(y-2)**2)
#    return 1/(x**2-x*y+2*y**2+x+y+1)


# Paramerar for gradient-metoden
gamma = 1e-2        # Læringsraten
GradMin = 1e-4      # Stopp-kriterium for gradienten
h = 1e-3            # Steglenda brukt i dei deriverte

# Startpunkt
x = 0
y = 0

# Initiere GradLengde - for å komme i gong
GradLengde = 1e2
# Gradient-metoden
while GradLengde > GradMin:
    # Estimerar gradienten - ved midspunktsmetoden
    dfdx = (funk(x+h, y) - funk(x-h, y))/(2*h) 
    dfdy = (funk(x, y+h) - funk(x, y-h))/(2*h)
    
    # Lengda av gradienten
    GradLengde = np.sqrt(dfdx**2 + dfdy**2)

    # Skriv GradLengde til skjerm - for å følge framdrifta
    print(f'Lengda av gradienten: {GradLengde:.5e}')
    
    # Oppdaterar parametrane
    x = x + gamma*dfdx
    y = y + gamma*dfdy
    

# Skriv optimale parametrar til skjerm
print('Ekstremalpunkt:')
print(f'x = {x:.4f}')
print(f'y = {y:.4f}')
print(f'Funksjonsverdi i punktet: {funk(x,y):.4f}')

