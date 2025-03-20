from termcolor import colored
print(colored("This is red text", "red"))
print(colored("This is green text", "green"))
print(colored("This is yellow text", "yellow"))


# Example: Multiplication table
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} * {j} = {i * j}")
