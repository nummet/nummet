"""Implementering av Eulers framovermetode for ei differensiallikning av 
andre orden. Input: Startkravet y(x0)=y0, y'(x0)=u0 og F(x,y), som definerer 
differensiallikninga ved Y'=F(x,Y), der Y=[y, u]^T.
Merk at koden skil mellom "Y", som er ein vektor i R^2, og skalaren "y".
Progammet tar talet på steg, N, som input.
"""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt


# Storleik på bokstavar i plott
plt.rcParams.update({'font.size': 15})

# Startkrav og maksimal x-verdi
x0 = 0
y0 = 2
u0 = -1
x_max = 2

def F(x, Y):
    """Differensiallikning"""
    return np.array([Y[1], -Y[1]+2*Y[0]+2*x+1])

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

# for-løkke som implementerer Eulers metode
for indeks in range(0, N):
    # Eulers framovermetode
    Y = Y + F(x,Y)*h
    # Oppdaterer vektor med y-verdiar
    y_vektor[indeks+1] = Y[0]
    # Oppdaterer x
    x = x+h

# Plottar resultatet saman med eksakt løysing
x_eks = np.linspace(x0, x_max, 200)
y_eks = np.exp(-2*x_eks)+2*np.exp(x_eks)-x_eks-1
plt.plot(x_eks, y_eks, 'k-', linewidth=2, 
         label = 'Eksakt')
plt.plot(x_vektor, y_vektor, 'r--', linewidth=2, 
         label = 'Numerisk')
plt.grid(visible=True)
plt.legend(loc='upper left')
plt.show()
