# jabbari79
print(4 + 2)
print(4 - 2)
print(4 * 2)
print(14 / 3)
print(4 ** 2)
print(14 // 3)
print(14 % 3)

print(type(-10.2))

print(abs(-18))
print(round(-18.5))
print(type(4 + 3.6))

print(12 + 2 * 3)
print((13.2 - 3) + 2 ** 3)

print("Hello World")
print('Hello World')
print("I'm Hasan")
print("""
 _ _
 0 0
-----
""")

print("Hi " + "you")
# print("Hi " + 5)

num = 4
first_name = "hasan"
last_name = "Hosseini"
print(first_name + " " + last_name)

# ********************Q1*******************

my_sen = 'I\'m Hasan.\nwho are you?'
ans = f"I'm {first_name} {last_name}"
print(my_sen)
print(ans)

quote = '\tI\'m \nBatman'
print(quote)

# string indexing
sample = "0123456789"
#         0123456789
print(sample[3])

# sample[start:stop:stepover]
print(sample[1])
print(sample[:2])
print(sample[1:])
print(sample[::3])
print(sample[::-1])
print(sample[::-2])

# sample[2] = 4
sample = sample + "9"
print(sample)

# bool
name = "reza"
single = False

# ********************Q2*******************

# list

fruits = ["apple", "banana", "orange", "grape"]
print(fruits)

print(fruits[2])

# slice the list
print(fruits[1:3])

# append a new item to the end of the list
fruits.append("mango")
print(fruits)
fruits[0] = "banana"
print(fruits)

# remove the last item from the list
fruits.pop()
fruits.pop(0)
print(fruits)

# rage()
numbers = range(1, 12, 2)
print(numbers)
print(type(numbers))

print(list(numbers))

# tuple
colors = ("red", "green", "blue", "red")
print(colors.count("red"))
print(colors[1])

print(colors[0:2])

# colors[0] = "pink"
print(colors)

# set
odd = {1, 3, 5, 7, 9}
even = set([2, 4, 6, 8, 10])

# find the union of two sets
print(odd | even)

# find the intersection of two sets
print(odd & even)

# find the difference of two sets
print(odd - even)

# check if an item is in a set
print(3 in odd)
print(3 in even)

# dictionary
# create a dictionary of countries and their capitals
countries = {"France": "Paris",
             "Japan": "Tokyo",
             "India": "New Delhi",
             "Iran": "Tehran"}

print(countries["France"])

countries["China"] = "Beijing"
print(countries)

# remove a key-value pair
countries.pop("Japan")
print(countries)
# change the value of a key
countries["India"] = "Mumbai"
print(countries)

matrix = [
    [1, 2, 3],
    {"name": ["n", 4]},
    [7, 8, 9],
]
print(matrix[1]["name"][1])
