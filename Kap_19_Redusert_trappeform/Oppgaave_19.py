"""Denne implementeringar rekkereduserar ei matrise til redusert
trappeform. Den aktuelle matrisa er gitt (hardkoda) i starten av skriptet.
Denne blir redusert til redusert trappeform. Til slutt blir tilsvarande
resultat funne med rref-funksjonen frå SymPy.

Implementeringa er delt inn ei rekke under-funksjonar.

Til sist blir input-matrisa og dei to resultata av rekkereduksjonen skrivne
til skjerm.
"""
# Importerar bibliotek og set utskriftsformat
import numpy as np
np.set_printoptions(linewidth=400)
np.set_printoptions(formatter={'all': lambda x: f"{x:.2f}"})
import sympy

# Tilordnar input-matrisa
A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])



def bakoverfase(A, leiar_vektor):
    """Denne funksjonen tar utgangspunkt i ei matrise på
    trappeform og ein vektor med søylenummera til alle
    leiande tal. Den sørger for at alle leiande tal blir
    ein og alle tal over desse blir null.
    Input: 
    A - matrise på trappeform
    leiar_vektor - vektor med nummeret på leiande søyler
    Elementa i leiar_vektor må komme i stigande rekkefølge.
    """

    # Kopierer matrisa og finn formatet
    M = np.copy(A)
    
    m = A.shape[0]
    n = A.shape[1]
    
    # Bestemmer talet på leiande tal
    v = len(leiar_vektor)
    
    # Går gjennom dei leiande tala - nedanfrå
    for rekke in range(v-1, -1, -1):
        soeyle = leiar_vektor[rekke]   # Den aktuelle søyla
        blokk = M[0:rekke+1, soeyle:n] # Hentar ut blokk
        k_inv = blokk[rekke, 0]        # Det leiande talet
        # Set dette til 1
        blokk = gonge_rekke(blokk, 1/k_inv, rekke)
        # Gjer tala over det leiande talet til null
        for p in range(0, rekke):
            k = -blokk[p, 0]
            blokk = legge_til_mult(blokk, k, rekke, p)
            # Oppdaterer matrisa    
            M[0:rekke+1, soeyle:n] = blokk

    return M

###

def byte_rekker(A, m, n):
    """Funksjon som byter om to rekker i ei matrise
    
    Input:
    A: Matrisa som skal endrast.
    m og n: Rekkene som skal bytast om.
    """
    
    M = np.copy(A)    
    M[[m, n],:] = A[[n, m],:]

    return M
    
###
    
def gonge_rekke(A, k, m):
    """Funksjon som gongar ei rekke i ei matrise 
    med eit tal ulik null
    
    Input:
    A: Matrisa som skal endrast.
    k: Talet det skal gongast med.
    m: Rekka som skal gongast med dette talet.
    """
    
    if abs(k) < 1e-14:
        print('Talet får ikkje vere null.')
        return None
    
    M = np.copy(A)
    M[m, :] = k * A[m, :]

    return M
    
###

def legge_til_mult(A, k, m, n):
    """Funksjon som legg eit multiplum av ei rekke til ei anna rekke i 
    ei matrise.

    Input:
    A: Matrisa som skal endrast.
    k: Talet det skal gongast med.
    m: Rekka som skal gongast med k og leggast til n.
    n: Rekka som vi skal legge til k gongar rekke m.
    """
    
    M = np.copy(A)
    M[n, :] = A[n, :] + k*A[m, :]

    return M

###

def RTF(A):
    """Funksjon som rekkereduserer ei matrise til redusert trappeform. 
    Funksjonen brukar først funksjonsfila Trappeform, som reduserer 
    matrisa til ei trappeform. Kvart steg i denne prosessen blir utført 
    i funksjonsfila Trappesteg. Når matrisa er redusert til 
    trappeform, går vi vidare til redusert trappeform med funksjonen 
    Bakoverfase. Fleire av desse funksjonsfilene brukar funksjonfiler 
    som implementerer dei tre elementære rekkeoperasjonane. Desse er:
    ByteRekker
    GongeRekke
    LeggeTilMult
    """
    
    # Får matrisa på trappeform og finn søylene med 
    # leiande tal
    M, leiar_vektor = trappeform(A)
    
    # Finn talet på leiande tal
    v = len(leiar_vektor)
    
    # Viss der er leiande tal: Utfører "bakoverfasen",
    # som går ut på å sette alle leiande tal til 1 og
    # gjere alle tal over desse til null.
    if v > 0:
        M = bakoverfase(M, leiar_vektor)

    return M

###

def trappeform(A):
    """Funksjon som reduserer ei matrise til ei trappeform. Funksjonen 
    lagar også ein vektor med søylenummera til søylene med leiande tal.
    """
    
    # Finn formatet på matrisa
    m = A.shape[0]
    n = A.shape[1]
    
    # Kopierer matrisa
    M = np.copy(A)
    
    # Initierer vektoren med søylenummera for 
    # dei leiande tala
    leiar_vektor = []
    # Set rekkenummeret til null
    rekke = 0
    # Går gjennom kvar søyle i matrisa og rekkereduserer for
    # kvar undermatrise
    
    for soeyle in range(0, n):
        # Hentar ut relevant underblokk av matrisa
        blokk = M[rekke:m, soeyle:n]
        # Rekkeopererer på blokka slik at første søyle får
        # rett struktur
        # Undersøker også om søyla har leiande tal
        blokk, leiar = trappesteg(blokk, m-rekke)
        # Oppdaterer dersom søyla har leiande tal
        if leiar == 1:
            # Oppdaterer vektor med leiande tal
            leiar_vektor.append(soeyle)
            # Oppdaterer den store matrisa
            M[rekke:m, soeyle:n] = blokk
            # Oppdaterer rekketalet
            rekke = rekke+1
    
    return M, leiar_vektor

###

def trappesteg(A, m):
    """Funksjon som omstrukturerer første søyle i ei matrise 
    slik at dette blir første steg mot å få matrisa på 
    trappeform. Input er matrisa som skal rekkereduserast
    og talet på rekker i denne. Output er den 
    modifiserte matrisa og ein indeks som er 1 dersom
    søyla har leiande tal og 0 viss ikkje.
    Input:
    A - Matrisa som skal rekkereduserast
    m - talet på rekker i matrisa
    """
    
    # Kopierer matrisa
    M = np.copy(A)
    
    # Leitar etter eit tal ulik null i søyle 1
    indeks = 0
    while indeks <= m-1 and np.abs(A[indeks, 0]) < 1e-14:
        indeks = indeks+1
    
    # Viss det er ei rein nullsøyle
    if indeks == m:
        # Set at søyla ikkje har leiande tal
        leiar = 0
        # Går ut av funksjonen
        return None, leiar 
    
    # Set at søyla har eit leiande tal
    leiar = 1
    
    # Sørger for å ha tal ulik null oppe til venstre
    if indeks > 0:
        M = byte_rekker(M, 0, indeks)
    
    # Gjer alle tala under det leiande talet til null
    m11 = M[0, 0]
    for indeks in range(1, m):
        # Finn talet vi skal gonge med
        k = -M[indeks, 0]/m11
        # Legg til slik at vi får null
        M = legge_til_mult(M, k, 0, indeks)
    
    return M, leiar

# Rekkereduserar og skriv til skjerm
print(f'A =\n {A}')
print(f'RTF(A) =\n {RTF(A)}')

# SymPy-versjonen:
RREF_sp = sympy.Matrix(A).rref()[0]
# Konvertere frå symbolsk til flyttal
RREF_sp = np.array(RREF_sp, dtype = float)
print(f'Frå SymPy:\n {RREF_sp}')