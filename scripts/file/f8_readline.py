import sys

with open('temp.txt', 'r') as f:
    s = f.readline()
    while len(s) != 0:
        print(repr(s))
        s = f.readline()