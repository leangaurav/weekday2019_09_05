import sys

with open('temp.txt', 'r') as f:
    s = f.read(4)
    while len(s) != 0:
        print(repr(s))
        s = f.read(4)