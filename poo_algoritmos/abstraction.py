
class washer:

    def __init__(self):
        pass

    def wash(self, temperature="hot"):
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge() 

    def _fill_water_tank(self, temperature):
        print(f"filling water tank {temperature}")

    def _add_soap(self):
        print("add soap")

    def _wash(self):
        print("washing the clothe") 

    def _centrifuge(self):
        print("_centrifuge the clothe")    


if __name__ == "__main__":
    washer = washer()
    washer.wash()

