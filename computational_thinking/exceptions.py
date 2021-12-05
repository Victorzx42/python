
def divided_elements_of_list(lists, divider):
    try:
        return [i / divider for i in lists]
    except ZeroDivisionError as e:
        return lists    

lists = list(range(10))    
divider = 0

print(divided_elements_of_list(lists, divider))