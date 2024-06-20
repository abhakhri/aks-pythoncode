# Simple Python concepts
# You can run this by: python exercise-1.py

city = "New York"

price = 250.00

high_score = 100

is_having_fun = True

print(city)
print(price)
print(high_score)
print(is_having_fun)

newline = "Hello\nWorld!"

print(newline)

greetWorld = "Hello \t World!"

print(greetWorld)

firstName = input("Enter your first name: ")

if firstName == "john":
    print(f"My first name is {firstName}")
elif firstName == "jack":
    print(f"My first name is {firstName}")
else:
    print(f"My first name is none of the above")

choice = input("Enter your choice of a number between 1 and 5 : ")

if choice == "1":
    print(f"YEA!!!")
elif choice == "2":
    print(f"OK")
elif choice == "3":
    print(f"HURRAY!")
elif choice == "4":
    print(f"Great Choice!")
else:
    print(f"AWW!!")
