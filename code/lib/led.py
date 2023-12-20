import machine
import uasyncio as asyncio


class Led:
    def __init__(self, pin):
        self.pin = machine.Pin(pin, machine.Pin.OUT)
        self.pin.off()

    def on(self):
        self.pin.on()

    def off(self):
        self.pin.off()

    async def blink(self, duration):
        self.on()
        await asyncio.sleep(duration)
        self.off()
