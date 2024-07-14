import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

# TOGGLE_KEY = KeyCode(char="s")
TOGGLE_KEY = Key.f6
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01)

def toggle_event(key):
    if key == TOGGLE_KEY:
        print('clicking')
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

