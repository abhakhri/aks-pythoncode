# Python program to illustrate
# *args for variable number of arguments
# among others such as classes, use of modules, loops, conditions etc
# # You can run this by: python exercise-5-functionsAndArgs.py

def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

# When we pass a reference and change the received reference to something else, 
# the connection between the passed and received parameters is broken

def myFun(x):
    print(f"Just received parameter x {x}")
    x = [30,40,50,60]
    print(f"After modifying the parameter x {x}")

lst = [10,11,12,13,14,15]
print(f"Before sending to myFun {lst}")

myFun(lst)
print(f"After sending to myFun {lst}")
#

a = 21
b = 4

print(~a)

""" print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2) """
#
# Classes
#
class Person:
    firstName: str
    lastName: str
    address: str
    city: str
    state: str
    zip: str


    def __init__(self, firstName, lastName, address, city, state, zip):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return f"{self.firstName} {self.lastName}, {self.address}, {self.city}, {self.state}, {self.zip}"
    
# person = Person("john", "doe", "100 Some Street Circle", "somecity", "CA", "94526")

# print(person)
#
# Create a child class
#
class Employee(Person):
    salary: float
    def __init__(self,firstName, lastName, address, city, state, zip, salary):
        super().__init__(firstName, lastName, address, city, state, zip)
        self.salary = salary
#
    def __str__(self):
        return f"{self.firstName} {self.lastName}, {self.address}, {self.city}, {self.state}, {self.zip} {self.salary}"
#
    def setSalary(self, salary: float) -> float:
        self.salary = salary
        return self.salary
    
    def getSalary(self) -> float:
            return self.salary
#
emp = Employee("john", "doe", "100 Some Street Circle", "somecity", "CA", "94526", 100000.00)
#
print(f"Employee is: {emp}")
#
# print(f"My current salary is: {emp.salary}")
#
emp.salary = 233000.00
#
print(emp.salary)
#
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#
for x in mytuple:
  print(x)
#
# Dictionary
#
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
#
print(len(thisDict))
#
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")
#
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
#
# MODULE
#
# Consider a module to be the same as a code library.
#
# A file containing a set of functions you want to include in your application.
#
# To create a module just save the code you want in a file with the file extension .py
#
# First way
import exercise_4_mymodule
print("First way in using an external module")
exercise_4_mymodule.greeting("Puss in boots")

# Second way
from exercise_4_mymodule import greeting
print("Second way in using an external module")
greeting("Fido")
#
# Asking for User Input
#
whatsMyName = input("What's your name?: ")
#
print(f"Mein name ist: {whatsMyName}")
#
# ENUMS in Python
#
# PACKAGE INTO EXECUTABLE
#
# PACKAGE INTO LIBRARY
#
#
