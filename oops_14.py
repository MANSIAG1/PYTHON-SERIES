# Defining a Class
class Student:
    # Class attribute (shared by all instances)
    name = "mansi"

# Creating an Object (Instance) of the Class
s1 = Student()

# Accessing the Class Attribute through the Object
print(s1.name)  # Output: mansi

# Another Class Example
class Car:
    color = "blue"
    brand = "BMW"

c1 = Car()
print(c1.color)  # Output: blue
print(c1.brand)  # Output: BMW

# Constructor (__init__ method)
# All classes have a function called __init__(), which is always executed when an object is being initialized.
# Syntax:
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# Example with Parameterized Constructor
class Student:
    def __init__(self, fullname, marks):  # we can pass multiple variables also
        self.name = fullname
        self.marks = marks
        print("Student created!")

s1 = Student("mansi", 87)
print(s1.name)  # Output: mansi
print(s1.marks)  # Output: 87

# Default Constructor
class Student:
    def __init__(self):
        pass

# self Parameter
# The self parameter is a reference to the current instance of the class
# and is used to access variables that belong to the class.

# Class Attributes vs Instance Attributes
class Student:
    college_name = "ABC College"  # Class attribute
    name = "anonymous"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute
        print("Student created!")

s1 = Student("mansi")
print(s1.name)  # Output: mansi

# Methods
# Methods are functions that belong to an object.
# They are defined within a class and can access attributes and other methods of the class using the self keyword.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):  # created a function here, this is a method
        print("Hello, students! I am", self.name)  # now we can access all the elements which are present in self

    def get_marks(self):
        return self.marks

s1 = Student("mansi", 65)
s1.hello()  # Output: Hello, students! I am mansi
print(s1.get_marks())  # Output: 65

#question 1 )-> create student class that takes name and marks of 3 subject as argument in constrctor then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hii",self.name,"your avg score is ",sum/3)        
s1=Student("tony shark",[45,67,89])
s1.average()
    