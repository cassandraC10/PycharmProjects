""" Using a FOR loop """
List = range(7)
runningTotal = []
total = 0
for n in List:
    total += n
    runningTotal.append(total)
    print("The sum of total using FOR loop is: ", total)

""" Using a WHILE loop """
# while List > 0:
#     List -= 1
#     total += List
#     print("Total of numbers in list using WHILE loop is: ", total)

number = 6
while number > 0:
    number -= 1
    total += number
    print("Total of numbers in list using WHILE loop is: ", total)

""" PYTHON DOESN'T USE DO WHILE """
""" Using DO WHILE loop """
# while True:
#     print("Total of numbers in list using DO-WHILE loop is:", number)
#     number -= 1
#     total += number
#     if number > 0:
#         break

