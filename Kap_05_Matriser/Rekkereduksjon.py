"""
Dette skriptet rekkereduserar ei matrise, typisk 
totalmatrisa til eit lineært likningssystemt, til 
redusert trappeform og skriv resultatet til skjerm.
"""

# Importerar NumPy og SymPy
import numpy as np
import sympy

# Sett antall desimalar vi skriv til skjerm for NumPy
np.set_printoptions(precision=4, floatmode='fixed', suppress=True)

# Tilordnar totalmatrisa 
T = np.array([[5, 1, 1, -2, 2],
              [1, -1, 1, 7, 30],
              [2, 1, 0, -5, -16],
              [2, 0, 1, 3, 17]])


R = sympy.Matrix(T).rref()[0]    # Rekkereduserar
R = np.array(R)                  # Konverterar til array
print(R)                         # Skriv til skjerm