from pave_numerique import Pave
from time import sleep

pave = Pave()

code = "1234A"
userInput = ""


def iscode(entry) -> None:
    return code == entry


while True:
    userInput += pave.getkey()
    if len(userInput) == len(code):
        if iscode(userInput):
            print(":)")
        else:
            print(":(")
        userInput = ""
    sleep(0.3)

