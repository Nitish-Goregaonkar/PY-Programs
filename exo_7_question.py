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



# Take input for the first sentence
sentence1 = input("Enter the first sentence: ")

# Split sentence into words and create a set of unique words
set1 = set(sentence1.split())

# Take input for the second sentence
sentence2 = input("Enter the second sentence: ")

# Split sentence into words and create a set of unique words
set2 = set(sentence2.split())

# Find common words in both sentences (intersection)
common_words = set1 & set2
print("Common words in both sentences:", common_words)

# Find words unique to each sentence
unique_to_sentence1 = set1 - set2
unique_to_sentence2 = set2 - set1

print("Words unique to first sentence:", unique_to_sentence1)
print("Words unique to second sentence:", unique_to_sentence2)
