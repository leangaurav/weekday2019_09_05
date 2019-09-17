import sys

if len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        val = int(sys.argv[1])
        print( val * val )
    else:
        print('Input should be of type int !')
else:
    print('Expected 1 value, got ', len(sys.argv) - 1 )
