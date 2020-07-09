import time
from threading import Thread


def hello(name, interval):
    while True:
        print("Hello, %s" % name)
        time.sleep(interval)


if __name__ == '__main__':
    t1 = Thread(target=hello, args=("Kirill", 2))
    t2 = Thread(target=hello, args=("Artem", 3))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
