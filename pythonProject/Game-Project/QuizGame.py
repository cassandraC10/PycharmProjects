print('Welcome to Python Quiz Game')
answer = input('Are you ready to play the Quiz ? (yes/no): ')
score = 0
total_questions = 3

if answer.lower() == 'yes:':
    answer = input('Question 1: Is Python an interpreted language ')
    if answer.lower() == 'yes':
        score += 1
        print('correct!')
    else:
        print('Wrong. Python is an interpreted language :( ')

    answer = input('Question 2: A module is a group of python commands (True/False)')
    if answer.lower() == 'false':
        score += 1
        print('Correct !')
    else:
        print('False. A module is a file of python commands')

    answer = input('Question 3: python is not a dynamically typed language ? (True/False)')
    if answer.lower() == 'false':
        score += 1
        print('Correct !')
    else:
        print('False. Python is a dynamically typed language')

print('You attempted', score, 'questions correctly!')
mark = (score/total_questions) * 100
print('marks obtained: ', mark)
print('Thank you for playing Python Quiz Game !')