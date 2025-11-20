# TUPLE BASICS

# Defining a tuple with geographical coordinates
location = (37.7749, -122.4194)

# Accessing tuple elements using indexing
print(location[0])
print(location[1])

# Creating empty tuples using two different methods
empty_tuple1 = tuple()
empty_tuple2 = ()

# A single-element tuple requires a trailing comma
number = (10,)
print(type(number))

# Converting lists and strings to tuples
nums = tuple([1, 2, 3])     # Creates a tuple from a list
print(type(nums))
print(len(nums))

letters = tuple('hello')    # Creates a tuple from a string
print(len(letters))
print(letters)

# TUPLE UNPACKING
# a = 10
# x, y = 10, 20
latitude, longitude  = location
print(latitude, longitude)

# NESTED TUPLES
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[2][1])

# Tuples are immutable, the following line would cause an error:
# location[0] = 23.3456

numbers = (1, 2, 3, 4, 5)
print(numbers)

for element in numbers:
    print(element)

item = 7
if item in numbers:
    print("Item is available")

# Slicing Tuple
tuple_data = (1, 2, 3, 4, 5)
print(tuple_data[1:2])
print(tuple_data[1:3])
print(tuple_data[::-1])