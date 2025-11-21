# Sets basics

unique_ids = {1, 2, 3, 3, 'a', 'b', 4}

# Print the set (order is not guaranteed)
print(unique_ids)
print(type(unique_ids))

# print(unique_ids[0]) # Error: Sets do not support indexing

# empty_set = {} # Empty dict, not set
empty_set = set()
print(type(empty_set))

# Create a set from a list to get unique sentences
sentences = ['Hello world', 'AI is amazing', 'Hello world', 'Python is great']
unique_sentences = set(sentences)
print(list(unique_sentences))

# Set operations and methods
# Create a set (duplicates are automatically removed)
unique_ids = {1, 2, 3, 1}
print(unique_ids)   # Output: {1, 2, 3} (order may vary)

# Add an element to the set
unique_ids.add(5)
print(unique_ids)

# Remove an element from the set
unique_ids.remove(3)
print(unique_ids)

# Add an immutable element (like a tuple) to the set
immutable_element = tuple([4, 5, 6])
unique_ids.add(immutable_element)
print(unique_ids)

# Iterate through the set (order is not guaranteed)
for uid in unique_ids:
    print(uid)

# Check for membership in the set
if 2 in unique_ids:
    print('2 is available in Set')
else:
    print('2 is not available in Set')

# Create an immutable set (frozenset)
immutable_tokens = frozenset(unique_ids)
print(immutable_tokens)

immutable_tokens.add(10)
print(immutable_tokens)



