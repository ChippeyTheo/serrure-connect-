from code_async import Code
from rfid_access_async import RFID
from SG90 import SG90
from lib.buzzer import Buzzer
from lib.led import Led
import uasyncio as asyncio


class Main:
    def __init__(self):
        self.__buzzer = Buzzer(pin=0)
        self.__code = Code(row=(33, 32, 16, 4), col=(14, 27, 26, 25), code="6969A", buzzer=self.__buzzer)
        self.__rfid = RFID(sck=22, mosi=21, miso=19, rst=18, cs=23)
        self.__sg90 = SG90(pin=13)
        self.__red_led = Led(pin=2)
        self.__green_led = Led(pin=15)
        self.__capteur =
        self.__rfid_access = False
        self.__code_access = False
    #     blanche, rouge, verte

    async def run(self):
        while True:
            self.__code_access = await self.__code.get_user_input()
            self.__rfid_access = await self.__rfid.read_rfid()
            if self.__code_access and self.__rfid_access:
                self.__green_led.on()
                await self.__buzzer.beep(1)
                await asyncio.sleep(0.5)
                await self.__buzzer.beep(1)
                self.__sg90.open()
            else:
                self.__red_led.on()
                self.__sg90.close()
            await asyncio.sleep(0.3)


if __name__ == "__main__":
    main = Main()
    asyncio.run(main.run())
