class Person:

    def __init__(self, name):
        self.name = name

    def get_moving(self):
        print("i am walking") 


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def get_moving(self):
        print("i am moving on my byke")


def run():
    person = Person("david")
    person.get_moving()

    cyclist = Cyclist("daniel")
    cyclist.get_moving()
             
if __name__ == "__main__":
    run()

# class Persona:

#     def __init__(self, nombre):
#         self.nombre = nombre
#         self._action = 'Ando caminando'

#     def avanza(self):
#         print(f'{self._action}')


# class Ciclista(Persona):

#     def __init__(self, nombre):
#         super().__init__(nombre)
#         self._action = 'Ando moviendome en mi bicicleta'

#     def avanza(self):
#         super().avanza()

# def main():
#     persona = Persona('David')
#     persona.avanza()

#     ciclista = Ciclista('Daniel')
#     ciclista.avanza()


# if __name__ == '__main__':
#     main()    