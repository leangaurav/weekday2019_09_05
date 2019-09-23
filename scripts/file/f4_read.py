import sys

print('file', sys.argv[0])

with open(sys.argv[0], 'r') as f:
    s = f.read()
    print(repr(s))