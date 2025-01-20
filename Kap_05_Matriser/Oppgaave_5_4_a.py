"""
I dette skriptet tilordnar vi ei kvadratisk matrise 
og inverterar ho.
Inversmatrisa blir skriven til skjerm.
"""

# Importerar numpy
import numpy as np

# Sett antall desimalar vi skriv til skjerm for NumPy
np.set_printoptions(precision=4, floatmode='fixed', suppress=True)

# Tilordnar matrisa
A = np.array([[3, -7, 1],
              [3, 3, -1],
              [1, 1, 1]])

# Inverterar og skriv resultatet til skjerm
Ainv = np.linalg.inv(A)
print(Ainv)

# Sjekkar at produktet blir I
Prod = np.matmul(A, Ainv)
print(Prod)
