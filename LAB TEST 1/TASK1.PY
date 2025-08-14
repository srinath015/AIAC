# Program to calculate the sum of odd and even numbers in a user-input list

# Get user input and convert to list of integers
numbers = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in numbers.split()]

even_sum = 0
odd_sum = 0

for num in num_list:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)