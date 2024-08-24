""" Skriptet finn eigenverdiar og eigenvektorar til ei matrise. 
I tillegg til å skrive ut desse, sjekkar også skriptet om
den karakteristiske likninga, det(A - \lambda I) = 0, er
oppfylt - og at V^{-1} A V, der V har eigenvektorane som
søyler, blir ei diagonalmatrise med eigenverdiane langs 
diagonalen.
"""

# Importerar NumPy
import numpy as np

# Sett antall desimalar vi skriv til skjerm for NumPy
np.set_printoptions(precision=4, floatmode='fixed', suppress=True)

# Tilordnar matrisa
A = np.array([[4, 6, 6],
              [-2, 5, 5],
              [2, -3, -3]])

# Finn eigenverdiar og eigenvektorar
Lambda, V = np.linalg.eig(A)

#Skriv verdiane til skjerm
print('Vektor med eigenverdiar:')
print(Lambda)
print('Matrise med eigenvektorar:')
print(V)

# Sjekkar den karakterstiske likninga
EigenVerdi = Lambda[0]
Rot = np.linalg.det(A - EigenVerdi*np.eye(3)) 
print('VS i karakteristisk likning: ', Rot)

# Sjekkar diagonaliseringa
Vinv = np.linalg.inv(V)            # Inverterar 
D = np.matmul(Vinv, np.matmul(A, V))      
print('Produktet Vinv A V: ')
print(np.round(D, 4))      