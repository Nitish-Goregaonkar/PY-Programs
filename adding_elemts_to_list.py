# Original list  
my_list = [1, 2, 3] 
 
# Adding a single element to the end  
my_list.append(4) 
print(my_list) # Output: [1, 2, 3, 4] 
 
# Adding multiple elements to the end  
my_list.extend([5, 6]) 
print(my_list) # Output: [1, 2, 3, 4, 5, 6] 
 
# Inserting an element at a specific position  
my_list.insert(2, 'a') # Inserts 'a' at index 2  
print(my_list) # Output: [1, 2, 'a', 3, 4, 5, 6] 