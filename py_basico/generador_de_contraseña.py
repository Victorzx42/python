import random

def generation_password():
    capital_letters = ["A", "B", "C", "D", "E", "F", "G"]
    tiny = ["a", "b", "c", "d", "e", "f", "g"]
    symbols = ["!", "#", "&", ")", "%", "¡", "$"]
    numbers = ["1", "2", "4", "6", "8", "9", "0"]

    characters = capital_letters + tiny + symbols + numbers

    password = []

    for i in range(15):
        characters_random = random.choice(characters)
        password.append(characters_random)

    password = "".join(password)  
    return password 

def run ():
    password = generation_password()
    print("your new password is: " + password)

if __name__ == "__main__":
    run()
