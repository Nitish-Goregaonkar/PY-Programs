def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print("factorial of the given number is :-",factorial(10))


mul=int(input("Enter a number"))
for i in range (1,11):
    print(mul,"*",i,"=",mul*i)


number=int(input("enter a number:-"))
sum =0
for x in range(1,number):
    if number%x==0:
        sum=sum+x
if sum==number:
    print("its a perfect number",number)

else:
    print("not a perfect number",number)



string1=input("enter string:-")
if(string1==string1[::-1]):
    print("its palindrome")
else:
    print("not a palindrome")