veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = 'aeiouy'
vysledek = dict({'samohlasky':0, 'souhlasky':0})

for pismeno in veta:
    if pismeno in samohlasky:
        vysledek['samohlasky'] += 1
    elif pismeno == " ":
        continue
    else:
        vysledek['souhlasky'] += 1

print(f'Počet souhlásek: {vysledek["souhlasky"]} | Počet samohlásek: {vysledek["samohlasky"]}')