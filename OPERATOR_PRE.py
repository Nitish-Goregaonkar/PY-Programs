# Detailed demonstration of Operator Precedence and Associativity in Python

print("Operator Precedence in Python:")

# 1. Parentheses () - Highest precedence
print("1. Parentheses ():", (5 + 3) * 2)

# 2. Subscription, slicing []
x = [10, 20, 30]
print("2. Subscription, Slicing:", x[1], x[:2])

# 3. Await (Not applicable in standard execution)

# 4. Exponentiation ** (Right-to-left)
print("4. Exponentiation **:", 2 ** 3 ** 2)

# 5. Unary Operators (+, -, ~)
print("5. Unary +, -, ~:", -(-5), +(-3), ~2)


# 6. Multiplication, Division, Modulus, Floor Division (Left-to-right)
print("6. Multiplication, Division, Modulus, Floor Division:", 10 * 2 / 5, 10 // 3, 10 % 3)

# 7. Addition and Subtraction (Left-to-right)
print("7. Addition and Subtraction:", 10 - 2 + 3)

# 8. Bitwise Shift Operators (<<, >>) (Left-to-right)
print("8. Bitwise Shift:", 5 << 2, 20 >> 2)

# 9. Bitwise AND (Left-to-right)
print("9. Bitwise AND:", 5 & 3)

# 10. Bitwise XOR (Left-to-right)
print("10. Bitwise XOR:", 5 ^ 3)

# 11. Bitwise OR (Left-to-right)
print("11. Bitwise OR:", 5 | 3)

# 12. Comparison, Membership, Identity Operators (Left-to-right)
print("12. Comparison, Membership, Identity:", 5 > 3, 5 == 5, 3 in [1, 2, 3], 5 is not 4)



# 16. Conditional Expression (Right-to-left)
print("16. Conditional Expression:", "Yes" if 5 > 3 else "No")

# 17. Lambda Expression (N/A - used in function definitions)
add = lambda a, b: a + b
print("17. Lambda Expression:", add(2, 3))

# 18. Assignment Expression (Walrus Operator :=) (Right-to-left)
print("18. Assignment Expression:",(x:=10),x)
print(id(x))