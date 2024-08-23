"""
Her reknar vi ut produktet av to kvadratiske 
matriser - på ulike måtar måtar.
"""

# Importerar NumPy
import numpy as np

# Sett antall desimalar vi skriv til skjerm for NumPy
np.set_printoptions(precision=4, floatmode='fixed', suppress=True)

# Tilordnar to matriser
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
B = np.array([[-2, -1, 0],
              [0, 1, 0],
              [7, -2, 1]])

# Med *-produkt
print('A*B:')
print(A*B)
print('B*A:')
print(B*A)

# Med @-produkt
print('A@B:')
print(A@B)
print('B@A:')
print(B@A)

# Med multiply
print('multiply(A, B):')
print(np.multiply(A, B))


# Med matmul
print('matmul(A, B):')
print(np.matmul(A, B))
