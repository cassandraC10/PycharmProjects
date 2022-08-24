# Display the sum, average, product, smallest and largest of the numbers.
x = int(input('Enter first digit: '))
y = int(input('Enter second digit: '))
z = int(input('Enter third digit: '))

# for number in range(1, 5):
#     print(sum(number))
#     print()

# print(sum(x, y, z))
Sum = x + y + z
average = (Sum / 3)
# print(math.prod(x, y, z))
product = x * y * z
print(min(x, y, z))
print(max(x, y, z))
print(Sum)
print(product)
print(average)
