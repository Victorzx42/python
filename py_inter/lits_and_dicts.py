def run ():
    my_list =[1, "hello", True, 4-5]
    my_dict ={"firstname": "victor",
              "lastname" : "morales"}

super_list = [
    {"firstname": "victor", "lastname" : "morales"},
    {"firstname": "daniel", "lastname" : "morales"},
    {"firstname": "diana", "lastname" : "molina"},
    {"firstname": "mariana", "lastname" : "guitierrez"},
    {"firstname": "hu", "lastname" : "tao"},
]   

super_dict = {
    "natural_numbers" : [1, 2, 3, 4, 5, 6],
    "integer_numbers" : [-1, -2, 0, 1, 2],
    "floating_numbers" : [1.1, 1.2, 4.5, 6.43]
}

# for key1, value1 in super_dict.items():
#     print(key1, "-", value1)

# for i in super_list:
#     for key2, values2 in i.items():
#         print(key2, "-", values2)  

# squares = []
# for i in range(1,101):
#     if i % 3 != 0:
#         squares.append(i **2)

squares = [i **2 for i in range(1, 101) if i % 3 != 0]
multiples = [i for i in range (1, 99999) if i % 36 == 0]

print(squares)
print(multiples)
    










if __name__ == "__main__":
    run()