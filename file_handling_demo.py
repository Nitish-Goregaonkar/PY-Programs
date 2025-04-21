import os
import shutil

def list_files(directory):
    try:
        files = os.listdir(directory)
        print("\nFiles and folders in directory:")
        for f in files:
            print(f)
    except FileNotFoundError:
        print("Directory not found.")

def create_file(filename):
    with open(filename, 'w') as f:
        f.write("")  # Empty file
    print(f"File '{filename}' created.")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print("\nFile content:")
        print(content)
    except FileNotFoundError:
        print("File not found.")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    except FileNotFoundError:
        print("File not found.")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}'.")
    except FileNotFoundError:
        print("Source file not found.")

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        print("File not found.")

def main():
    while True:
        print("\nFile Manager Menu:")
        print("1. List files")
        print("2. Create file")
        print("3. Read file")
        print("4. Delete file")
        print("5. Move file")
        print("6. Rename file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            path = input("Enter directory path: ")
            list_files(path)
        elif choice == '2':
            filename = input("Enter file name to create: ")
            create_file(filename)
        elif choice == '3':
            filename = input("Enter file name to read: ")
            read_file(filename)
        elif choice == '4':
            filename = input("Enter file name to delete: ")
            delete_file(filename)
        elif choice == '5':
            source = input("Enter source file path: ")
            destination = input("Enter destination path: ")
            move_file(source, destination)
        elif choice == '6':
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice == '7':
            print("Exiting File Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
