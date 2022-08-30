# Creating Class Level Variables
class Person:
    
    def stupid_example():
        print(5)
    
    def __init__(self, name):
        self.name = name
        
Person.stupid_example()

p1 = Person('Aaron')
p2 = Person('King')


# Reading Files

with open('ClassesAndObjectsI/data.txt') as f:
    data = f.read()

print(data)