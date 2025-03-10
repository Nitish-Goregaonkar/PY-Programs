# Print a single asterisk and move to the next line twice to create space
print("*", end="\n\n")

# Print two asterisks separated by a space and move to the next line twice to create space
print("*", "*", sep=" ", end="\n\n")

# Print three asterisks separated by a space and move to the next line twice to create space
print("*", "*", "*", sep=" ", end="\n\n")

# Print four asterisks separated by a space and move to the next line twice to create space
print("*", "*", "*", "*", sep=" ", end="\n\n")



# Input: Get a string from the user
user_input = input("Enter a string: ")

# Reverse the string and join each character with a comma
reversed_string = ','.join(reversed(user_input))

# Output: Print the reversed string with commas between each character
print("reversed string =",reversed_string)


#factorial of a number is the product of all positive integers from 1 to n : for eg 5!=5*4*3*2*1=120
# taking input from the user  
num=int(input("Enter a Number:-"))
#initializing factorial =1
factorial=1
#loop from 1 to num
for i in range(1,num+1):
    factorial=factorial*i
#displaying the results using print function 
print("factorial of", num, "is",factorial)


#sum of first 10 natural numbers using multi line commments
""" the sum of the first n natural number is calculated using formula sum=n*(n+1)/2"""
#define number i.e n
n =10
#calculating the sum using the formula 
sum_of_numbers=n*(n+1)/2
#print calculate sum 
print("sum of first",n,"natural number is ", sum_of_numbers)


#using function calculating the sum of 10 natural numbers 

from colorama import Fore
#printing the below stattement in red color using colorama library
print(Fore.RED +"program to find the sum of n natural numbers using a function:-"+Fore.RESET)
#function to calculate the sum of n natural numbers
def calculateSumN(num):
    sum =0
     #loop 
    for i in range (1,num+1):
        sum+=i
    return sum 

result = calculateSumN(10)
print("Sum =", result)





