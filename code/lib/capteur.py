import machine
import uasyncio as asyncio


class Capteur:
    def __init__(self, pin):
        self.__pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.__state = False

    async def read(self):
        while True:
            self.__state = self.__pin.value()
            await asyncio.sleep_ms(100)

    @property
    def state(self):
        return self.__state
