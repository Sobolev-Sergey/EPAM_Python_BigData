import time
from threading import Lock, Thread, RLock

counter = 0
lock = RLock()


def hello(name, interval):
    while True:
        global counter
        lock.acquire()
        lock.acquire()
        counter += 1
        print("Hello, %s (%d)" % (name, counter))
        lock.release()
        lock.release()
        time.sleep(interval)


if __name__ == '__main__':
    t1 = Thread(target=hello, args=("Kirill", 1))
    t2 = Thread(target=hello, args=("Artem", 1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
