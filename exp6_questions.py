# Creating a tuple containing other tuples
outer_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# Accessing elements from the outer tuple
print("Outer tuple:", outer_tuple)
# Accessing an inner tuple
inner_tuple = outer_tuple[1]
print("Second inner tuple:", inner_tuple)
# Accessing an element from an inner tuple
element = outer_tuple[2][0]
print("First element of the third inner tuple:", element)



# Creating two tuples
tuple1 = (5, 2, 9, 1)
tuple2 = (8, 6, 4, 3)

# Concatenating tuples
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Sorting in ascending order
sorted_ascending = tuple(sorted(concatenated_tuple))
print("Sorted in ascending order:", sorted_ascending)

# Sorting in descending order
sorted_descending = tuple(sorted(concatenated_tuple, reverse=True))
print("Sorted in descending order:", sorted_descending)



# Creating a tuple of three elements
original_tuple = (10, 20, 30)

# Tuple unpacking into variables
a, b, c = original_tuple
print(f"Original values: a = {a}, b = {b}, c = {c}")

# Swapping values using tuple unpacking
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
