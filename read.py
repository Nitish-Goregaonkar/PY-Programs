# Create the file and write some content
file_object = open("example.txt", "w")
file_object.write("Hello, this is a sample file.")
file_object.close()
# Open a file in read mode
file_object = open("example.txt", "r")

# Read the entire contents of the file
file_contents = file_object.read()

# Print the file contents
print(file_contents)

# Close the file
file_object.close()