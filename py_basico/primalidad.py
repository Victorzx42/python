# def es_primo(numero):
#     contador = 0

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador +=1
#     if contador == 0:
#         return True
#     else:
#         return False


# def run():
#     numero = int(input("escribe un numero: "))
#     if es_primo(numero):
#         print("es primo")
#     else:
#         print("no es primo")    


# if __name__ == "__main__":
#     run()




def es_primo(numero): 
     
    if numero % 2 == 0:
        return False
    elif numero % 3 == 0 :
        return False    
    elif numero % 5 == 0:
        return False   
    elif numero % 7 == 0:
        return False   
    elif numero % 11 == 0 :
        return False                     
    else:
        return True            

def run():
    dos = 2
    tres = 3
    cinco = 5
    siete = 7
    once = 11
    numero = int(input("escribe un numero: "))
    if numero == dos:
        print("es primo")
    elif numero == tres:
        print("es primo")
    elif numero == cinco:
        print("es primo")
    elif numero == siete:
        print("es primo")
    elif numero == once:
        print("es primo")
    elif es_primo(numero):
        print("es primo")
    else:
        print("no es primo")    


if __name__ == "__main__":
    run()
