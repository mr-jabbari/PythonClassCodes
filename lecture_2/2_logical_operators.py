# jabbari79
# condition = False
# if 1 != 3 and 1 < 3:
#     print("Hi")
#     print("Hi2")

# print(1 == 3)
# print(1 < 3)
# print(1 > 3)
# print(1 <= 3)
# print(1 >= 3)
# print(1 != 3)
# print((1 == 3) and (4 != 5))
# print((1 == 3) or (4 != 5))
# print(not 2 == 3)

# print(bool("d"))
# if not "":
#     print("done")





















# x = None
# print(x)
# print(type(x))
# print(bool(x))





# name = input("what is your name? ")
# print(type(name))
# print(bool(name))
# if name:
#     print("hi")


first_name = input("please give me your first name: ")
last_name = input("please give me your last name: ")
birth_year = int(input("enter your birth year: "))
password = input("give me your password: ")
password2 = input("give me your password again: ")

start_sen = f"hi {first_name} {last_name},"
age = 1402 - birth_year

if password == password2:
    print(f"your password {len(password) * '*'} is {len(password)} long and does match.")
    if 0 < age < 18:
        print(f"{start_sen} you can't vote now, please come back in {18 - age} years.")
    elif 18 <= age <= 120:
        print(f"{start_sen} you can vote now.")
    elif age == 1000:
        print("sorry mr Yuda you can't vote in planet earth.")
    elif age <= 0:
        print(f"{start_sen} come back when you are born.")
    else:
        print("there is a Zomby here!!!")
else:
    print("your password doesn't match!!!")
