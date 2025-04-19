# Step 1: Create a file and write data
file_object = open("myfile.txt", "w")  # Open file in write mode
file_object.write("Hello, this is the first line.\n")
file_object.write("This is the second line.\n")
file_object.write("And here is the third line.\n")
file_object.close()  # Close the file after writing

# Step 2: Reopen the file for reading
file_object = open("myfile.txt", "r")  # Open file in read mode

# Read the entire file using read()
print("Using read():")
print(file_object.read())  # Reads the entire file
file_object.seek(0)  # Reset file pointer to the beginning

# Read one line using readline()
print("\nUsing readline():")
print(file_object.readline())  # Reads the first line
file_object.seek(0)  # Reset file pointer to the beginning

# Read all lines using readlines()
print("\nUsing readlines():")
print(file_object.readlines())  # Reads all lines as a list of strings

# Close the file
file_object.close()
