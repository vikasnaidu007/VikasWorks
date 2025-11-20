'''
Challenge #1

A company has a revenue of 45,897,513.
Calculate its profit, assuming profit is 12.7% of the revenue.
Display the result rounded to two decimal places.
'''

# Calculate company's profit from revenue

revenue = 45_897_513
profit_percentage = 12.7 / 100
profit = revenue * profit_percentage

# Display profit with 2 decimal places
print(f'Company\'s profit: ${profit:.2f}')

'''
Challenge #2

Consider the following string declaration which is part of the output of a Linux command.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

Try to solve the challenge in more than one way.
'''
my_str = 'wlo1 Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
mac = my_str.split()[-1]
print(mac)

'''
Challenge #3

Display the following strings literally:

It displayed: "You've got an error!"

\n means a new line.

\ is known as the escape character.
'''

# Solution 1
message = "It displayed: \"You've got an error!\""

# Solution 2
message = 'It displayed: "You\'ve got an error!"'
print(message)


print('\\n means a new line.')
# or
print(r'\n means a new line')  # r'' means a raw string where \ doesn't have a special meaning.

print('\\ is known as the escape character.')

'''
Challenge #4

Write a Python script to convert feet (ft) to centimeters (cm).

Conversion: 1 ft = 30.48 cm

Prompt the user to enter a value in feet.

Display the result in centimeters with two decimal places, formatted using an f-string.
'''

# ft = float(input('Enter distance (in ft):'))
# cm = ft * 30.48
# print(f'{ft} ft = {cm:.2f} cm')

'''
Challenge #5

Write a Python script to check if a string is a palindrome.
'''

s1 = 'mom'
print(f'Is s1 palindrome? => {s1 == s1[::-1]}')

'''
Challenge #6

Change the solution of the previous challenge to ignore whitespace and letter case when checking if a string is a palindrome.
'''

s1 = 'Rats live on no evil star'
s1 = s1.replace(' ', '')
s1 = s1.lower()
print(f'Is s1 palindrome? => {s1 == s1[::-1]}')

'''
Challenge #7

Write a Python script that extracts the first and last two characters from a user-entered string.

Example:

Input: 'Hello!'

Output: 'Heo!'
'''

my_str = 'Hello!' # input('Enter a string(min 2 chars):')
new_str = my_str[:2] + my_str[-2:]
print(new_str)


'''
Challenge #8

Write a Python script that replaces all occurrences of the first character in a string with '$', except for the first occurrence itself.

Example:

Input: 'mamama'
Output: 'ma$a$a'
'''
my_str = 'mamama'
char = my_str[0]
new_str = my_str[1:].replace(char, '$')
new_str = char + new_str
print(new_str)

'''
Challenge #9

Write a Python program to remove the character at the nth index from a non-empty string.

The nth index is provided by the user.
'''

n = int(input('Enter the nth index char to remove:'))
my_str = input('Enter the string to change:')
first_part = my_str[0:n]
last_part = my_str[n+1:]
new_str = first_part + last_part
print(new_str)

'''
Challenge #10

Write a Python script that removes characters at odd index positions from a given string.
'''
my_str = input('Enter the string to change:')
new_str = my_str[::2]
print(new_str)

'''
Challenge #11

Write a Python script that prompts the user for a circle's radius and calculates its area.

Formula: Area = π * r² (π = 3.1415)

Display the area with four decimal places using an f-string.
'''

radius = float(input('Enter circle radius:'))
area = 3.1415 * radius ** 2
print(f'The area of a circle with a radius of {radius} is {area:.4f}')

'''
Challenge #12

Write a Python script that counts the number of occurrences of a substring in a given string, ignoring letter case.
'''

my_str = "Welcome to Romania. romania is an awesome country, isn't it? Hello roMania!"
sub_string = "Romania"

# convert string to lowercase
tmp_str = my_str.lower()

# use the count function
count = tmp_str.count(sub_string.lower())
print(f'The substring "Romania" appears {count} times in the string.')

'''
Challenge #13

Write a Python script to format a number using:

US/UK format: A comma , as the thousands separator

EU format: A period . as the thousands separator

Example:

Input: 1234567

Output: 1,234,567 (US/UK) and 1.234.567 (EU)
'''

n = 12384756982
n_comma = f'{n:,}'

print(n_comma)

print(n_comma.replace(',', '.'))

