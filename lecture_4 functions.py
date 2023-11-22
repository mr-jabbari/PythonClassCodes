"""
    this lecture is for functions
"""


# Defines a function named 'greet' that prints a greeting.
def greet(name):
    return f"Hello, {name}!"


# Uses the function 'greet' with the argument 'Alice'.
# print(greet("Alice"))  # Output: Hello, Alice!

# Defines a function with a default parameter.
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Calls the function with and without the optional parameter.
# print(greet("Bob"))  # Output: Hello, Bob!
# print(greet("Bob", "Howdy"))  # Output: Howdy, Bob!


# Defines a function that accepts a variable number of arguments.
def fruits(*args):
    return f"I like these fruits: {', '.join(args)}."


# Uses the function with three arguments.
# print(fruits("apple", "banana", "cherry"))  # Output: I like these fruits: apple, banana, cherry.


# A function accepting any number of keyword arguments.
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calls the function with keyword arguments.
# profile(name="John", age=30, job="Developer")


# Output:
# name: John
# age: 30
# job: Developer
