# Relational (Comparison) Operators
# These operators compare the values and return a boolean result.

a = int(input("Enter A Value of A: "))
b = int(input("Enter A Value of B: "))
print("Values of A & B are", a, b)

print("A is equal to B:", a == b)    # Equal to
print("A is not equal to B:", a != b)  # Not equal to
print("A is greater than B:", a > b)   # Greater than
print("A is less than B:", a < b)    # Less than
print("A is greater than or equal to B:", a >= b)  # Greater than or equal to
print("A is less than or equal to B:", a <= b)   # Less than or equal to

print()

# Logical Operators
# These operators perform logical operations on boolean values.
x=True
y=False
print(x and y)
print(x or y)
print(not x)

print()

# Bitwise Operators
# These operators perform bit-level operations.

a = int(input("Enter a value for A (bitwise operations): "))
b = int(input("Enter a value for B (bitwise operations): "))
print("Values of A & B are", a, b)

print("Bitwise AND of A & B:", a & b)  # Bitwise AND
print("Bitwise OR of A & B:", a | b)   # Bitwise OR
print("Bitwise XOR of A & B:", a ^ b)  # Bitwise XOR
print("Bitwise NOT of A:", ~a)  # Bitwise NOT
print("Bitwise left shift of A by 2:", a << 2)  # Left shift
print("Bitwise right shift of A by 2:", a >> 2)  # Right shift
