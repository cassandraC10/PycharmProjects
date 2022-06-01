# from datetime import datetime
#
#
# def __init__(self, name, surname, birthdate, address, telephone, email):
#     self.name = name
#     self.surname = surname
#     self.birthdate = birthdate
#
#     self.address = address
#     self.telephone = telephone
#     self.email = email
#
#
# def age(self):
#     today = datetime.date.today()
#     age = today.year - self.birthdate.year
#
#     if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#         age -= 1
#
#     return age
#

class Person:
    pass


# person = Person(
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12),  # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jane.doe@example.com"
# )
#
# print(person.name)
# print(person.email)
# print(person.age())
#
# def age(self):
#     if hasattr(self, "_age"):
#         return self._age
#
#     today = datetime.date.today()
#
#     age = today.year - self.birthdate.year
#
#     if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#         age -= 1
#
#     self._age = age
#     return age

class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname, age):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return
    def __str__(self):
        return f"your name {self.name}"

    def __eg__(self, other):
        return self.name == other.name and other.age == self.age


    p1 = Person("Cassie", 23)
    p2 = Person("Cassandra, 19")

    print(p1)
