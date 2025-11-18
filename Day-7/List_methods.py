# ESSENTIAL LIST METHODS IN PYTHON

# ADDING ELEMENTS TO A LIST

list1 = list()

# append(): Adds a single element to the end of the list
list1 = [1, 2.2, 'abc']
list1.append([4, 5])
print(list1)

# extend(): Extends the list with elements from an iterable
list1.extend(['x', 'y'])
print(list1)

# insert(): Inserts an element at a specific index
list1.insert(3, False)
print(list1)

# REMOVING ELEMENTS FROM A LIST

# clear(): Removes all elements from the list
list1.clear()
print(list1)

# pop(): Removes and returns an element by index (default is the last element)
l2 = [10, 20, 30, 40]
x = l2.pop()
print(x, l2)

l2.pop(1)
print(l2)

# COUNTING ELEMENTS IN A LIST
# count(): Counts occurrences of a specific element

letters = list('abaca') # Converts a string into a list of characters
print(letters)
print(letters.count('a'))

# string[::-1]

# REVERSING AND SORTING LISTS
# reverse(): Reverses the order of elements in place
sequence = [1, 2, 3, 4]
sequence.reverse()
print(sequence)

# sort(): Sorts the list in ascending order (default)
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

# Descending Order
numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)
print(numbers)

# sorted(): Returns a new sorted list without modifying the original
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers, reverse=True)  # Creates a new sorted list
print(numbers, sorted_numbers)