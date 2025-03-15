def find_primes(a, b):
    primes = []  # List to store prime numbers
    num = a      # Start checking from the number a

    while num <= b:
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            i = 2
            while i * i <= num:  # Check for factors up to the square root of num
                if num % i == 0:
                    is_prime = False
                    break
                i += 1
            if is_prime:
                primes.append(num)
        num += 1  # Move to the next number
    
    return primes

# Input: Two integers a and b
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

# Find and print prime numbers in the range [a, b]
print("Prime numbers between", a, "and", b, "are:", find_primes(a, b))



# Initialize a variable to store the sum
sum_of_evens = 0

# Loop through numbers from 1 to 100
for number in range(1, 101):
    # Check if the number is even
    if number % 2 == 0:
        sum_of_evens += number

# Print the result
print("The sum of all even numbers from 1 to 100 is:", sum_of_evens)

