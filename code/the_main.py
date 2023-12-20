from code_async import Code
from rfid_access_async import RFID
from SG90 import SG90
from lib.buzzer import Buzzer
from lib.led import Led
from lib.capteur import Capteur
import uasyncio as asyncio


class Main:
    def __init__(self):
        self.__buzzer = Buzzer(pin=0)
        self.__code = Code(col=(4, 16, 32, 33), row=(25, 26, 27, 14), code="6969A", buzzer=self.__buzzer)
        self.__rfid = RFID(sck=22, mosi=21, miso=19, rst=18, cs=23, buzzer=self.__buzzer)
        self.__sg90 = SG90(pin=13)
        self.__red_led = Led(pin=2)
        self.__green_led = Led(pin=15)
        self.__capteur = Capteur(pin=12)

    async def run(self):
        while True:
            print("Main.run()")
            print("Capteur : ", self.__capteur.read())
            if not self.__capteur.read():
                self.__green_led.off()
                if await self.__code.get_user_input() and await self.__rfid.read_rfid():
                    self.__green_led.on()
                    await self.__buzzer.beep(1)
                    await asyncio.sleep(0.5)
                    await self.__buzzer.beep(1)
                    self.__sg90.open()
                    await asyncio.sleep(10)
                else:
                    self.__red_led.on()
                    self.__sg90.close()
            else:
                self.__green_led.on()
            await asyncio.sleep(0.3)


if __name__ == "__main__":
    main = Main()
    asyncio.run(main.run())
