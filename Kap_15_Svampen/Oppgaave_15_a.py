"""Implementeriga estimerar volum og overflate av ein bygning gitt
med ein profilfunksjon. Til det brukar den både trapesintegrasjon og
midtpunktsformelen for numerisk integrasjon.
"""

# Importerar NumPy
import numpy as np

# Grenser (høgda)
a = 0
b = 60

def R(x):
    """Profil på tårn"""
    return 5+4/(1+np.exp((35-x)/1.5))*(np.sqrt(np.abs(x+ \
        1))-np.sqrt(31))**2

dx = 1e-3           # Liten verdi for numerisk derivasjon
def Rd(x):
    """Derivert"""
    return (R(x+dx)-R(x-dx))/(2*dx)

def int_volum(x):
    """Integrand for volumet"""
    return R(x)**2

def int_overflate(x):
    """Integrand for overflata"""
    return R(x) * np.sqrt(1+Rd(x)**2)


# Oppdeling
n = int(input('Gi oppdelinga n: '))
h = (b-a)/n                  # Steglengda

# Integrerer for å finne volum og overflate
# Bidrag frå endane
volum = h/2*(int_volum(a) + int_volum(b))
overflate = h/2*(int_overflate(a) + int_overflate(b))
# Resten av bidraga
for i in range(1, n):
    xi = a+i*h
    volum = volum + h*int_volum(xi)
    overflate = overflate + h*int_overflate(xi)
    
# Gange med rette faktorar til slutt
volum = np.pi*volum    
overflate = 2*np.pi*overflate

# Skriv volum og overflata til skjerm
print(f'Volum: {volum:.1f} m^3')
print(f'overflate = {overflate:.1f} m^2')