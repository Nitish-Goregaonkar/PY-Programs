



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
