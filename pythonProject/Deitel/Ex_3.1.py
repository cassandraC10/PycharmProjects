""" Validating user input """
passes = 0
failures = 0
for student in range(10):
    result = 0
    while result not in [1, 2]:
        result = int(input('input exam result (1=pass, 2=fail): '))

    if result == 1:
        passes += 1
    else:
        failures += 1

print('number of passes is: ', passes)
print('number of failures is: ', failures)

if passes >= 8:
    print('Bonus to instructor')

#  GIVING INFINITE LOOP & I DONT KNOW WHY!!!!!
