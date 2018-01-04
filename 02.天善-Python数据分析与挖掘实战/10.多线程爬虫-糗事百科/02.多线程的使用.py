import threading
import time

class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(0, 10):
            print('我是线程A')
            time.sleep(1)

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(0, 10):
            print('我是线程B')
            time.sleep(2)


t1 = A()
t1.start()
t2 = B()
t2.start()
