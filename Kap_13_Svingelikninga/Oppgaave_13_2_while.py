"""Implementering av Eulers framovermetode for svinvelikninga.
Input: Startkravet y(x0)=y0, y'(x0)=u0 og F(x,y), som definerer 
differensiallikninga ved Y'=F(Y), der Y=[y, u]^T, y' = u og u' = -5*sin(y).
Merk at koden skil mellom "Y", som er ein vektor i R^2, og skalaren "y".
Progammet tar talet på steg, N, som input.
I dette skriptet forsøker vi å finne ut når y(t) = y0/10. Svaret blir skrive
til skjerm til slutt.
"""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt


# Storleik på bokstavar i plott
plt.rcParams.update({'font.size': 15})

# Startkrav og maksimal x-verdi
x0 = 0
y0 = .15
u0 = 0
x_max = 50

def F(x, Y):
    """Differensiallikning"""
    return np.array([Y[1], -5*np.sin(Y[0])])


# Steglengda
N = int(input('Gi talet på steg: '))
h = (x_max-x0)/N

# Lagar vektorar
x_vektor = np.linspace(x0, x_max, N+1)
y_vektor = np.zeros_like(x_vektor)
y_vektor[0] = y0

# Initerer x og Y
x = x0
Y = np.array([y0, u0])

# for-løkke som implementerer Eulers midpunktsmetode
while np.abs(Y[0] - y0*np.cos(np.sqrt(5)*x)) < y0/10:
    # Eulers midtpunktsmetode
    x_hatt = x + h/2
    y_hatt = Y + F(x,Y)*h/2
    Y = Y + F(x_hatt,y_hatt)*h
    # Oppdaterer x
    x = x+h

# Skriv sluttverdi til skjerm
print(f'x = {x:.4f}')