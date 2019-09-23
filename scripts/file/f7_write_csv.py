with open('file.csv', 'w') as out_file:
    for i in range(10):
        print(i, i**2, i ** i, sep=',', file = out_file)
