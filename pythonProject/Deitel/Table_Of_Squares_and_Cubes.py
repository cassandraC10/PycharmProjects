print('number\t' '  square\t' 'cube\t')

for x in range(0, 6):
    print('{0:6d}\t {1:7d}\t {2:3d}'.format(x, x * x, x * x * x))
