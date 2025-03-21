from termcolor import colored
print(colored("This is red text", "red"))
print(colored("This is green text", "green"))
print(colored("This is yellow text", "yellow"))


# Example: Multiplication table
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} * {j} = {i * j}")


numbers=[1,2,3,4,5,6,7,8,9,10]
even_no=[num for num in numbers if num %2==0]
print("even numbers:", even_no)