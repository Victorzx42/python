
class Car:

    def __init__(self,model, mark, color):
        self.model = model
        self.mark = mark
        self.color = color
        self._status = "in repose"
        self._motor = Motor(cylinders=4)
        self.brakes = brakes

    def speed_up(self, type="slowly"):
        if type == "fast":
            self._motor.inject_gasoline(10)  
        else:
            self._motor.inject_gasoline(3) 

        self._status= "in movement" 

    def reduce_speed(self, type="fast"):
        if type == "fast":
            self.brakes
        else:
            self._motor.inject_gasoline(3)  

        self._status= "in movement"       





class Motor:

    def __init__(self, cylinders, type="gasoline"):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self, quantity):
        pass
