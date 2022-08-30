# I. Classes And Objects
Intro to Classes and Objects
**How do we program in an Object Oriented way?**

- Figure out the types of objects we will need for our program, and we define them in a Class.
- The Class is simply the blueprint/framework for new object creation. This is great for scalability and maintenance of large systems.
- The object stores k/v data for each instantiated object

![Screen Shot 2022-06-18 at 23.11.34.png](:/43ab4c71accb4828be8e2e1a1be0fa25)

**What is the constructor equivalent for Python?**

- The init method that we create when making a class. This is the function/method that runs/is triggered when we instantiate a new object of a class.

```
Example
def __init__(self, property1, property2):
    self.property1 = property1
    self.property2 = property2
```

**What is Instantiation?**

- We instantiate every time we need a new object, we instantiate the object using the Class as a blueprint for what the object will look like.
- Each instantiation of a class has different data for the properties

```
Example of 2 Instantiations of The Same Class, Leading to the Creation of 2 New Scraper objects

website1 = Scraper('www.google.com', True)
website2 = Scraper('www.yahoo.com', False)
```

* * *

- Anytime you want to give every object access to a custom method, always pass self into the method/function to ensure it connects back to the class.
- "self" is the equivalent of "this" in another language

**What is an attribute/fields/properties/variables/data member?**

- Things that describe our objects makeup and characteristics. Confined to the object it is created for.

**What is a method/function/custom method used for?**
\- It defines behaviors of our objects

```
Example

def performAnAction(self):
    print('HELLO')
    
Call this method
website1.performAnAction()
website2.performAnAction()
```

**What about variables?**

- They define and store our data for the object.

**How do you work with other classes or use a class within another class?**

- We import Enum to utilize its features
- Locate the class that we want to interact with and pass in Enum to the class
- Locate the other classes we want the class to interact with and pass it as a parameter to that class. This gives it access to all of it's attributes and methods.
- When we are creating the enum it is confined and definted within it's particular class we passed it into.
    `from enum import Enum`

**Nested Classes**
**When would you need or use a nested class?**
If a class is only utilized by the one specific class that it is nested under,

### Class and Object Example Diagram

* * *

![Screen Shot 2022-06-18 at 22.11.50.png](:/2086d79c074e499fb9d5f93fcb5b7f72)