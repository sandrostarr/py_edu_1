class A:
    property1 = 'Property 1'
    property2 = 'Property 2'

    def say_hi(self, name='guest'):
        return 'Hi, ' + name


a = A()
# a.property1 = 'Property 1'
# a.property2 = 'Property 2'
# print(a)

print(a.property1)

print(a.say_hi())