cisla = [1, 2, 3, 4, 5, 6, 7, 8]
licha = int()
suda = int()

for cislo in cisla:
    if cislo % 2 == 1:
        licha += cislo
    else:
        suda += cislo

vysledek = abs(licha - suda)

print(f'Rozdíl je: {vysledek}')
