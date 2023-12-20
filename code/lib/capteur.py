import machine


class Capteur:
    def __init__(self, pin):
        self.__pin = machine.Pin(pin, machine.Pin.IN)

    def read(self):
        return bool(self.__pin.value())
