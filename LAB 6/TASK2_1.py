def print_multiples(num):
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

num = int(input("Enter a number: "))
print_multiples(num)