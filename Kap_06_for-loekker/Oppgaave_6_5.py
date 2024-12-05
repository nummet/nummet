"""I dette skriptet implementerar vi fakultetsfunksjonen. 
I tillegg testar vi denne funksjonen for nokre verdiar.
"""

# Implementering av fakultetsfunksjonen
def fakultet(n):
    """Funksjon som reknar ut n! - n fakultet.
    n må vere eit naturleg tal.
    """
    
    f = 1       # Set startverdien til 1

    for i in range(1,n+1):
        f = f*i # Gongar med neste faktor

    return f

# Reknar ut nokre funksjonsverdiar
print(f'fakultet(0) = {fakultet(0)}')
print(f'fakultet(4) = {fakultet(4)}')
print(f'fakultet(10) = {fakultet(10)}')
print(f'fakultet(20) = {fakultet(20)}') 
