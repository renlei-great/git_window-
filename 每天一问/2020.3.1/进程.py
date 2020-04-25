
import multiprocessing
from multiprocessing import Pool
import time

def test1():
    while True:
        print('test1')
        time.sleep(0.2)


def test2():
    while True:
        print('test2')
        time.sleep(0.2)


def test3():
    while True:
        print('test3')
        time.sleep(0.2)


def test4():
    while True:
        print('test4')
        time.sleep(0.2)


# t1 = multiprocessing.Process(target=test1)
# t2 = multiprocessing.Process(target=test2)
# t1.start()
# t2.start()

def main():
    # t1 = multiprocessing.Process(target=test1)
    # t2 = multiprocessing.Process(target=test2)
    # t3 = multiprocessing.Process(target=test2)
    # t4 = multiprocessing.Process(target=test2)
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    po = Pool(2)
    for i in range(1,5):
        name = 'test' + str(1)
    # print(id(name))
    # print(id(test1))
        po.apply_async(name)


if __name__ == "__main__":
    main()