import threading
import time


def tow():
    while True:
        print('tow')


def foo():
    # 输出此刻的线程名
    print(threading.current_thread().name)
    # 创建一个daemon线程去跑tow函数
    t1 = threading.Thread(target=tow, daemon=True, name='tow')
    t1.start()
    t1.join()


if __name__ == "__main__":
    # 创建一个daemon线程去跑foo函数
    t = threading.Thread(target=foo, daemon=True, name='主')
    t.start()
    # time.sleep(3)
    t.join()
    print('----end-----')