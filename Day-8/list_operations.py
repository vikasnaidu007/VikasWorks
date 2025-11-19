# List Operations: Concatenation, Slicing, and Iteration

# -----------------------------
# 1. List Concatenation
# -----------------------------

l1 = [3, 4]
print(l1, id(l1))

l1 = l1 + [5, 6]    # Creates a new list (concatenation)
print(l1, id(l1))   # Memory address changes

l1 += [7, 8]        # Modifies the existing list in place
print(l1, id(l1))   # Memory address remains the same

# extend() adds elements individually
l1.extend([11, 12])
print(l1, id(l1))

# append() vs extend()
l1.append(['a', 'b'])
l1.extend(['x', 'y'])
print(l1, id(l1))

# -----------------------------
# 2. List Slicing
# -----------------------------
# str[start_index:stop_position:step]

numbers = [1, 2, 3, 4, 5]

# Output: [2, 3, 4]
print(numbers[1:4])
print(numbers)

# Output: [1, 2, 3]
print(numbers[0:3])

# Output: [3, 4, 5]
print(numbers[-3:])
print(numbers[2:])

# Output: [2, 4]
print(numbers[1:5:2])
print(numbers[1::2])

# Output: [5, 4, 3, 2, 1]
print(numbers[::-1])

# -----------------------------
# 3. Iteration and Membership Testing
# -----------------------------

ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1', '10.0.0.2']

# print(ip_list[0])
# print(ip_list[1])
# print(ip_list[2])

# ip = ip_list[0]
# ip = ip_list[1]
# ip = ip_list[2]
# Iterations: for, while

# Iterating over the list
for ip_address in ip_list:
    print(ip_address)

target_ip = '10.0.0.4'
if target_ip in ip_list:
    print(f'{target_ip} is in the list')

# 1. Modifying one list affects another if they share the same reference

l1 = [1, 2, 3]
l2 = l1  # l2 references the same object as l1
print(id(l1), id(l2))

l2[0] = 'xx'
l2.append(10)

print(l2, l1)

# To avoid this, use list.copy() for a shallow copy
l3 = l1.copy()
print(id(l1), id(l3))
l3.append('abc')
print(l3, l1)

# 2. Removing items from a list while iterating can cause unexpected behavior
nums = [1, 2, 3, 4, 5, 6, 7]
new_list = list()
for n in nums:
    if n >= 5:
        new_list.append(n)

print(new_list)

# Correct approach: Create a new list instead of modifying the original one during iteration
# [expression for n in nums if condition]

new_list = [n for n in nums if n >= 5]
print(new_list)
