# Program to remove duplicates from a list of integers and print the sorted result

# Get user input as a comma-separated string
user_input = input("Enter a list of integers separated by commas: ")

# Convert input string to a list of integers
input_list = [int(x.strip()) for x in user_input.split(',')]

# Remove duplicates using set and sort the result
sorted_list = sorted(set(input_list))

print("Sorted list without duplicates:", sorted_list)