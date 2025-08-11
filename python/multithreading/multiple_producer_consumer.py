import threading
import queue
import time
import random

q = queue.Queue()

def producer(id):
    for _ in range(3):
        item = f"P{id}-Item-{random.randint(1,100)}"
        q.put(item)
        print(f"Producer {id} -> {item}")
        time.sleep(random.random())
    q.put(None)  # Sentinel

def consumer(id):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumer {id} <- {item}")
        q.task_done()

# Create producers
producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]

for t in producers + consumers:
    t.start()

for t in producers:
    t.join()

# Send stop signal to consumers
for _ in consumers:
    q.put(None)

for t in consumers:
    t.join()

print("All work done")
