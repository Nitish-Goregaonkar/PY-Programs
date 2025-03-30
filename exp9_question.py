# Function to find the maximum of two numbers
def find_max(a, b):
    return max(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Maximum:", find_max(num1, num2))


# Function to count vowels in a string
def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

