velikost = 10
symboly = ['#',' ']
sachovnice = []

for radek in range(velikost):
    rada = []
    for bunka in range(velikost):
        index = (radek + bunka) % len(symboly)
        rada.append(symboly[index])
    sachovnice.append(''.join(rada))

print('\n'.join(sachovnice))