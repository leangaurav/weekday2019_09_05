f = open('temp.txt', 'w')

for i in range(10):
    print(i, file = f)

f.close()