import threading

#subclassing thread 
class MyThread(threading.Thread):
    def run(self):
        print(f"{self.name} is running")

t = MyThread()
t.start()
t.join()
