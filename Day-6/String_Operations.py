# CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

message = 'GenAI is amazing!'

print(message[4])
print(message[9])

# INDEXING: Accessing individual characters in a string
print(message[0])
print(message[5])
print(message[-1])
print(message[-7])

n = len(message)
print(n)
print(message[n-1])

# STRINGS ARE IMMUTABLE
# message[0] = 'X'
# print(message)

# STRING CONCATENATION
greeting = 'Hello, '
role = 'AI enthusiast'

# Combining strings using `+`
print(greeting + role + "!")

print('Version ' + str(4.0))


# STRING REPETITION

# * in integer 3 * 4 = 12

# Repeating a string multiple times
separator = '??'
print(separator * 10)

# STRING SLICING

tech = 'Machine Learning'
# Extracting a substring using slicing: string[start_index:stop_position]

print(tech[0:7])
print(tech[8:])
print(tech[:7])

# 'ning' (last four characters)
print(tech[-4:])

# Demonstrating different slicing variations: string[start_index:stop_position:step]

# tech = 'Machine Learning'
# 'McieLann'
print(tech[::2])

# 'gninraeL enihcaM' (reversed string)
print(tech[::-1])



