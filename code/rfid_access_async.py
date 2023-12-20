import uasyncio as asyncio
from lib.mfrc522 import MFRC522
from machine import Pin, SoftSPI
from lib.buzzer import Buzzer


class RFID(MFRC522):
    def __init__(self,sck=22, mosi=23, miso=19, rst=18, cs=5, buzzer: Buzzer=None):
        super().__init__(sck=sck, mosi=mosi, miso=miso, rst=rst, cs=cs)
        self.__rfid_name = ["carte",
                            "badge_bleu1",
                            "badge_bleu2"]
        self.__rfid_UI = ["0x8ac41a05",
                          "0xea87b463",
                          "0x038fc90b"]
        self.__spi = SoftSPI(baudrate=100_000, polarity=0, phase=0, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))
        self.spi.init()
        self.__buzzer = buzzer

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
                    if self.__buzzer is not None:
                        await self.__buzzer.beep(1)
                    return True
                print("accès refusé")
                if self.__buzzer is not None:
                    await self.__buzzer.beep(3)
                return False

            await asyncio.sleep(2)


if __name__ == "__main__":
    rfid = RFID()
    asyncio.run(rfid.read_rfid())
