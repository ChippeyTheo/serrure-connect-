import uasyncio as asyncio
from lib.pave_numerique_async import Pave
from lib.buzzer import Buzzer


class Code(Pave):
    def __init__(self, code: str = "1234A", row: tuple = (17, 16, 5, 18), col: tuple = (14, 27, 26, 25),
                 buzzer: Buzzer = None):
        super().__init__(row, col, buzzer)
        self.__buzzer = buzzer
        self.__code = code
        self.__userInput = ""

    def __iscode(self, entry) -> None:
        return self.__code == entry

    async def get_user_input(self):
        while True:
            self.__userInput += await self.getkey()
            print(self.__userInput)
            if len(self.__userInput) == len(code):
                if self.__iscode(self.__userInput):
                    self.__userInput = ""
                    if self.__buzzer is not None:
                        await self.__buzzer.beep(1)
                    return True
                self.__userInput = ""
                if self.__buzzer is not None:
                    await self.__buzzer.beep(3)
                return False
            await asyncio.sleep(0.3)


if __name__ == "__main__":
    code = Code()
    asyncio.run(code.get_user_input())
