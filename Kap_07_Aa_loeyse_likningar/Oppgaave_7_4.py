""" Dette skriptet reknar ut kor mange elevar det må vere i ei skuleklasse 
for at der mest sannsynleg skal vere minst to elevar med bursdag same dag.
Vi går ut frå at alle fødselsdagar er like sannsynlege og at at fødselsåret 
ikkje var eit skottår.
"""


# Initierer p og n
p = 1
n = 0

while p > 1/2:
    n = n +1                    # Aukar elevtalet
    p = p*(365 - n+1)/365       # Oppdaterer sannsyn

# Skriv resultatet til skjerm
print (f'n = {n}')