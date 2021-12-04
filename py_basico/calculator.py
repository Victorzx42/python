def run ():
    num1 = int(input("selection the number one "))
    num2 = int(input("selection the number two "))
    sum = num1 + num2
    rest = num1 - num2
    divided = num1 / num2
    multiplication = num1 * num2
    operations = int(input("""selection the numbers for the operation
    1 = +
    2 = -
    3 = /
    4 = *
    """))
    if operations == 2:
        print(sum)
    elif operations == 2:
        print(rest)
    elif operations == 3:
        print(divided)
    elif operations == 4:
        print(multiplication)
    else:
        print("please choice a number valid")

    

if __name__ == "__main__":
    run()    