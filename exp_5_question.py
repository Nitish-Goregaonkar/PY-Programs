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

def count_frequency_with_count(lst):
    return {item: lst.count(item) for item in set(lst)}

def count_frequency_without_count(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

# Testing the functions
sample_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Frequency (using count function):", count_frequency_with_count(sample_list))
print("Frequency (without using count function):", count_frequency_without_count(sample_list))
