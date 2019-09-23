import sys

with open('temp.txt', 'r') as f:
    s = f.read(4)
    while len(s) != 0:
        print(repr(s))
        s = f.read(4)
        
    print("Pointer at: ", f.tell())
    print('Re read: ', f.read(10))
    
    f.seek(0) # bring pointer to beginning
    print("Pointer at: ", f.tell())
    print('Re read 2 : ', f.read(10))