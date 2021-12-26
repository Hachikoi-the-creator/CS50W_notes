# Takes a func as an argument and returns that func changed
# OR add extra capabilities to a function
def testin(func):
    def wrapper():
        print("Before runnin'")
        func()
        print("hello there")
    return wrapper
    
"""
Takes nothing() as an arguent
-> returns a function that prints more 
"""
@testin
def nothing():
    print("a")

nothing()

# --------------------------------------------------
# A version of decorators whit default functions 
# --------------------------------------------------
persons = [
    {"name":"Jhon", "Livin":"Ohaio"},
    {"name":"Childe", "Livin":"Liyue"},
    {"name":"Andreus", "Livin":"Mondstand"}
]
def f(list_element):
    return list_element["name"]
    # return list_element["Livin"]

# Tells the func sort, how you want to sort every element of the list
persons.sort(key=f)
# The same but whit lambda
persons.sort(key=lambda person: person["name"])
print(persons)

# --------------------------------------------------
# Try, Except
# --------------------------------------------------
import sys
try:
    x = int(input("Ayyy: "))
    y = int(input("Awwww: "))
except ValueError:
    print("invalid input")
    # This is more reliable, used in production, etc
    sys.exit()

try:
    print(f"The result of the division is {x/y}")
except ZeroDivisionError:
    print("Cannot divide by zero, otherwise the world will end and.. your pc will explode")
    exit()


