"""Implementeringa løyser likninga  \int_(mu-b)^(mu+b) f(x) dx = 1/2
ved hjelp av Newtons metode. f(x) er ein Gauss-funksjon med middelverdi mu 
og standardavvik sigma. I tillegg har koden inputparametrane N og b0, der N
er talet på punkt brukt i eit trapesestimat av integralet over, og b0 er 
startgjettinga for b. Implementeringa brukar funksjonen int_gauss(...) til 
å estimere integralet.
"""

# Importerar NumPy
import numpy as np

def gauss_funk(x):
    """Gauss-funksjonen"""
    return 1/sigma/np.sqrt(2*np.pi) * \
            np.exp(-(x-mu)**2/2/sigma**2)

def int_gauss(mu, sigma, b, N):
    """Funksjon som estimerer     
    int_(mu-b)^(mu+b) f(x) dx - 1/2 for Gauss-funksjonen
    f(x)=1/(2*sqrt(2*pi))*exp(-(x-mu)^2/(2*sigma^2)).
    Integralet blir estimert ved trapesintegrasjon,
    inputvariabelen N gir talet på punkt brukt i estimatet.
    """
    
    # Bestemmer steglengda
    h = 2*b/N
    
    # Startverdi for x
    x = mu-b
    
    #Endepunkt:
    integral = (gauss_funk(mu-b)+gauss_funk(mu+b))/2
    
    # for-løkke som går over alle "indre" punkt
    for ind in range(1, N):
        x = x+h
        integral = integral+gauss_funk(x)
    
    # Gangar summen med steglengda h for å få integralet
    integral = integral*h
    
    # Bestemmer funksjonen G
    return integral-1/2


# Input-parametrar
mu = 4
sigma = 2
N = int(input('Talet på punkt i trapesintegrasjon: '))
# Start-gjetning
b0 = 1                          

# Fikserer presisjonen
pres = 1e-5

# Set meir eller mindre tilfeldig verdi for b_gml
b_gml = 10
b = b0

# Itererer til vi får den presisjonen vi vil ha
while abs(b-b_gml) > pres:
    b_gml = b
    g = int_gauss(mu, sigma, b, N)
    nemnar = 2*gauss_funk(mu+b)
    b = b-g/nemnar

# Skriv svaret til skjerm
print(f'b = {b:.4f}')