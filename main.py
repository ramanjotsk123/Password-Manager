def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{website},{username},{password}\n")

    print("Password saved successfully!")


def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("No passwords stored.")

            for item in data:
                print(item.strip())

    except FileNotFoundError:
        print("No passwords stored yet.")


while True:

    print("\nPASSWORD MANAGER")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
