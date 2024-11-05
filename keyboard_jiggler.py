import time
import threading
from pynput.keyboard import Controller

keyboard = Controller()

# Function to simulate key press
def press_key(time_interval):
    time.sleep(time_interval)
    while not stop_event.is_set():
        keyboard.press('a')
        keyboard.release('a')
        time.sleep(time_interval)

# Function to handle user input
def handle_input():
    global stop_event
    while True:
###        user_input = input("Enter command (Start/Stop/End): ").strip().lower()
        user_input = input("Enter command (Start/Stop): ").strip().lower()
        if user_input == 'start':
            if not stop_event.is_set():
                time_interval = float(input("Enter the time interval in seconds : " ).strip())
                print("Letter 'a' Will Be Printed With Time Interval Of : {} Seconds".format(time_interval))
                stop_event.clear()
                threading.Thread(target=press_key, args=(time_interval,)).start()
        elif user_input == 'stop':
            stop_event.set()
###        elif user_input == 'end':
###            stop_event.set()
            break

# Event to control the key pressing thread
stop_event = threading.Event()

# Start handling user input
handle_input()
