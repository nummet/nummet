"""
Dette skriptet gjer finn lokale ekstremalpunkt for ein to-variabel funksjon
ved hjelp av gradient-metoden.

Alle inputs, inkludert funksjonsuttrykket og dei partielt deriverte av denne, 
er hardkoda i starten av skriptet.
"""

# Importere NumPy
import numpy as np

# Funksjonen vi skal minimere
def funk(x, y):
    return 1/(x**2-x*y+2*y**2+x+y+1)

# Dei partielle deriverte
# x-derivert
def funkX(x,y):
    return -(2*x-y+1)/(x**2-x*y+2*y**2+x+y+1)**2
# y-derivert
def funkY(x,y):
    return -(-x+4*y+1)/(x**2-x*y+2*y**2+x+y+1)**2

# Paramerar for gradient-metoden
gamma = 1e-2        # Læringsraten
GradMin = 1e-4      # Stopp-kriterium for gradienten

# Startpunkt
x = 0
y = 0

# Initiere GradLengde - for å komme i gong
GradLengde = 1e2
# Gradient-metoden
while GradLengde > GradMin:
    # Reknar ut gradienten
    dfdx = funkX(x, y)
    dfdy = funkY(x, y)    
    # Lengda av gradienten
    GradLengde = np.sqrt(dfdx**2 + dfdy**2)

    # Skriv GradLengde til skjerm - for å følge framdrifta
    print(f'Lengda av gradienten: {GradLengde:.5e}')
    
    # Oppdaterar variablane
    x = x + gamma*dfdx
    y = y + gamma*dfdy
    

# Skriv optimale parametrar til skjerm
print('Ekstremalpunkt:')
print(f'x = {x:.4f}')
print(f'y = {y:.4f}')
print(f'Funksjonsverdi i punktet: {funk(x,y):.4f}')
