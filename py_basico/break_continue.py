def run ():
    # for contador in range(1000):
    #     if contador %2 != 0:
    #         continue
    #     print(contador)
    # ///////////////////////////
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    # texto = input("escribe un texto: ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)
    numero = 12
    multiplicacion = numero*20
    while multiplicacion<1000000:
        print(multiplicacion)
        numero = numero+1
        multiplicacion = numero*20
        if multiplicacion > 180000:
             break 
        

if __name__ == "__main__":
    run()