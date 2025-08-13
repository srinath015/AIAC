def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) != 2:
        return "Invalid input. Please enter a name in 'First Last' format."
    first, last = parts
    return f"{last}, {first}"

if __name__ == "__main__":
    name = input("Enter full name (First Last): ")
    print(format_name(name))