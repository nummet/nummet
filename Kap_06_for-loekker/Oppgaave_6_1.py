# Set summen til 0
s = 0

for i in range(1, 11):  # Bestemmer summasjonsgrensene
    s = s + i**2        # Legg til eit ledd

# Skriv summen til skjerm:
print(f's = {s:.4f}')