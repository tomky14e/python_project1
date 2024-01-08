vysledek = list()
zadana_cisla = ('1, 2, 3, 4, 5')
cisla = zadana_cisla.split(",")

for cislo in cisla:
    vysledek.append(int(cislo.strip()))

print(f'List: {vysledek}')