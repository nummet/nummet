"""Dette skriptet løyser likninga 
a x^2 + b x + c = 0 .
Vi er her berre interesserte i reelle løysingar.
Dersom der berre er ei løysing, blir denne skriven til
skjerm ein gong.
"""

# Importerer NumPy
import numpy as np

# Les inn verdiane for a, b og c:
a = float(input('Gi verdien for a: '))
b = float(input('Gi verdien for b: '))
c = float(input('Gi verdien for c: '))

# Ser om det er ei førstegradslikning
if a==0:
    if b==0:
        print('Inga løysing')
    else:      
        x = -c/b
        print(f'x = {x:.5f}')

# Undersøker om vi har to, ei eller ingen reelle løysingar
elif b**2-4*a*c<0:              # Inga reell løysing
    print('Inga reell løysing')
elif b**2-4*a*c==0:             # Ei løysing
    x = -b/(2*a)
    print(f'x = {x:.5f}')
else:                           # To løysingar
    x1 = (-b-np.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
    print(f'x1 = {x1:.5f}')
    print(f'x2 = {x2:.5f}')