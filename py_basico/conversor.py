def conversor(tipo_pesos, valor_dolar):
    pesos = input("cuantos pesos " + tipo_pesos + " tienes:")
    pesos = float(pesos)
    valor_pesos = 3833
    dolares =  pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " pesos " + tipo_pesos)

if __name__ == "__main__":    

    menu = """"
1 colombia
2 argentina
3 mexicamos

elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("ingresa un numero correcto porfa ;")