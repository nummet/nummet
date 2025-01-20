"""
Dette skriptet definerar funksjonar som implementerar 
dei tre typane rekkeoperasjonar vi kan gjere på ei matrise.
Den brukar så desse funksjonane til å rekkeoperere på 
ei gitt matrise.
"""

# Importerar NumPy
import numpy as np

# Sett antall desimalar vi skriv til skjerm for NumPy
np.set_printoptions(precision=4, floatmode='fixed', suppress=True)

# Tilordnar ei matrise
A = np.array([[1, 2, 3],
              [4, 5, 6]])
             
# Funksjon som gangar rekke n med talet k
def GangeRekke(A, n, k):
    B = np.copy(A)
    B[n, :] = k*A[n, :]
    return B

# Funksjon som byter om på rekke m og n
def ByteRekker(A, m, n):
    B = np.copy(A)
    B[m, :] = A[n, :]
    B[n, :] = A[m, :]
    return B    

# Funksjon som legg k gonger rekke m til rekke n
def LeggeTilMult(A, m, n, k):
    B = np.copy(A)
    B[n, :] = A[n, :] + k*A[m, :]
    return B

# Utfører rekkeoperasjonar på A
A1 = LeggeTilMult(A, 0, 1, -4)
print(A1)

A2 = GangeRekke(A1, 1, -1/3)
print(A2)

A3 = LeggeTilMult(A2, 1, 0, -2)
print(A3)            
             
