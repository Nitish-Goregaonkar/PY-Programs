#built in functions like len(): Returns the number of elements in the list. 
#del: Deletes elements from the list or the entire list. 
 #list(): Converts other data types into lists.

my_list = [1, 2, 3]  
print(len(my_list)) # Output: 3 
del my_list[1] # Deletes the second element 
print(my_list) # Output: [1, 3] 
tuple_data = (4, 5, 6) 
list_from_tuple = list(tuple_data)  # Converts tuple to list  
print(list_from_tuple)  # Output: [4, 5, 6]