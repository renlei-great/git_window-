
def wer(a):
    def werapp(func):
        def app(*args, **kwargs):
            print('新加点功能呗')
            print('我是装饰器的a:',a)
            return func(*args, **kwargs)
        return app
    return werapp


@wer(12)
def a(a,b):
    print('我是个旧功能')
    print('a', a, '\nb', b)

a(1,2)

#
#
# def werapp(func):
#     def app(*args, **kwargs):
#         print('新加点功能呗')
#         return func(*args, **kwargs)
#     return app
#
#
#
# @werapp
# def a(a,b):
#     print('我是个旧功能')
#     print('a', a, '\nb', b)
#
# a(1,2)