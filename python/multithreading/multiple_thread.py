import threading

def worker(num):
    print(f"Worker {num} is working")

#Using Multiple Threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
