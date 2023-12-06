import uasyncio as asyncio
from mfrc522 import MFRC522
from machine import Pin, SoftSPI
import time

led_green = Pin(2, Pin.OUT)
led_red = Pin(2, Pin.OUT)

rfid_name = ["carte",
             "badge_bleu1",
             "badge_bleu2"]
rfid_UI = ["0x8ac41a05",
           "0xea87b463",
           "0x038fc90b"]

def get_user(uid):
    index = 0
    try:
        index = rfid_UI.index(uid)
        return rfid_name[index]
    except ValueError:
        return None

async def read_rfid():
    while True:
        print("Identifiez-vous")
        (stat, tag_type) = lecteur_rfid.request(lecteur_rfid.REQIDL)
        while stat != lecteur_rfid.OK:
            (stat, tag_type) = lecteur_rfid.request(lecteur_rfid.REQIDL)

        (stat, raw_uid) = lecteur_rfid.anticoll()
        if stat == lecteur_rfid.OK:
            card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            await asyncio.sleep(1)

            username = get_user(card_id)
            if username:
                led_green.value(1)
                led_red.value(0)
                print("accès autorisé, bienvenue :", username)
            else:
                led_green.value(0)
                led_red.value(1)
                print("accès refusé")

            await asyncio.sleep(2)

# Initialize SPI and RFID reader
spi = SoftSPI(baudrate=100_000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(27), miso=Pin(26))
spi.init()
lecteur_rfid = MFRC522(sck=22, mosi=21, miso=19, rst=4, cs=23)

# Run the asyncio event loop
asyncio.create_task(read_rfid())

async def main():
    await asyncio.gather(read_rfid())

if __name__ == "__main__":
    asyncio.run(main())