def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

    print(ve)


def run():
    num = input('Ingresa un número: ')
    assert num <= 0, "you must enter a positive number"
    assert num.isnumeric(), "you must enter a number"
    print(divisors (int(num)))
    print("Finish my programer")

    print("you must enter a number ")      


if __name__ == '__main__':
    run()