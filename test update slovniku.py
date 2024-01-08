sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]

counts = dict()

for number in sequence:
    if number not in counts.keys():
        counts.update({number : 1})
    else:
        counts.update({number : counts[number] + 1})

for key, value in sorted(counts.items()):
    print (f'key: {key} value: {value}')