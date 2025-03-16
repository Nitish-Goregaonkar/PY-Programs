def get_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {char.lower() for char in sentence if char.lower() in vowels}

# Taking input from the user
sentence = input("Enter a sentence: ")
print("Vowels present in the sentence:", get_vowels(sentence))



# Define sets for vegetarian and non-vegetarian dishes
vegetarian_dishes = {"Salad", "Paneer Tikka", "Vegetable Biryani", "Dal Tadka"}
non_vegetarian_dishes = {"Chicken Biryani", "Fish Curry", "Dal Tadka", "Egg Curry"}

# Find all dishes available (union)
all_dishes = vegetarian_dishes | non_vegetarian_dishes  # Using union operator
print("All available dishes:", all_dishes)

# Find common dishes (intersection)
common_dishes = vegetarian_dishes & non_vegetarian_dishes  # Using intersection operator
print("Dishes present in both categories:", common_dishes)

# Check if vegetarian_dishes is a subset of non_vegetarian_dishes
is_subset = vegetarian_dishes.issubset(non_vegetarian_dishes)
print("Is vegetarian_dishes a subset of non_vegetarian_dishes?", is_subset)
