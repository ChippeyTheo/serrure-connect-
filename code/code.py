from lib.pave_numerique import Pave
from time import sleep

pave = Pave()

code = "1234A"
userInput = ""


def iscode(entry: str) -> bool:
    return code == entry


def enter_new_code(new: str) -> str:
    print("Enter new code : ", end="")
    while len(new) != len(code):
        new += pave.getkey()
        print(new, end="")
    return new


while True:
    userInput += pave.getkey()
    print(userInput)
    if userInput[:-1] == 'C':
        code = enter_new_code(code)
        userInput = ""
    if len(userInput) == len(code):
        if iscode(userInput):
            print(":)")
        else:
            print(":(")
        userInput = ""
    sleep(0.3)