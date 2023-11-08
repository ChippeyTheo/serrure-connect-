from machine import Pin
import utime


class Pave:
    def __init__(self, row: tuple = (17, 16, 5, 18), col: tuple = (14, 27, 26, 25)):
        self.row_pins = [Pin(i, Pin.OUT) for i in row]  # 17, 16, 5, 18
        self.col_pins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in col]  # 14, 27, 26, 25
        self.key_map = [
            ['1', '2', '3', 'F'],
            ['4', '5', '6', 'E'],
            ['7', '8', '9', 'D'],
            ['A', '0', 'B', 'C']
        ]
        self.debounce_time = 20

    # read pressed key
    def read_keypad(self) -> str | None:
        for i, row_pin in enumerate(self.row_pins):
            row_pin.value(0)
            for j, col_pin in enumerate(self.col_pins):
                if col_pin.value() == 0:
                    utime.sleep_ms(self.debounce_time)
                    if col_pin.value() == 0:
                        row_pin.value(1)
                        return self.key_map[i][j]
            row_pin.value(1)
        return None

    def getkey(self) -> str:
        while True:
            key = self.read_keypad()
            if key is not None:
                return key
            utime.sleep_ms(150)
