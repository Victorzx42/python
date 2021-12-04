def run ():
    num1 = int(input("selection the number one "))
    num2 = int(input("selection the number two "))
    sum = num1 + num2
    rest = num1 - num2
    divided = num1 / num2
    multiplication = num1 * num2
    operation = int(input("""selection the numbers for the operation
    1 = +
    2 = -
    3 = /
    4 = *
    """))
    if operation == 2:
        print(sum)
    elif operation == 2:
        print(rest)
    elif operation == 3:
        print(divided)
    elif operation == 4:
        print(multiplication)
    else:
        print("please choice a number valid")

    

if __name__ == "__main__":
    run()    