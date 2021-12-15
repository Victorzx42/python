def run ():
    my_dicts = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dicts[i] = i**3

    # my_dicts = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    my_dicts = {i: i**0.5 for i in range(1, 1001)}

    print(my_dicts)
#///////////////////////////////////////////
    my_lits = [1, 2, 3, 4, 5]

    my_lits_modificate = [i**2 for i in my_lits]

    print(my_lits_modificate)

    
if __name__ == "__main__":
    run()    