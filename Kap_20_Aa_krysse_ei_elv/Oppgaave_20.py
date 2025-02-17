"""Dette skriptet estimerar kor lang tid det tar å krysse ei elv med variabel 
straum - med to ulike strategiar.
Strategi 1 går ut på å alltid kompensere for straumen ved å gjere 
y-komponenten av svømme-farten like stor som straument S(x).
Strategi 2 går ut på at vinkelen theta mellom farten v og x-aksen blir holdt 
fast heile svømmeturen. Vinkelen blir då bestemt av kravet om at ein ikkje 
skal ha noko netto avdrift i y-retning.

Skriptet reknar ut kor lang tid ein brukar med kvar av metodane. I tillegg 
plottar vi banen gjennom elva og framdrifta over elva plotta som funksjon av 
tid.
"""

# Bibliotek
import numpy as np
from matplotlib import pyplot as plt

# Fontstorleik i plotta
plt.rcParams.update({'font.size': 15})

# Input-variablar
D = 20          # Breidda
v = 1           # Svømme-fart
Smax = 0.9      # Maksimal straum
N = 500         # Antal punkt i diskretiseringa


# Funksjon for straum-profil
def S(x):
#    return Smax*np.exp(-(x-D/2)**4/5000)
    return Smax*16/(16+(x-D/3)**2)

# Funksjon som estimerar eit integral ved hjelp av trapes-metoden
def Trapes(x, y):
    L = len(x)                  # Antal punkt
    dx = x[1] - x[0]            # Delta x (antar uniformt grid)
    T = 0.5*dx*(y[0] + y[-1])   # Første og siste punkt
    for i in range(1,L-1):      # Summerar alle andre bidrag
        T = T + dx*y[i]         
    return T

# Tida det tar med strategi 1:
xVektor = np.linspace(0, D, N)
TidVektor = 1/np.sqrt(v**2 - S(xVektor)**2)
T1 = Trapes(xVektor, TidVektor)

# Skriv resultatet til skjerm
print(f'Med strategi 1 brukar vi {T1:.2f} s på å krysse elva')    

# Bestemmer vinkelen for strategi 2
Svektor = S(xVektor)
Int = Trapes(xVektor, Svektor)
theta = np.arcsin(Int/(v*D))
T2 = D**2/np.sqrt((v*D)**2 - Int**2)

# Skriv resultatet til skjerm
print(f'Med strategi 2 brukar vi {T2:.2f} s på å krysse elva')    
    
# Plottar framdrifta som funksjon av tid for strategi 1:
# Tida brukt for kvar \Delta x, strategi 1:
FramdriftTidS1 = np.zeros(N)    # Allokerar
dx = D/(N-1)
FramdriftTidS1[0] = 0
for i in range(1, N):
    x = xVektor[i]
    FramdriftTidS1[i] = FramdriftTidS1[i-1] + \
    dx*1/np.sqrt(v**2 - S(x)**2)

# Strategi 2 gir ei rett linje:
FramdriftTidS2 = xVektor/(v*np.cos(theta))    

plt.figure(1)
plt.clf()
# Strategi 1
plt.plot(FramdriftTidS1, xVektor,'-', color = 'blue', linewidth = 1.5)
# Strategi 2
plt.plot(FramdriftTidS2, xVektor, '-', color = 'red', linewidth = 1.5)
# Markerar sluttidene som loddrette strekar
plt.vlines([T1, T2], 0, D, linestyles = 'dashed', colors = 'black')
# Pyntar på figuren
plt.xlabel('Tid [s]')
plt.ylabel('Framdrift [m]')
plt.ylim(0, D)
plt.grid()
plt.show()


# Plottar avdrift som funksjon av framdrift (strategi 1 har inga avdrift)
TidVektorS2 = np.linspace(0, T2, N)
dt = T2/(N-1)
xVektorS2 = v*np.cos(theta)*TidVektorS2
yVektorS2 = np.zeros(N)
yVektorS2[0] = 0
x = 0
for i in range(1, N):
    x = xVektorS2[i]
    yVektorS2[i] = yVektorS2[i-1] + (v*np.sin(theta) - S(x))*dt
    
plt.figure(2)
plt.clf()
# Strategi 1 (vassrett linje)
plt.plot([0, D], [0, 0], '-', color = 'blue', linewidth = 1.5)
# Strategi 2
plt.plot(xVektorS2, yVektorS2, '-', color = 'red', linewidth = 1.5)    
plt.xlabel('Framdrift [m]')
plt.ylabel('Avdrift [m]')
plt.xlim(0, D)
plt.grid()
plt.show()
