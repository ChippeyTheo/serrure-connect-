from mfrc522 import MFRC522
from machine import Pin
from machine import SoftSPI
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
    except:
        return 0    

spi = SoftSPI(baudrate=100_000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(27), miso=Pin(26))
spi.init()
lecteur_rfid = MFRC522(sck=14, mosi=27, miso=26, rst=33, cs=25) #sda = cs

while True:
    print("Identifiez-vous")
    (stat, tag_type) = lecteur_rfid.request(lecteur_rfid.REQIDL)
    while stat!=lecteur_rfid.OK:
        (stat, tag_type) = lecteur_rfid.request(lecteur_rfid.REQIDL)
            
    (stat, raw_uid) = lecteur_rfid.anticoll()
    if stat == lecteur_rfid.OK:
        card_id ="0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
        time.sleep(1)
        
        username = get_user(card_id)
        if username != 0:
            led_green.value(1)
            led_red.value(0)
            print("accès autorisé, bienvenue :", username)
        else:
            led_green.value(0)
            led_red.value(1)
            print("accès refusé")
            
        time.sleep(2)