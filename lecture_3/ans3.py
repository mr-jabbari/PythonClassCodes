n = 100000  # Example range
count = 0
for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break
    if prime:
        count += 1
        print("count: ", count)
        print(num)

# n = 5
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
