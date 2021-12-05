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
        hig = answer  

    answer = (high + low) / 2

print(f"the square root of {objetive} is {answer}")  
