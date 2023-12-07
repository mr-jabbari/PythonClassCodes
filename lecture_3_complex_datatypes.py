# jabbari79
"""
python built in functions: https://docs.python.org/3/library/functions.html
python list methods: https://www.w3schools.com/python/python_lists_methods.asp
python dict methods: https://www.w3schools.com/python/python_ref_dictionary.asp
python set methods: https://www.w3schools.com/python/python_ref_set.asp
python tuple methods: https://www.w3schools.com/python/python_ref_tuple.asp

lecture overview:
    data types:
        None
        list    []
        set     {}
        tuple   ()
        dictionary   {key:value}




    break, continue, pass
"""




# # rage()
# # use a range() function to create a sequence of numbers from 1 to 10 (inclusive) with a step of 2
# numbers = range(1, 11, 2)
#
# # print the type of the object
# print(type(numbers))
#
# # convert the object to a list
# print(list(numbers))




## list
# # create a list of fruits
# fruits = ["apple", "banana", "orange", "grape"]
# # # access the first item
# # print(fruits[0])
# #
# # # slice the list from index 1 to 3 (exclusive)
# # print(fruits[1:3])
# #
# # # append a new item to the end of the list
# fruits.append("mango")
# # fruits[0] = "banana"
# print(fruits)
# #
# # # remove the last item from the list
# fruits.pop()
# fruits.pop(1)
# print(fruits)





# # tuple
# # create a tuple of colors
# colors = ("red", "green", "blue", "red")
# print(colors.count("red"))
# # access the second item
# print(colors[1])
#
# # slice the tuple from index 0 to 2 (exclusive)
# print(colors[0:2])
#
# # try to change the first item
# colors[0] = "pink"
# print(colors)




# set
# # create a set of odd numbers
# odd = {1, 3, 5, 7, 9}
#
# # create a set of even numbers
# even = set([2, 4, 6, 8, 10])
#
# # find the union of two sets
# print(odd | even)
#
# # find the intersection of two sets
# print(odd & even)
#
# # find the difference of two sets
# print(odd - even)
#
# # check if an item is in a set
# print(3 in odd)
# print(3 in even)




# dictionary
# # create a dictionary of countries and their capitals
# countries = {"France": "Paris",
#              "Japan": "Tokyo",
#              "India": "New Delhi",
#              "Iran": "Tehran"}
#
# # # access the value of a key
# print(countries["France"])
# #
# # # add a new key-value pair
# countries["China"] = "Beijing"
# print(countries)
# #
# # # remove a key-value pair
# countries.pop("Japan")
# print(countries)
# #
# # change the value of a key
# countries["India"] = "Mumbai"
# print(countries)




# user_1 = {
#     "name": "Gholi",
#     "age": 25,
#     "followers": 255,
#     "admin": True,
#     "brothers": ["reza","ali"]
# }
# print(user_1["age"])
# print(user_1.keys())
# print(user_1.values())
# if user_1["admin"]:
#     print("you have access")



# matrix = [
#     [1,2,3],
#     {"family":["mom","dad"]},
#     [7,8,9],
# ]
# print(matrix[1]["family"][1])















# # for
# # create a list of numbers
# numbers = ["google", 2, 3, 4, 5]
# #
# # use a for loop to print each number
# for num in numbers:
#     print("hi")
#     print(num)
# print("ended")


# # create a string
# word = "hello"
#
# # use a for loop to print each character
# for char in word:
#     print(char)
#
# print(list(range(10)))
# use a range to generate a sequence of numbers from 1 to 10 (exclusive)
# for i in range(1, 11):
#     print(i)







# small_num = int(input("enter smaller number: "))
# big_num = int(input("enter bigger number: "))
# if small_num>big_num:
#     small_num,big_num = big_num,small_num
# count = 0
# for i in range(small_num,big_num+1):
#     count += i
# print(f"your count is: {count}")








# # while
# # initialize a counter
# i = 1
# # use a while loop to print the numbers from 1 to 10
# while i <= 11:
#     print(i)
#     if i == 8:
#         break
#     if i == 5:
#         continue
#     # increment the counter by 1
#     i += 1








# define a password
password = "secret"

# ask the user to enter a password
user_input = input("Enter the password: ")

# use a while loop to check if the password is correct
while user_input != password:
    # print a message
    print("Wrong password. Try again.")
    # ask the user to enter a password again
    user_input = input("Enter the password: ")

# print a message
print("Correct password. You are logged in.")
