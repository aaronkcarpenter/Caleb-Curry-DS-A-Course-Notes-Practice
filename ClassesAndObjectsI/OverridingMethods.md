# Overriding Methods/Custom Objects
When we are within a cusom class, we can create a method named `__str__`, and it will automatically override the current implementation.
- Methods inside of Python are `virtual` , meaning it can be overridden. 
	- Methods/Examples Discussed
		- `__str__` - Custom String Method
		- `__eq__` - Customer Equality Checker Method
		- `__hash__` - Custom Hash Method 
			- Option 1: Setting the Custom `__hash__ = None` to none
			- Option 2: Creating the actual custom method
```
Example of Overriding A Method

class Person:
	def __init__(self, name):
		self.name = name

<!-- Method/Function that return the name of a Person object created -->
	def __str__(self):
		return f'{self.name}'
		
<!-- Method/Function that checks for equality of 2 things based off of their value, not off of the space in memory they hold. == for value comparison and 'is' for memory location comparison -->
	def __eq__(self, other):
		return self.name == other.name

<!-- Saying NO THANKS to the hash and not having one for our custom object. Meaning, it is unusable for any that require hashing-->
	__hash__ = None
<!--  Implementing your own custom version of hash for your class(NOT REALLY REQUIRED-->
	def __hash__(self):
		return hash(self.name)
		
		
<!-- Instantiating A New Person Object -->
	p = Person('Aaron')
	p2 = Person('Aaron')
	print(p)
	
<!-- 	Hash Example -->
	people = {p1: p2} --> NO, CANT DO
	people = { 'person': p2} --> YES, CAN DO
```