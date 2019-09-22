#!usr/bin/python3
#coding=UTF-8
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import os
import sys
#import threading
import RPi.GPIO as GPIO
import requests
from os import path
#from wakeonlan import send_magic_packet

key1 = 5 #power button
key2 = 6 #up button
key3 = 13 #down button
key4 = 19 #enter button

GPIO.setmode(GPIO.BCM)

GPIO.setup(key1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
try:

    if __name__ == '__main__':
        while True:
            key1state = GPIO.input(key1)
            key2state = GPIO.input(key2)
            key3state = GPIO.input(key3)
            key4state = GPIO.input(key4)
            
            if key1state == False:
                if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
                    r = requests.get('http://localhost:6000/signup')
                else:
                    r = requests.get("http://localhost:6000/showAddress")
                time.sleep(0.5)
            elif key2state == False:
                print('Key2 Pressed')
                time.sleep(0.5)
            elif key3state == False:
                print('Key3 Pressed')
                time.sleep(0.5)
            elif key4state == False:
                print('Key4 Pressed')
                time.sleep(0.5)
except Exception:
    print ("traceback.format_exc():\n%s") % traceback.format_exc()
    exit()


