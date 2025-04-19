# Open a file for updating (reading and writing)
file = open("example.txt", "w+")  # "w+" allows reading and writing, but it overwrites the file

# Using write() to insert a single string
file.write("This is a single line written using the write() method.\n")

# Using writelines() to insert multiple strings
lines = ["Line 1 written using writelines().\n", "Line 2 written using writelines().\n", "Line 3 written using writelines().\n"]
file.writelines(lines)

# Move the file pointer to the beginning
file.seek(0)

# Read and display the content of the file
content = file.read()
print("Content of the file:")
print(content)

# Close the file
file.close()
