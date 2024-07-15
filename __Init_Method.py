# __init__ is a contructor method in Python and is automatically called to allocate memory when
# a new object/instance is created. All classes have a __init__ method associated with them. 
# It helps in distinguishing methods and attributes of a class from local variables.

class Student:
    def __init__(self, name,roll,age):
        self.name = name 
        self.age = age 
        self.roll = roll
    def displayData(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Roll: ",self.roll)
        
s1 = Student("Tukaram",16,22)
s1.displayData()        