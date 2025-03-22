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

n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
avg1=(n1+n2)/2
avg2=(n2+n3)/2
avg3=(n3+n1)/2
maxi=max(avg1,avg2,avg3)
print(maxi)


string1=input("enter a string:")
if(string1==string1[::-1]):
    print("its palindrome ")
else:
    print("not a palindrome")


def factorial(n):
   
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print("the factorial of n is :",factorial(10))


m=int(input("enter a number"))
for i in range(1,11):
    print(m,"*",i,"=",m*i)

for num in range(1,11):
    if num==5:
        continue
    print(num)



x=int(input("enter an number:-"))
ans=x**0.5
print("square root of an number is:-",ans)


g=int(input("enter a number"))
sum=0
for x in range (1,g):
    if g%2==0:
        sum=sum+i
if sum==g:
   print("its the perfect number",g) 
