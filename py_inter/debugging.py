def divisors(num):
    try:
        if num < 0 or num == 0:
            raise ValueError("you must enter a positive number")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    #return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Finish my programer")
    except ValueError:
        print("you must enter a number ")      


if __name__ == '__main__':
    run()