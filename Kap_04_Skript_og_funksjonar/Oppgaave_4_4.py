# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Definerer funksjonen
def funk(x):
    return x**2*np.cos(x)

# Reknar ut nokre funksjonsverdiar og skriv dei til skjerm
x1 = 0
funk_val_1 = funk(x1)
x2 = np.pi
funk_val_2 = funk(x2)
print(f'For x = {x1:.4f} er f(x) = {funk_val_1:.4f}')
print(f'For x = {x2:.4f} er f(x) = {funk_val_2:.4f}')
 
# Plottar funksjonen for eit sett med x-verdiar
x = np.linspace(-6, 6, 1000)
f = funk(x)
plt.plot(x, f)
plt.show()