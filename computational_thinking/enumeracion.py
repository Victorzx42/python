#/////////SEARCH EXACT
# objetive = int(input("choose a whole number: "))
# answer = 0

# while answer**2 < objetive:
#     answer += 1

# if answer**2 == objetive:
#     print(f"the square root of {objetive} is {answer}")
# else:
#     print(f"{objetive} no have a square root exact")    

#/////////SEARCH INEXACT
# objetive = int(input("choose a number: "))
# epsilon = 0.01
# step = epsilon**2
# answer = 0.0

# while abs(answer**2 - objetive) >= epsilon and answer <= objetive:
#     answer += step 

# if abs(answer**2 - objetive) >= epsilon:
#     print(f"no choose the square root {objetive}")
# else:
#     print(f"the sqaure root of {objetive} is {answer}")   
objetive = int(input("choose a number: "))
epsilon = 0.001
low = 0.0
high = max(1.0, objetive)
answer = (high + low) / 2

while abs(answer**2 - objetive) >= epsilon:
    print(f"low={low}, high={high}, answer={answer}")
    if answer**2 < objetive:
        low = answer
    else:
        high = answer  

    answer = (high + low) / 2

print(f"the square root of {objetive} is {answer}")    