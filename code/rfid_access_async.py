import uasyncio as asyncio
from lib.mfrc522 import MFRC522
from machine import Pin, SoftSPI


class RFID(MFRC522):
    def __init__(self):
        super().__init__(sck=22, mosi=21, miso=19, rst=4, cs=23)
        self.__rfid_name = ["carte",
                            "badge_bleu1",
                            "badge_bleu2"]
        self.__rfid_UI = ["0x8ac41a05",
                          "0xea87b463",
                          "0x038fc90b"]
        self.__spi = SoftSPI(baudrate=100_000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(27), miso=Pin(26))
        self.spi.init()

    def __get_user(self, uid):
        if uid in self.__rfid_UI:
            index = self.__rfid_UI.index(uid)
            return self.__rfid_name[index]
        return None

    async def read_rfid(self):
        while True:
            print("Identifiez-vous")
            (stat, tag_type) = self.request(self.REQIDL)
            while stat != self.OK:
                (stat, tag_type) = self.request(self.REQIDL)
            (stat, raw_uid) = self.anticoll()
            if stat == self.OK:
                card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                await asyncio.sleep(1)

                username = self.__get_user(card_id)
                if username:
                    print("accès autorisé, bienvenue :", username)
                    return True
                print("accès refusé")
                return False

            await asyncio.sleep(2)


if __name__ == "__main__":
    rfid = RFID()
    asyncio.run(rfid.read_rfid())
