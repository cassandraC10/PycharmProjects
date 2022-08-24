#  This is mine, trying to merge.
def UserMenu():
    while True:
        user = input('what is your name?: ')
        print(user, ' Medical Diagnosis')

        user_response = input('What is Your Problem?: ')
        #  ignore the first  reply.
        user_response_again = input('What is Your Problem?: ')

        print(input('Have you had this problem before (yes or no)?: '))
        if user_response.lower() == 'yes':
            print('Well, you have it again.')
        else:
            print('Well, you have it now.')

#  i attempted this, i dont know what i did
#  deleted now, only output print is here
