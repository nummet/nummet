"""Kode som bestemmer kor lang tid det å tømme ein tank.

Profilen til tanken er gitt ved R(x) under.
Vi tar utgangspunkt i Torricellis lov, V'(t) = -k sqrt(h).
"""

# Importerar NumPy
import numpy as np

# Startkrav:
t0 = 0
h0 = 60

# Parametrar
v_tot = 19951
k = 2*v_tot/(3*np.sqrt(h0))

# Initerar h og t
t = t0
h = h0

def R(x):
    """Profilfunksjon"""
    return 5+4/(1+np.exp((35-x)/1.5)) * \
        (np.sqrt(x+1)-np.sqrt(31))**2

def F(x):
    """Høgresida i differensiallikninga"""
    return -k*np.sqrt(x)/(np.pi*R(x)**2)

# Steglengde
dt = float(input('Steglengda i tid: '))

while h > 0:
    h = h+F(h)*dt       # Eulers metode
    t = t+dt

# Skriv slutttida til skjerm
print(f't = {t:.4f}')