"""
Dette skriptet testar kandidatar til reknereglar for matriser. For å teste 
brukar vi 3*3-matriser med tilfeldige tal mellom -5 og 5.
"""

# Importerar NumPy
import numpy as np

# Lagar matriser med tilfeldige tal
A = 10*(np.random.rand(3, 3) - 0.5*np.ones((3,3)))
B = 10*(np.random.rand(3, 3) - 0.5*np.ones((3,3)))

# Venstresida i "rekneregelen"
VS = A + B
# Høgresida
HS = B + A

# Skriv differansen til skjerm - for å sjå om det blir nullmatrisa
print(VS - HS)  