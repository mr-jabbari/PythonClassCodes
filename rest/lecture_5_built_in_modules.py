import math  #  https://docs.python.org/3/library/math.html#module-math
from math import sin
import datetime  #  https://docs.python.org/3/library/datetime.html#module-datetime
from datetime import timedelta
import random  #  https://docs.python.org/3/library/random.html#module-random
import csv  #  https://docs.python.org/3/library/csv.html#module-csv
import json  #  https://docs.python.org/3/library/json.html#module-json


# math
# print(math.pi)                 # Outcome: 3.141592653589793
# print(sin(math.pi / 2))   # Outcome: 1.0
# print(math.cos(math.pi))       # Outcome: -1.0



# datetime
# Get the current date and time.
# now = datetime.datetime.now()
# print(now)
#
# # Calculate a new timedelta and add it to the current time.
# future_date = now + timedelta(days=10, weeks=2)
# print(future_date)

# before = datetime.datetime.now()
# print(before)
#
# for _ in range(1000000000):
#     pass
#
# after = datetime.datetime.now()
# print(after)
# run_time = after - before
# print(run_time)
# print(run_time.microseconds)
# print(run_time.seconds)
# print(run_time.total_seconds())
# print(type(run_time))





# random
# Generate a random integer within a given range.
# print(random.randint(1, 100))
# Choose a random element from a list.
# fruits = ['apple', 'banana', 'cherry']
# print(random.choice(fruits))
# print(fruits)
# Shuffle a list randomly.
# random.shuffle(fruits)
# print(fruits)








# num = random.randint(0, 100)
# number_of_chances = 5
# for i in range(number_of_chances+1):
#     user_num = int(input("give me a number between 0 and 100: "))
#     if i == number_of_chances:
#         print("you lost.")
#         break
#     elif 100 < user_num or 0 > user_num:
#         print("I said between 0 and 100.")
#     elif user_num == num:
#         print("you won")
#         break
#     elif user_num > num:
#         print("this time give me smaller number.")
#     else:
#         print("this time give me bigger number.")
#     print(f"you have {number_of_chances - i} time left")
# print(num)




# csv
# Writing data to a CSV file
# data = [
#     ['Name', 'Age', 'Country'],
#     ['John', '25', 'USA'],
#     ['Emily', '30', 'Canada'],
#     ['David', '40', 'UK']
# ]

filename = 'lecture_5.csv'

# with open(filename, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)


# # Reading data from a CSV file
# with open(filename, 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
