import threading
import time

event = threading.Event()

def wait_for_event():
    print("Waiting for event...")
    event.wait()
    print("Event received!")

t = threading.Thread(target=wait_for_event)
t.start()

time.sleep(2)
print("Setting event")
event.set()
