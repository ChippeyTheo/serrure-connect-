import uasyncio as asyncio
from pave_numerique import Pave
from time import sleep

pave = Pave()

code = "1234A"
userInput = ""

def iscode(entry) -> None:
    return code == entry

async def get_user_input():
    global userInput
    global code
    while True:
        userInput += pave.getkey()
        print(userInput)
        if len(userInput) == len(code):
            if iscode(userInput):
                print(":)")
            else:
                print(":(")
            userInput = ""
        await asyncio.sleep(0.3)

async def main():
    await asyncio.gather(get_user_input())

if __name__ == "__main__":
    asyncio.run(main())