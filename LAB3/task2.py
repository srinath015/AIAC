def sort_numbers():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, user_input.strip().split()))
        sorted_numbers = sorted(numbers)
        print("Sorted numbers:", sorted_numbers)
    except ValueError:
        print("Please enter valid integers separated by spaces.")

if __name__ == "__main__":
    sort_numbers()
