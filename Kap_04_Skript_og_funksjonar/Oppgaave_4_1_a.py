"""Dette skriptet plottar to funksjonar."""

# Importerer biblioteka vi treng
import numpy as np
import matplotlib.pyplot as plt

# Vektor med argumentverdiar
x = np.linspace(-5.0, 5.0, 200)
# Vektorar med funksjonsverdiar
y = np.sin(np.exp(x))
z = np.exp(np.sin(x))

# Plottar funksjonane saman
plt.plot(x, y, 'b-')
plt.plot(x, z, 'r-')
plt.show()