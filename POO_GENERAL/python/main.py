from car import Car
from account import Account



if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("AMS234", Account("victor morales", "ANDA123")) 
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("AJE44F", Account("Henry morales", "ASJ344"))
    print(vars(car2))
    print(vars(car2.driver))