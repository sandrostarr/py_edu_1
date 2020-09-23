class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}')


class Employee(Person):
