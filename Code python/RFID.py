'''
File: RFID.py
Project: Code python
Created Date: Su Jan 2022
Author: Julien Dagnelie
-----
Last Modified: Mon Jan 17 2022
Modified By: Julien Dagnelie & Loïc Tumelaire
-----
Copyright (c) 2022 Universite catholique de Louvain
-----
HISTORY:
Date   Sun Jan 16 2022   	By Julien Dagnelie	Comments
----------	---	---------------------------------------------------------
'''
from mfrc522 import MFRC522

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=6,rst=5)       # spi_id =?

def lecture():
    while True:
        reader.init()                                           # Start the connection to the RFID reader
        (stat, tag_type) = reader.request(reader.REQIDL)        # Request the current status of the reader. Nani ?
        if stat == reader.OK:                                   # Checks the value stored in stat, if the reader is ok, the code moves forward.
            card = int.from_bytes(bytes(uid),"little",False)    # Card store the data from an RFID card / tag
            print(card)                                         # Print the card details to the Python shell
            if card == 611994825:                               # Si la carte est le numéro ...
                print("Hello user1")

#Source:
#https://www.tomshardware.com/how-to/raspberry-pi-pico-powered-rfid-lighting
#https://github.com/danjperron/micropython-mfrc522