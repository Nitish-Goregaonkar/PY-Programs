# Function to find the maximum of two numbers
def find_max(a, b):
    return max(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Maximum:", find_max(num1, num2))


# Function to count vowels in a string
def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

user_string = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_string))


# Function to register students in a class
def register_students(class_name, *students, **details):
    print(f"Class Name: {class_name}")
    print("Students:", ", ".join(students) if students else "No students registered")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

