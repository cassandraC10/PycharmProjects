def signup():
    username = str(input("Go ahead, name your Diary: "))
    if any(users["username"] == username for users in users_access_details):
        print("\n * 15")
        print("Oops username already exists")