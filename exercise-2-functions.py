# Function, and use of function
# You can run this by: python exercise-2-functions.py

name: str = input("Enter your name: ")

def Greeting(name: str) -> str:
    fullGreeting =  "Hello " + name
    return fullGreeting

print(Greeting(name)) 

