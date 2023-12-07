# Jabbari79
"""
lecture overview:
    functions:
        print()
        type()
        abs()    just for numbers
        round()  just for numbers
        str()    convert to string
        int()    convert to int
        float()  convert to float
        bool()   convert to bool
    math operators:
        + sum
        - subtraction
        * multiplication
        / division
        // int division
        ** power
        % remainder
    Simple Data Types:
        str:
            "my string"
             012345678     string indexing
        int:
            4
            -75
            53484435487352154
            8
        float:
            5.0
            -78.168
            0.0
        bool:
            True
            False
    variables:
        my_custom_name = my data

    comment:
        #
    comment shortcut:
        Ctrl + /

"""


# int and int functions
print(4+2)
print(4-2)
print(4*2)
print(4/2)
print(4**2)
print(14//3)
print(14 % 3)
print(abs(-18))
print(round(-18.5))
print(type(4+3.6))
print(12 + 2 * 3)
print((13.2-3) + 2 ** 3)

# str and str functions
print("Hello World")
print('Hello World')
print("I'm Hasan")
print("""
 _ _
 0 0
-----
""")
print("Hi " + "you")
print("Hi " + '5')

# variables
a, b, c = 12, 4, 5
print(a)
print(b)
print(c)

num = 4
first_name = "Ali"
last_name = "Alavi"
print(first_name + " " + last_name)
my_sen = 'I\'m Hasan.\nwho are you?'
ans = f"I'm {first_name} {last_name}"
print(my_sen)
print(ans)
quote = '\tI\'m \nBatman'
print(quote)

# string indexing
sample = "012345678"
#         0123456
print(sample[1])
print(sample[:2])
print(sample[1:])
print(sample[::3])
print(sample[::-1])
print(sample[::-2])


# sample[2] = 4
new_sample = sample + "9"
print(sample)

# bool
name = "reza"
single = True