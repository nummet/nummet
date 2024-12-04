"""Dette skriptet plottar tre funksjonar."""

# Importerer bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Vektor med argumentverdiar
x = np.linspace(-5, 7, 500)
# Vektorar med funksjonsverdiar
y = np.sin(np.exp(x))
z = np.exp(np.sin(x))
f = np.cos(np.exp(x))

# Plottar funksjonane saman
plt.plot(x, y, 'b-')
plt.plot(x, z, 'r-')
plt.plot(x, f, 'g-')
plt.show()