class Person:

    def __init__(self, name):
        self.name = name
        self.age = 20

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}')