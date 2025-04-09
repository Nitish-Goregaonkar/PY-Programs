# Example script to demonstrate the print() function with all parameters 
# Importing the sys module to use sys.stdout 
import sys
# 1. Basic usage with multiple objects 
print("Hello", "World", "!", sep=" ", end="\n") 
 
# 2. Using the 'sep' parameter to separate objects with a custom separator 
print("Python", "is", "fun", sep=" - ") 
# 3. Using the 'end' parameter to avoid the newline and print on the same line 
print("This is", end=" ") 
print("still on the same line.") 
 
# 4. Redirecting the output to a file using the 'file' parameter 
# Open a file in write mode 
with open("output.txt", "w") as f: 
    print("This will be written to a file.", file=f) 
 
