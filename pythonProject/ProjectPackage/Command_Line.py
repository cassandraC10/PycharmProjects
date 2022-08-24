import sys

print(len(sys.argv))
for arg in sys.argv:
    print(arg)
try:
    total = sum(int (arg) for arg in sys.argv[1:])
    print('total:', total)
except ValueError:
    print('Value error: requires zero or more integer command line argument')