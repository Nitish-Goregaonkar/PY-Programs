#Check if a number is positive. 
number = 10 
if number > 0: 
 print(f"{number} is positive.")

#Check if a number is positive or negative. 
number = -5 
if number > 0: 
  print(f"{number} is positive.")  
else: 
 print(f"{number} is negative.") 


 #Classify a number as positive, negative, or zero. 
number = 0 
if number > 0: 
 print(f"{number} is positive.") 
elif number < 0: 
 print(f"{number} is negative.") 
else: 
 print("The number is zero.")


#Check if a person is eligible to vote based on their age and citizenship. 
age = 20 
citizenship = 'USA' 
if age >= 18: 
 if citizenship == 'USA': 
   print("You are eligible to vote.") 
else: 
 print("You are not eligible to vote in the USA.") 
