import threading
import time
from multiprocessing import Process

num = 0

class A(threading.Thread):
    def run(self) -> None:
        global num
        q1.acquire()
        for i in range(1000000):
            num += i
        q1.release()
        time.sleep(0.2)
        print("A : {}".format(num))


class B(threading.Thread):
    def run(self) -> None:
        global num
        q1.acquire()
        for i in range(1000000):
            num += i
            time.sleep(0.2)
        q1.release()
        print("B : {}" .format(num))


class C(threading.Thread):
    def run(self) -> None:
        global num
        q1.acquire()
        for i in range(1000000):
            num += i
            time.sleep(0.2)
        q1.release()
        print("B : {}" .format(num))


class D(threading.Thread):
    def run(self) -> None:
        global num
        q1.acquire()
        for i in range(1000000):
            num += i
            time.sleep(0.2)
        q1.release()
        print("B : {}" .format(num))


def mu():
    while True:
        print('mu')
        time.sleep(1)


q1 = threading.Lock()
# q2 = threading.Lock()
# m = Process(target=mu)
# m.start()
# while True:
#     print('z')
#     time.sleep(1)

if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    d = D()
    a.start()
    b.start()
    c.start()
    d.start()
    time.sleep(2)
    print("总 : {}".format(num))