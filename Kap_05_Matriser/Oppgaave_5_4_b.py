"""
I dette skriptet forsøker vi å løyse eit likningssystem 
ved å invertere koeffisientmatrisa.
Dette gir berre meining når vi har like mange likningar 
og ukjende - altså  når koeffisientmatrisa er kvadratisk.
"""

# Importerar numpy
import numpy as np

# Sett antall desimalar vi skriv til skjerm for NumPy
np.set_printoptions(precision=4, floatmode='fixed', suppress=True)

# Tilordnar matrisa
A = np.array([[1, 2, 0, 0],
             [1, -2, 1, 0],
             [0, 1, -2, 1],
             [0, 0, 1, -3]])

# Hoegresida (som vektor)
b = np.array([3, 7, np.pi, 2+3j])

# Reknar ut løysinga og skriv ho til skjerm
Ainv = np.linalg.inv(A)
x = np.matmul(Ainv, b)
print(np.round(x, 3))
