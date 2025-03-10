# Get two decimal numbers from the user
num1 = int(input("Enter the first decimal number: "))
num2 = int(input("Enter the second decimal number: "))

# Convert the decimal numbers to binary
bin1 = bin(num1)[2:]
bin2 = bin(num2)[2:]

# Print the binary representations
print(f"Binary of {num1}: {bin1}")
print(f"Binary of {num2}: {bin2}")

# Convert binary strings back to integers for bitwise operations
int_bin1 = int(bin1, 2)
int_bin2 = int(bin2, 2)

# Perform bitwise operations
and_result = int_bin1 & int_bin2
or_result = int_bin1 | int_bin2
xor_result = int_bin1 ^ int_bin2
not_result1 = ~int_bin1
not_result2 = ~int_bin2

# Print bitwise operation results
print(f"{bin1} AND {bin2} = {bin(and_result)[2:]}")
print(f"{bin1} OR {bin2} = {bin(or_result)[2:]}")
print(f"{bin1} XOR {bin2} = {bin(xor_result)[2:]}")
print(f"NOT {bin1} = {bin(not_result1)[3:]}")
print(f"NOT {bin2} = {bin(not_result2)[3:]}")

# Use logical operators to check conditions based on results
and_cond = and_result != 0
or_cond = or_result != 0
xor_cond = xor_result != 0

# Print logical conditions results
print(f"AND result is non-zero: {and_cond}")
print(f"OR result is non-zero: {or_cond}")
print(f"XOR result is non-zero: {xor_cond}")
