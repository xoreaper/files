for calc in range(1, 5, 2):
    opt = input("What operation do you wanna do +,-,/,*,= ")

    number1 = float(input("Enter the first Number = "))
    number2 = float(input("Eneter the second Number = "))

    if opt == "+":
        result = number1 + number2
        print(result)
    elif opt == "-":
        result = number1 - number2
        print(result)

    elif opt == "/":
        result = number1 / number2
        print(result)

    elif opt == "*":
        result = number1 * number2
        print(result)

    else:
        print("invalid input")
    result = None

if result is not None:
    print("The output is :", result)
