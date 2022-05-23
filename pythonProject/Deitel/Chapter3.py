# student_grade = 75
# if student_grade >= 90:
#     print('A')
# elif student_grade >= 80:
#     print('B')
# elif student_grade >= 80:
#     print('B')
# elif student_grade >= 70:
#     print('C')
# elif student_grade >= 60:
#     print('D')
# else:
#     print('F, you failed')
#
# result = ('passed' if student_grade >= 60 else 'failed')
# print(result)

# product = 7
# while product <= 1000:
#     product = product * 7
#     print(product)
#
# for character in 'programming':
#     print(character, end='    ')

# for number in range(10):
#     print(number, end='    ')
#
# total = 0
# # for number in range(1000):
# #     total = total + number
# #     print(total)
# for number in [1, 2, 3, 4, 5]:
#     total += number
#     print(total)

# """Using sequence controlled iteration"""
# total = 0
# grade_counter = 0

# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

# for grade in grades:
#     total += grade
#     grade_counter += 1
# Average = total / grade_counter
# print('Your average score is: ', Average)


"""Using sentinel controlled iteration"""
# total = 0
# grade_counter = 0
#
# grade = int(input('Enter grade, end with -1 as sentinel: '))
#
# while grade != -1:
#     total += grade
#     grade_counter += 1
#     grade = int(input('Enter grade, end with -1 as sentinel: '))
#
# if grade_counter != 0:
#     average = total / grade_counter
#     print(f' The average grade score is {average: .3f}')
#     # print('The average grade score is ', average)
# else:
#     print('No grades were entered')

""" A program to summarize results and bonus instructor"""

# passes = 0
# failures = 0
#
# for student in range(10):
#     result = int(input('input exam result: '))
#
#     if result >= 5:
#         passes += 1
#     else:
#         failures += 1
#
# print('number of passes is: ', passes)
# print('number of failures is: ', failures)
#
# if passes >= 8:
#     print('Bonus to instructor')

# # for number in range(0, 100, 5):
# for number in range(100, 0, -5):
#     print(number, end=' ')

# for number in range(10, 0, 2):
#     print(number, end=' ')

# values = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]
# for values in values:
#     print(values, end=' ')

# sum_of_numbers = 0
# for number in range(2, 101, 2):
#     sum_of_numbers += number
#     print(sum_of_numbers)

# principal = Decimal('1000.00')
# print(principal)
# x = Decimal('25.5')
# y = Decimal('5')
#
# print(x + y)
# print(x * y)
# print(x // y)
# print(x - y)


# principal = 1000
# rate = 5
# for year in range(1, 11):
#     amount = principal * (1 + rate) ** year
#     print('your amount in 10 years is : ', amount)

# principal = 1000
# rate = 7
# for year in range(1, 11):
#     amount = principal * (1 + rate) ** year
#     print('your amount in 10 years is : ', amount)

# principal = 1000
# rate = 5
# year = 10
# amount = principal * (1 + rate) ** year
# print('your amount in 10 years is : ', amount)

# from decimal import Decimal
#
# print(f"{Decimal('37.45') * Decimal('1.0625'):.2f}")

i, j, k, m = 1, 2, 3, 4
var = (i >= 1) and (j < 4)
print(var)
