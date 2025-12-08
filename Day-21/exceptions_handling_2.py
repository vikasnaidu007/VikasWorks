while True:
    try:
        a = int(input("Enter a value: "))
        b = int(input("Enter b Value: "))
        # c = int(input("Enter c Value: "))
        c = 7
        d = a / b + c

    except ZeroDivisionError as err:
        print(f'Division by zero is not permitted: {err.args}')
    except TypeError as err:
        print(f'Type error: {err.args}')
    except Exception as err:
        print(err.args)
    else:
        print(d)
        break
    finally:
        print('Good Bye!!!!')

age = 4
if age < 0:
    raise Exception('Age less than Zero not permitted')