def opt(operator, num1, num2):

    if operator == '+':
        result = num1 + num2

    elif operator == '-':
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2

    elif operator == '/':
        result = num1 / num2

    else:
        print("Invalid operator.")
        return None

    return result


operator = input("Enter an operator (+,-,*,/): ")
print()
