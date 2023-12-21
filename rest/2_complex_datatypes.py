# for
# create a list of numbers
numbers = ["google", 2, 3, 4, 5]
#
# use a for loop to print each number
for num in numbers:
    print("hi")
    print(num)
print("ended")


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
