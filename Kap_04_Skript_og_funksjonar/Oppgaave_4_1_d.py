"""Skript som reknar ut kva eit beløp i NOK tilsvarar i
pund, euro og svenske kroner. Dei aktuelle kursane er
fiksert i skriptet.
"""

# Kursar
kurs_euro = 11.50
kurs_pund = 12.81
kurs_SVK = 101.30/100

# Les inn beølp i NOK:
NOK = float(input('Beløp i norske kroner: '))

# Resultat
belop_euro = NOK/kurs_euro
belop_pund = NOK/kurs_pund
belop_SVK = NOK/kurs_SVK
# Skriv resultata til skjerm
print(f'Beløp i euro: {belop_euro:.2f}')
print(f'Beløp i pund: {belop_pund:.2f}')
print(f'Beløp i svenske kroner: {belop_SVK:.2f}')