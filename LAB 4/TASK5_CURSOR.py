filename = "C:\\Users\\pooda\\OneDrive\\Desktop\\SR UNIVERSITY.txt"
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print(f"File not found: {filename}")
