"""
    this lecture is for functions
"""

def add(num1, num2):
    print(num1+num2)


# Defines a function named 'greet' that prints a greeting.
def greet(name):
    return f"Hello, {name}!"


# Defines a function with a default parameter.
def greet_2(name, greeting="Hello"):
    return f"{greeting}, {name}!"




# Uses the function 'greet' with the argument 'Alice'.
print(greet("Alice"))
greet("reza")

add(num1=5, num2=8)

# Calls the function with and without the optional parameter.
print(greet_2(name="Bob"))
print(greet_2("Bob", "Howdy"))


# Defines a function that accepts a variable number of arguments.
def fruits(*args):
    print(args)
    return f"I like these fruits: {', '.join(args)}."


# Uses the function with three arguments.
# print(fruits("apple", "banana", "cherry"))


# A function accepting any number of keyword arguments.
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calls the function with keyword arguments.
# profile(name="John", age=30, job="Developer")
