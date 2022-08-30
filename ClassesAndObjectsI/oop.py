from enum import Enum

class PersonType(Enum):
    ADMIN = 0
    USER = 1
    SUPER_USER = 2
    
class Person:
    # This is basically that is generate to create a new Person object
    def __init__(self, name, age, person_type, personTypeNestedExample): # self is required and the extra params are attributes each person object should have access to
        self.name = name
        self.age = age
        self.personType = person_type
        self.personTypeNestedExample = personTypeNestedExample
        
        """Custom Method Creation
        """
    def greet(self):
        print(f'My name is {self.name}, my age is {self.age}, and I currently serve the role as {self.personType}/{self.personTypeNestedExample}!')
        
        
    class PersonTypeNestedExample(Enum):
        NESTED_BRO = 0
        NESTED_SIS = 1
        NESTED_TRANS = 2
        
p = Person('Aaron', 35, PersonType.SUPER_USER, Person.PersonTypeNestedExample.NESTED_BRO)
p2 = Person('Deez', 19, PersonType.ADMIN, Person.PersonTypeNestedExample.NESTED_SIS)
p3 = Person('Caleb', 79, PersonType.SUPER_USER, Person.PersonTypeNestedExample.NESTED_TRANS)

p.greet()
p2.greet()
p3.greet()

class Position:
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom
        
    def __str__(self):
        return f'Pan: {self.pan}, Tilt: {self.tilt}, Zoom: {self.zoom}'
    
    def __eq__(self, other):
        return self.pan == other.pan and self.tilt == other.tilt and self.zoom == other.zoom
    
    __hash__ = None

class Camera:
    
    def readCameraData():
        with open('ClassesAndObjectsI/cameras.txt') as f:
            cameraData = f.read()
            
        cameraDataArr = cameraData.split()
        serial_number = cameraDataArr[0]
        position = Position(int(cameraDataArr[1]), int(cameraDataArr[2]), int(cameraDataArr[3]))
        camera_type = Camera.CameraType[cameraDataArr[4]]
        c = Camera(serial_number,position, camera_type)
        return c
     
        
    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type
        
    def __str__(self):
        return f'Serial Number: {self.serial_number}, Camera Type: {self.camera_type}, Position: {self.position.__str__()}'
    
    def __eq__(self, other):
        return self.serial_number == other.serial_number and self.position == other.position and self.camera_type == other.camera_type
    
    __hash__ = None
    
    class CameraType(Enum):
        ptz = 0
        eptz = 1
        stationary = 2

c =Camera.readCameraData()
print(c)