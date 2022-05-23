# user_access_details = [{'username': 'Cassandra', 'password': 'Cassie123'},
#                        {'username': 'Cynthia', 'password': 'love234'},
#                        {'username': 'Adebola', 'password': 'password123'}]

user_access_details = {
    'favourite_food': ['rice and chicken', 'beans', 'semo'],
    'favourite_movie': ['Xmen', 'Tom & jerry'],
    'favourite_music': ['trap_nation'],
    'favourite_color': ['neon', 'black', 'white']
}


def check_type(favourite_food, favourite_movie, favourite_music, favourite_color):
    for key, value in user_access_details.items():
        print(type(user_access_details))


if __name__ == "__main__":
    print(check_type)

# def check_list(username, password):
#     # code to be written here, to check if user exists
#
#     for users in user_access_details:
#         if users['username'] == username and users['password'] == password:
#             print(users)
#
#
# if __name__ == "__main__":
#     print(check_list("Cassandra", "Cassie123"))
