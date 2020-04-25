import threading

def add(a):
    for i in range(50):

        print("子线程{}：{}".format(a, threading.current_thread().ident))
        print('-------')


t = threading.Thread(target=add, args=(1,))
t1 = threading.Thread(target=add, args=(2,))
t.start()
t1.start()
# t.run()
# t1.start()

# for i in range(5):
print('主线程:{}'.format(threading.current_thread().ident))