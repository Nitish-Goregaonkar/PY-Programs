g=int(input("enter a number"))
sum=0
for x in range (1,g):
    if g%2==0:
         sum=sum+i
if sum==g:
      print("its the perfect number",g) 
else:
     print("its not a perfect number",g)


#new program
x=int(input("enter an number:-"))
ans=x**0.5
print("square root of an number is:-",ans)


# Example: Nested while loop to print a right-angle triangle
rows = 5 
i = 1 
while i <= rows:
      j = 1 
      while j <= i: 
       print()  # New line after each row 
i += 1
           

# Example: Nested for loop to print multiplication table 
for u in range(1, 6): 
     for x in range(1, 6): 
          print(f"{u} x {x} = {u * x}", end='\t') 
     print()   







#printing traingle program
def pascals_triangle(n):
     triangle = [[1] * (i + 1) for i in range(n)]
     for i in range(2, n):
           for j in range(1, i):
                 triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
     for row in triangle:
           print(" ".join(map(str, row)))


n = int(input("Enter number of rows: "))

pascals_triangle(n)