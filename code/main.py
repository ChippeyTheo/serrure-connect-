from code_async import Code
from rfid_access_async import RFID
from SG90 import SG90
import uasyncio as asyncio


class Main:
    def __init__(self):
        self.__code = Code()
        self.__rfid = RFID()
        self.__sg90 = SG90()
        self.__rfid_access = False
        self.__code_access = False

    async def run(self):
        while True:
            self.__code_access = await self.__code.get_user_input()
            self.__rfid_access = await self.__rfid.read_rfid()
            if self.__code_access and self.__rfid_access:
                self.__sg90.open()
            else:
                self.__sg90.close()
            await asyncio.sleep(0.3)


if __name__ == "__main__":
    main = Main()
    asyncio.run(main.run())
