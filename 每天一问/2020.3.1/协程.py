import gevent
from gevent import monkey

monkey.patch_all()


def f11():
    for i in range(5):
        print('f1')
        gevent.sleep(0.5)


def f22():
    for i in range(5):
        print('f2')
        gevent.sleep(0.5)


def f33():
    for i in range(5):
        print('f3')
        gevent.sleep(0.5)


f1 = gevent.spawn(f11)
f2 = gevent.spawn(f22)
# f3 = gevent.spawn(f33)
print('开始')
f1.join()
print('---')
gevent.sleep(0.001)
print('---')
