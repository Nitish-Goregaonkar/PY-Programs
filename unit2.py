def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print("factorial of the given number is :-",factorial(10))


mul=int(input("Enter a number"))
for i in range (1,11):
    print(mul,"*",i,"=",mul*i)

    