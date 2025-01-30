"""Implementering av Eulers framovermetode for svinvelikninga.
Input: Startkravet y(x0)=y0, y'(x0)=u0 og F(x,y), som definerer 
differensiallikninga ved Y'=F(Y), der Y=[y, u]^T, y' = u og u' = -5*sin(y).
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
for indeks in range(0, N):
    # Eulers midtpunktsmetode
    x_hatt = x + h/2
    y_hatt = Y + F(x,Y)*h/2
    Y = Y + F(x_hatt,y_hatt)*h
    # Oppdaterer vektor med y-verdiar
    y_vektor[indeks+1] = Y[0]
    # Oppdaterer x
    x = x+h


# Plottar resultatet saman med tilnærma, analytisk løysing
plt.figure(1)
plt.clf()
y_eks = y0*np.cos(np.sqrt(5)*x_vektor)
plt.plot(x_vektor, y_eks, 'k-', linewidth=2, 
         label = 'Analytisk tilnærming')
plt.plot(x_vektor, y_vektor, 'r--', linewidth=2, 
         label = 'Numerisk')
plt.grid(visible=True)
plt.legend(loc='upper left')
plt.show()

# Plottar differansen mellom numerisk løysing og analytisk tilnærming
plt.figure(2)
plt.clf()
plt.plot(x_vektor, y_eks-y_vektor, 'k-', linewidth=2)
plt.hlines([-0.1*y0, 0.1*y0], x0, x_max, colors='red', linestyles='--')
plt.grid(visible=True)
plt.show()