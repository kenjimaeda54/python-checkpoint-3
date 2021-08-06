d = {'cachorro': 2, 'gato': 3, 'elefante': 1}

for i in sorted(d, key=d.get):
    print(i, d[i])
