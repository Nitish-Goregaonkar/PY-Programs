#for loop ex
#for times in range(1,5):
    #print("nitish")

    #for breaking a loop in specified condition
#for i in range(1,100):
    #if (i==5):
       # break
    #print(i)
    #skip specified no and continue the loop
#for i in range(1,30):
 #   if(i==10):
  #      continue
   # print(i)

#print no from 1 to n
#n=int(input())
#for i in range(1,n+1):
 #   print(i)

 #print x to n
#x= int (input())
#n= int (input())
#for i in range(x, n+1):
 #   print(i)

 #take n as input and print the multiples of 7 till n
#n= int (input())
#for i in range (0, n+1, 7):
 #   print(i, end=" ")

#while loop ex
# wap that repeatedly asks a user to input a no then print a no is odd or even.
#continue the program until user says no
#user_input= input("do you want to continue (yes/no)")
#user_input="yes"
#while user_input=="yes":
 #   no=int(input("enter the no "))
   # if no%2==0:
    #    print("even")
   # else:
    #    print("odd")
    #print n, n-k, n-2k, n-3k till l
    #for eg:-50 5 4
   # output:-50,45,40,35,.....5
n = int(input())
k = int(input())
l = int(input())
while(n >=l):
    print(n)
    n= n-k


