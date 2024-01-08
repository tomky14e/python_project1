jmena = [
 'Michal', 'Pepa', 'Honza',
 'Pavel', 'Lukas', 'Matej',
 'Iva', 'Klara', 'Jana',
 'Honza', 'Vasek','Milan',
 'Michal'
]

kopie_jmen = jmena.copy()

for i in range(len(kopie_jmen)):
    for j in range(i + 1, len(kopie_jmen)):
        if kopie_jmen[i] > kopie_jmen[j]:
            kopie_jmen[i], kopie_jmen[j] = kopie_jmen[j], kopie_jmen[i]

print(kopie_jmen)    