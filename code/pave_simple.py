from pave_numerique import Pave
from time import sleep

pave = Pave()

code = "1234A"
userInput = ""


def iscode(entry: str) -> bool:
    return code == entry


while True:
    print("ok")
    userInput += pave.getkey()
    print(userInput)
    if len(userInput) == len(code):
        if iscode(userInput):
            print(":)")
        else:
            print(":(")
        userInput = ""
    sleep(1)
