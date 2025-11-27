# Iteration concept
    # starting (at index 0)
    # Increment
    # Condition

# Working with Ranges in Python

# -----------------------------
# 1. Using range() in a Loop
# -----------------------------

# range(start, stop) -> stop is exclusive
for participant_id in range(1, 101):
    print(f'Assigning ID to participant #{participant_id}')

# -----------------------------
# 2. Creating a List from a Range
# -----------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))
print(numbers)

even_numbers = list(range(0, 101, 2))
print(even_numbers)

# -----------------------------
# 3. Looping a Fixed Number of Times (Ignoring Index)
# -----------------------------
for _ in range(5): # The underscore (_) is a convention for an unused variable
    print('Analyzing Data')

