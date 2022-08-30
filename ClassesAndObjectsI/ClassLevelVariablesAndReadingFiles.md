# Class-Level Variables & Reading Files

**Want the variable at the class level?**
Define it outside of the init function and don't pass in self. If you pass in self,
it ends up being a method on each instance created.

If you add it ass an variable when defining the class, it will always be an attribute
available to each instance created.

```
classLevelVariablesAndReadingFiles.py

def stupid_example():
        print(5)

def __init__(self, name):
        self.name = name

Person.stupid_example()

p1 = Person('Aaron')
p2 = Person('King')
```

## Reading Files
***
```
with open('data.txt') as f:
    data = f.read()
```