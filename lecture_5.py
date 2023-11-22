import math  #  https://docs.python.org/3/library/math.html#module-math
import datetime  #  https://docs.python.org/3/library/datetime.html#module-datetime
import random  #  https://docs.python.org/3/library/random.html#module-random
import csv  #  https://docs.python.org/3/library/csv.html#module-csv


# math
# print(math.pi)                 # Outcome: 3.141592653589793
# print(math.sin(math.pi / 2))   # Outcome: 1.0
# print(math.cos(math.pi))       # Outcome: -1.0


# datetime
# Get the current date and time.
# now = datetime.datetime.now()
# print(now)   # Example output: 2021-06-19 12:11:00.123456
#
# # Calculate a new timedelta and add it to the current time.
# future_date = now + datetime.timedelta(days=10)
# print(future_date)  # Outcome will be 10 days after the current date and time.


# random
# Generate a random integer within a given range.
# print(random.randint(1, 100))  # For example, returns a number between 1 and 100.
#
# # Choose a random element from a list.
# fruits = ['apple', 'banana', 'cherry']
# print(random.choice(fruits))  # For example, returns 'apple', 'banana', or 'cherry'.

# Shuffle a list randomly.
# random.shuffle(fruits)
# print(fruits)  # The order of elements in 'fruits' is now shuffled.


# csv
# Write to a CSV file.
# with open('example.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'department', 'birthday'])
#     writer.writerow(['John Smith', 'Accounting', 'November'])
#     writer.writerow(['Erica Meyers', 'IT', 'March'])
#
# # Read from a CSV file.
# with open('example.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)  # Prints each row in the file.
