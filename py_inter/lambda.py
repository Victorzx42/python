from functools import reduce

def run ():
# palindrome = lambda string: string == string[::-1]

# print(palindrome("ana"))

    my_lits = [1, 2, 3, 4, 5]
    squares_map = list(map(lambda x: x**2, my_lits))
    squares_filter = list(filter(lambda x: x%2 != 0, my_lits))
    squares_reduce = reduce(lambda a,b: a * b, my_lits)
    print(squares_map)
    print(squares_filter)
    print(squares_reduce)
if __name__ == "__main__":
    run()        