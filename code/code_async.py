import uasyncio as asyncio
from lib.pave_numerique_async import Pave


class Code(Pave):
    def __init__(self, code: str = "1234A", row: tuple = (17, 16, 5, 18), col: tuple = (14, 27, 26, 25)):
        super().__init__(row, col)
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
                    return True
                self.__userInput = ""
                return False
            await asyncio.sleep(0.3)


if __name__ == "__main__":
    code = Code()
    asyncio.run(code.get_user_input())
