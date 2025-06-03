def remove_value(lst, value):
    return [item for item in lst if item != value]

print(remove_value([1, 2, 3, 2, 4], 2))  # Output: [1, 3, 4]
        