#list1= [5,4,3,2,1]
#list2= [6,7,8,9,0]
#print(list1)
#print(list2)

#print(list1[2])
#print(list2[-1])
#list1.append("hello")
#print(list1)

#n= int(input())
#mylist=[]
#for i in range(0, n):
 #   value=int(input())
  #  mylist.append(value)
#print(mylist)

#n= int(input())
#newlist=input().split(" ")
#for i in range (n):
 #newlist[i]= int(newlist[i])
#print(newlist)

#n= int(input())
#list1= []
#for i in range(n):
 #   value= int(input())

#  list1.append(value)

#for i in range(0, n, 2):
 #    print(list1[i])

 #print alternative array elements
#n = int(input())
#list1=[]
#for i in range(n):
 #    value= int(input())
  #   list1.append(value)
#for i in range(0, n,2):
 #    print(list1[i])


 #print the element of the array from the last index till the 0th index but in one line
#n =  int(input())
#list1=[]
#for i in range(n):
 #   value= int(input())
  #  list1.append(value)
#for i in range (n-1,-1,-1):
 #   print(list1[i], end= " ")


#wap to check if both the array are similar or not print true or false
#n1= int(input())
#list1=[]
#for i in range (n1):
 #   value= int(input())
  #  list1.append(value)

#n2= int(input())
#list2=[]
#for i in range (n2):
 #   value1= int(input())
  #  list2.append(value1)

#if(n1==n2):
 #   if(list1==list2):
  #      print("true")
    #else:
   #     print("false")
#else:
 #   print("false")

 #1. append(): add a single element to the end of the list
 #list1=[1,2,3]
 #list1.append("hello")
 #print(list1)


 #2. extend():- adds all the elements of an iterable to the end of the list
#list1=[1,2,3]
#list1.extend([4,5,6])
#print(list1)



#3. insert():- insert element at the specified index
#list1=[1,2,3]
#list1.insert(1,"hello")
#print(list1)

#4. **remove()**: Removes the first occurrence of a specified element.
#list1 = [1,2,3,4,5,1,1,1,1]
#list1.remove(1)
#print(list1)
#list1.remove(1)
#print(list1)

#5. **pop()**: Removes and returns the element at the specified index (or the last element if no index is specified).
# remove from particular index
# remove from last
#list1 = [1,2,3,4,5]
#list1.pop()
#print(list1)

#6. ** clear()**: Removes all items from the list.
#list1 = [1,2,3,4,5]
#list1.clear()
#print(list1)

#7. **index()**: Returns the index of the first occurrence of a specified element.
#list1=[1,2,3,4,5,6,7,8,9,10]
#index= list1.index(5)
#print(index)

#8. **count()**: Returns the number of occurrences of a specified element in the list.
#list1 =[1,2,2,2,2,2,3,3,3,3,3,4]
#count = list1.count(2)
#print(count)

#9. **sort()**: Sorts the element of the list in place.
# list1 = [1,2,3,4,5,6,7,8,9]
#10. **reverse()**: Reverses the element of the list in place.

#11. **copy()**: Returns a shallow copy of the list.