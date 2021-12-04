def run ():
    num2 = int(input("selection the number one "))
    num3 = int(input("selection the number two "))
    sum = num2 + num3
    rest = num2 - num3
    divided = num2 / num3
    multiplication = num2 * num3
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