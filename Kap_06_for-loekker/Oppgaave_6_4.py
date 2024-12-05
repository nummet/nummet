"""I dette skriptet lagar vi ein funksjon som finn den største
verdien i ein vektor.
I tillegg testar vi denne funksjonen på ein spesifikk vektor.
"""

# Imorterar numpy
import numpy as np

# Definerar maksimerings-funksjonen
def maks_funk(x):
    """Funksjon som finn det største elementet i vektoren x.
    """
    
    # Tilordnar m - det foreløpig største elementet
    m = x[0]

    # for-løkke som går gjennom x
    for elem in x:
        if elem > m:
            # Om elementet er større enn M, oppdaterer vi M
            m = elem

    return m    


# Testar at funksjonen finn maksimalverdien for ein vektor
x = np.array([7, np.pi, -4, 14, 3, 9])
print(f'x = {x}')
print(f'maks_funk(x) = {maks_funk(x):.2f}')    
