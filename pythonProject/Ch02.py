"""EXAMPLES and EXERCISES"""
"""simple if statements"""
# print('Enter two integers and compare with boolean if statements')
# number1 = int(input('Enter first  integer'))
# number2 = int(input('Enter second integer'))
#
# if number1 == number2:
#     print(number1, 'is equal to ', number2)
# if number1 != number2:
#     print(number1, 'is not equal to ', number2)
# if number1 <= number2:
#     print(number1, 'is less than or equal to ', number2)
# if number1 >= number2:
#     print(number1, 'is greater than or equal to ', number2)
import math

"""Exercise Two"""

"""No 2.2  variable rating:"""
#   rating = input('Enter an integer rating between 1 and 10')
#        ans = it can input even strings, no definition of type

""" No 2.3 (Fill in the missing code)"""
# grade = int(input("Enter the variable grade"))
#
# if grade >= 90:
#     print('Congratulations! Your grade of 91 earns you an A in this course.')

""" No 2.4 (Arithmetic) """
# print(27.5 + 2)
# print(27.5 - 2)
# print(27.5 * 2)
# print(27.5 / 2)
# print(27.5 // 2)
# print(27.5 ** 2)

""" (Circle Area, Diameter and Circumference)"""
# radius = 2
# pi = 3.14159
# diameter = 2 * pi
# circumference = 2 * pi * radius
# area = pi * radius ** 2
#
# print(diameter)
# print(circumference)
# print(area)

""" No 2.6 (Odd or Even)"""
# number = int(input('Enter a number'))
#
# evenNumber = number % 2
#
# if number == evenNumber:
#     print('number is even number')
# if number != evenNumber:
#     print('number is not an even number')  # i tried for my even sha

""" No. 2.7 (Multiples) """
# number = 1024
# anotherNumber = 2
#
# multipleOf1st = 1024%4
# multipleOf2nd = 2%10
#
# if number == multipleOf1st:
#     print(number, ' is a multiple of ', multipleOf1st)
# if number != multipleOf1st:
#     print(number, 'is not a multiple of ', multipleOf1st)
# if anotherNumber == multipleOf2nd:
#     print(anotherNumber, ' is a multiple of ', multipleOf2nd)
# if anotherNumber != multipleOf2nd:
#     print(anotherNumber, 'is not a multiple ', multipleOf2nd)


""" No. 2.8 (Table of Squares and Cubes) """
# number = square = cube = 0
#
# print('number ' '  square ' ' cube')
#
# number = 0
# square = number ** 2
# cube = number * square
# print(number, ' ',  square, ' ', cube, sep='\t')
#
# number = 1
# square = number ** 2
# cube = number * square
# print(number, ' ', square, ' ', cube, sep='\t')
#
# number = 2
# square = number ** 2
# cube = number * square
# print(number, ' ', square, ' ', cube, sep='\t' )
#
# number = 3
# square = number ** 2
# cube = number * square
# print(number, ' ', square, ' ', cube, sep='\t')
#
# number = 4
# square = number ** 2
# cube = number * square
# print(number, ' ', square, ' ', cube, sep = '\t')
#
# number = 5
# square = number ** 2
# cube = number * square
# print(number, ' ', square, ' ', cube, sep='\t')

""" No. 2.9 (Integer value of a character) """

# # print(ord('A'))     B C D b c d 0 1 2 $ * + and the space character
# print(ord('B'))
# print(ord('C'))
# print(ord('D'))
# print(ord('b'))
# print(ord('c'))
# print(ord('d'))
# print(ord('0'))
# print(ord('1'))
# print(ord('2'))
# print(ord('$'))
# print(ord('*'))
# print(ord('+'))
# print(ord(' '))

""" No. 2.10 (Arithmetic, Smallest and Largest) """

# # Display the sum, average, product, smallest and largest of the numbers.
# x = int(input('Enter first digit'))
# y = int(input('Enter second digit'))
# z = int(input('Enter third digit'))
#
# # print(sum(x, y, z))
# sum = x + y + z
# average = ((x + y + z) / 3)
# # print(math.prod(x, y, z))
# product = x * y * z
# print(min(x, y, z))
# print(max(x, y, z))
# print(sum)
# print(product)
# print(average)

"""No. 2.11 (Separating the Digits in an Integer)"""
# number = int(input('Enter five digit integer'))
# #print(number, number, number, number, number, sep='\t')
# # i didnt get it, can't seperate them
# #correction
# # integer = int(input('Enter five digit integer'))
# for integer in '12345':
#     print(integer, end='\t')
#     # dont use sep, it prints line by line, end will sep on a straight line


"""No. 2.12 (7% Investment Return)"""
p = 1000
r = 7  # %
for year in range(1, 11):
    a = p * (1 + r) ** year
    # print(f'{year:>2}{a:>10.2f}', end=' ')
    print('amount after 10 years is: ', a)

# After entering chapter 3, my answer doesnt make me satisfied
# honestly i feel tired, i had a real real bad day, nothing is just working

"""No. 2.13 (How Big Can Python Integers Be?)"""
# x = 123456123456123456123456 ** 78910
# print(x)
# # Python integers can be very very big,

"""No. 2.14 (Target Heart-Rate Calculator)"""
# user_age = int(input('Enter your age'))
# max_heart_rate = 220 - user_age
# print('your maximum heart rate is ', max_heart_rate)
# percentage = 50 / 100 * max_heart_rate
# print(percentage)
# Target_heartrate = percentage * max_heart_rate
# print('your target heart rate is ', Target_heartrate)

"""No. 2.15 (Sort in Ascending Order) """
# user_input = float(input('Enter first number')), float(input('Enter second number')), float(input('Enter third number'))
# # if number1 > number2:
# #     print('number 1 is greater than number 2')
# # i am lost, have an idea of what to type, but it'll waste my time
# """Correction"""
# # built in functions
# print(sorted(user_input))
