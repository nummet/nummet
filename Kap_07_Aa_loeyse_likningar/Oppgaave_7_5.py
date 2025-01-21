"""I dette skriptet har vi implementert ein funksjon som finn løysinga av 
tredjegradslikninga. I tillegg har vi brukt det til å rekne ut løysinga av 
ei tredjegradslikning - gitt ved input-parametrane a, b, c og d i likninga
a x^3 + b x^2 + c x + d = 0.
"""

# Inporterar NumPy
import numpy as np

def kubikkrot(x):
    """Funksjon som gjer at vi kan ta kubikk-rota av 
    negative tal
    """
    if x>0:
        return x**(1/3)
    else:
        return -abs(x)**(1/3)

def tredjegrads_funk(a,b,c,d):
    """Funksjon som løyser tredjegradslikninga
    ax^3+bx^2+cx+d=0.
    Input er koeffisientane a, b, c, d.
    Funksjonen gir dei tre løysingane x_1, x_2 og x_3
    som output.
    """
    
    # Kontrollerer at det faktisk er ei tredjegradslikning
    if a == 0:
        print('Dette er ikkje ei tredjegradslikning')
        return None
    
    # Tilordnar parametrar som inngår i løysingsformelen
    # Vektor med u_1, u_2 og u_3:
    u = np.array([1, complex(-1, np.sqrt(3))/2, 
                  complex(-1, -np.sqrt(3))/2])
    delta_0 = b**2-3*a*c
    delta_1 = 2*b**3-9*a*b*c+27*a**2*d
    
    # Stor C. NB! Ulik input-variabelen c.
    C = kubikkrot((delta_1+np.sqrt(complex(delta_1**2-
        4*delta_0**3)))/2)
    
    # Løysinga
    if abs(delta_0) < 1e-14 and abs(delta_1) < 1e-14:
        # Spesialtilfelle: 3 like røter
        x = -b/(3*a)
    elif abs(delta_0) < 1e-14 and delta_1 < 0:
        # Endrar C i dette tilfellet
        C = kubikkrot(delta_1)
        x = -1/(3*a)*(b+u*C+delta_0/(u*C))
    else:
        x = -1/(3*a)*(b+u*C+delta_0/(u*C))
        
    return x

# Set opp koeffisientane i ei tredjegradslikning, løyser likninga og skriv
# løysingane til skjerm
a = 1
b = 1
c = 2
d = -1
x = tredjegrads_funk(a, b, c, d)
print(x)