import threading
import time

succeed_sum = 0


def worker(count = 10):
    """生产杯子"""
    global succeed_sum
    for i in range(1,count+1):
        time.sleep(0.5)
        print(threading.current_thread().name, '生产第{}个杯子'.format(i))

        succeed_sum += 1
    print('生产完成')


workeron = threading.Thread(daemon=False, target=worker, name='工人1', args=(5,))
workeron.start()
workeron.join()

print('生产了：', succeed_sum)
