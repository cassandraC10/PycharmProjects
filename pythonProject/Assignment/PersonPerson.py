from dataclasses import dataclass

# from pythonProject.Assignment.Person import Person


@dataclass
class Person:
    name: str
    age: int

    def is_minor(self):
        return self.age < 18

person1 = Person("Cassie", 23)
person2 = Person("Cassandra", 19)

print(person1.is_minor())
person1.name = "Shindara"
print(person1)