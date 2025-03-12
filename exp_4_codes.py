# Example: Using a while loop to print numbers from 1 to 5 
number = 1 
while number <= 5: 
    print(f"While Loop: {number}") 
    number += 1

# Example: Using a for loop to print elements of a list 
fruits = ['apple', 'banana', 'cherry'] 
for fruit in fruits: 
    print(f"For Loop: {fruit}")

# Example: Nested for loop to print multiplication table 
for u in range(1, 6): 
    for x in range(1, 6): 
        print(f"{u} x {x} = {u * x}", end='\t') 
    print()  # New line after each inner loop iteration

# Example: Nested while loop to print a right-angle triangle 
rows = 5 
i = 1 
while i <= rows: 
    j = 1 
    while j <= i: 
        print('*', end=' ')
        j += 1 
print()  # New line after each row 
i += 1