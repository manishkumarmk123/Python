#pip install keyboard

import keyboard as kb
from threading import Thread
SHOULD_RECORD = True
def start_rec():
    while SHOULD_RECORD:
        rec = kb.record(until="escape+ctrl+shift")
        seq = kb.get_typed_strings(rec)
        with open("records.txt", "a") as f:
            f.write("".join(seq) + "\n")
        print("saved")
def stop_rec():
    global SHOULD_RECORD
    SHOULD_RECORD = False
start_thread = Thread(target=start_rec)
start_thread.start()
kb.add_hotkey("ctrl+alt+s", stop_rec)
kb.wait()
