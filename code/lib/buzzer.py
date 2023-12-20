import machine
import uasyncio as asyncio


class Buzzer:
    def __init__(self, pin):
        self.pin = machine.Pin(pin, machine.Pin.OUT)
        self.pin.off()

    async def beep(self, duration):
        self.pin.on()
        await asyncio.sleep(duration)
        self.pin.off()
