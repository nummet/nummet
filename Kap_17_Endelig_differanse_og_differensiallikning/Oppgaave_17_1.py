"""Implementeringa løyser startverdiproblemet
a(x) y' + b(x) y = c(x), y(x_0)=y_0.
Koden brukar endeleg differanse-formlar for
numeriske deriverte til å sette opp problemet
som ei matriselikning.
Input:
  1) Funksjonane a(x), b(x) og c(x)
  2) Startkravet, x0 og y0
  3) Maksimalverdi for x, xf
  4) Talet på delintervall, N
Til den siste variabelen brukar vi input-funksjonen.
Dei andre er hardkoda.
"""

# Importerer bibliotek
import numpy as np
import sympy
import matplotlib.pyplot as plt

# Fontstorleik i plotta
plt.rcParams.update({'font.size': 15})

# Inputvariablar
x0 = 0
y0 = 0
xf = 10
# Gir oppdelinga av x-intervallet
N = int(input('Gi talet på delintervall: '))

# Funksjonar
def a(x):
    return np.log(x+1)
    
def b(x):
    return np.exp(-x)
    
def c(x):
    return np.sin(x**2/5)

# Vektor med x-verdiar
h = (xf-x0)/N
x_vektor = np.linspace(x0+h, xf, N)

# Matriser og vektor for funksjonane
A_mat = np.diag(a(x_vektor))
B_mat = np.diag(b(x_vektor))
# reshape() transponerer vektoren til ein søylevektor
C_vektor = c(x_vektor.reshape(-1,1))

# Matrise for den deriverte
# Brukar midtpunktsformelen for numerisk derivasjon
D1_mat = np.zeros((N, N))
for ind in range(1, N-1):
    D1_mat[np.ix_([ind], [ind-1, ind+1])] = \
        np.array([-1, 1])/(2*h)
# Derivert i venstre ende
D1_mat[0, 1] = 1/(2*h)
# Derivert i høgre ende
D1_mat[N-1, (N-3):N] = np.array([1, -4, 3])/(2*h)

# Set opp totalmatrisa
tot_mat =  np.hstack(((np.matmul(A_mat, D1_mat)+B_mat), 
                     C_vektor))
# Legg til startkravet
tot_mat[0,N] = tot_mat[0,N] + a(x0+h) * y0/(2*h)

# Løyser likningssystemet
aux_s = sympy.Matrix(tot_mat).rref()[0]
aux = np.array(aux_s)
y_vektor = np.transpose(aux[:, N])
# Tar med utgangspunktet
y_vektor =  np.insert(y_vektor, 0, y0)
x_vektor =  np.insert(x_vektor, 0, x0)

# Plottar løysinga
plt.plot(x_vektor, y_vektor)
plt.grid(visible=True)
plt.show()