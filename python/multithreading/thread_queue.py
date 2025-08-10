import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing item {i}")
        q.put(i)  # Put data in queue
        time.sleep(1)
    q.put(None)  # Sentinel to signal the consumer to stop

def consumer():
    while True:
        item = q.get()
        if item is None:  # Stop signal
            break
        print(f"Consumed item {item}")
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()
print("Producer and Consumer finished")
