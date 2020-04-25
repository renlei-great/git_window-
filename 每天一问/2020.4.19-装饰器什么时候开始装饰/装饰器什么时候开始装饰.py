def work(func):
    print('进行装饰')
    def app():
        print('装饰功能')
    return app


@work
def f():
    print('被装饰函数')