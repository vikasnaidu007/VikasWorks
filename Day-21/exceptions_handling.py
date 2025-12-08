# Python Errors and Exception Handling

# Types of Exceptions:
# 1. Syntax Errors # IDE helping
# 2. Runtime Errors

# for x in range(10):
#     print(x)
# print(x)
#
# with open('a.txt', 'r') as file:
#     print(file.read())
#
# a, b = 10, 2
# print(a/b)

# a = int(input("Enter a First number: "))
# b = int(input("Enter a Second number: "))
#
# try:
#     c = a / b
#     print(c)
# except:
#     print("Can't perform division by zero")
# finally:
#     print("Good Bye!!!!")

try:
    file = open('a.txt', 'r')
    file.write('writing to the file')
except:
    print("1. Can't write to a file")
else:
    print("2. File has been written Successfully")
finally:
    print("3. This code is executed always")
    print(file.closed)
    if not file.closed:
        file.close()
    print(file.closed)