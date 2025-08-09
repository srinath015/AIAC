# Simple user authentication system with register_user() and login_user()

users_db = {}

def register_user():
    print("=== Register User ===")
    username = input("Enter a new username: ").strip()
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return
    password = input("Enter a new password: ").strip()
    users_db[username] = password
    print(f"User '{username}' registered successfully!\n")

def login_user():
    print("=== Login User ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users_db and users_db[username] == password:
        print(f"Login successful! Welcome, {username}.\n")
    else:
        print("Invalid username or password. Please try again.\n")

if __name__ == "__main__":
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Select an option (1/2/3): ").strip()
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.\n")
