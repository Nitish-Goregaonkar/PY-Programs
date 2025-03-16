# Method 1: Using the reverse() method
def reverse_with_method(lst):
    lst.reverse()
    return lst

# Method 2: Using slicing
def reverse_with_slicing(lst):
    return lst[::-1]

# Method 3: Using a for loop
def reverse_with_loop(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)
    return reversed_list

# Method 4: Using recursion
def reverse_with_recursion(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_with_recursion(lst[:-1])

# Method 5: Using reduce (functional programming)
from functools import reduce
def reverse_with_reduce(lst):
    return reduce(lambda acc, x: [x] + acc, lst, [])

# Example usage
original_list = [1, 2, 3, 4, 5]

print("Original list:", original_list)
print("Reversed with reverse():", reverse_with_method(original_list.copy()))
print("Reversed with slicing:", reverse_with_slicing(original_list))
print("Reversed with loop:", reverse_with_loop(original_list))
print("Reversed with recursion:", reverse_with_recursion(original_list))
print("Reversed with reduce:", reverse_with_reduce(original_list))



# Program to find the maximum and minimum elements in a list

def find_max_min(lst):
    return max(lst), min(lst)

# Testing the function
sample_list = [10, 20, 5, 8, 30, 2]
max_val, min_val = find_max_min(sample_list)
print("Maximum:", max_val)
print("Minimum:", min_val)



# Program to count the frequency of each element in a list

def count_with_builtin(lst):
    frequency = {}
    for item in lst:
        frequency[item] = lst.count(item)  # Using count()
    return frequency

def count_without_builtin(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1  # Increment count
        else:
            frequency[item] = 1  # Initialize count
    return frequency

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Using count():", count_with_builtin(my_list))
print("Without using count():", count_without_builtin(my_list))
