# File Operations Module

# 1. Create a new file
def create_file():
    name = input("Enter file name: ")

    if name.endswith(".txt"):
        file_name = name
    else:
        file_name = name + ".txt"

    try:
        file = open(file_name, "x")
        file.close()
        print("File created successfully!")
    except FileExistsError:
        print("File already exists!")


# 2. Write content in a file
def write_file():
    name = input("Enter file name: ")

    if name.endswith(".txt"):
        file_name = name
    else:
        file_name = name + ".txt"

    content = input("Enter content: ")

    file = open(file_name, "w")
    file.write(content)
    file.close()

    print("Content saved successfully!")


# 3. Read content from a file
def read_file():
    name = input("Enter file name: ")

    if name.endswith(".txt"):
        file_name = name
    else:
        file_name = name + ".txt"

    try:
        file = open(file_name, "r")
        content = file.read()
        file.close()

        if content == "":
            print("File is empty!")
        else:
            print("File content:")
            print(content)

    except FileNotFoundError:
        print("File not found!")


# 4. Add new content to a file
def append_file():
    name = input("Enter file name: ")

    if name.endswith(".txt"):
        file_name = name
    else:
        file_name = name + ".txt"

    content = input("Enter new content: ")

    file = open(file_name, "a")
    file.write("\n" + content)
    file.close()

    print("New content added successfully!")


# 5. File Operations Menu
def file_menu():
    while True:
        print("\n--- FILE OPERATIONS ---")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Append to File")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")
