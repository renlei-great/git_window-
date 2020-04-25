
# try:
#     pass
# except Exception:
#     pass
# else:
#     # raise ValueError('JJJ')
#     pass
# finally:
#     pass
#
# def func(a):
#     int(a)
#     print(a)
# int('a')
# func('a')

# class wi(object):
#     def run(self):
#         print('d打开文件')
#         raise ValueError('123')
#
#
#     def __enter__(self):
#         print('enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exc_type:',exc_type, '\n exc_val:', exc_val, '\nexc_tb:',exc_tb)
#         print('exit')
#
# ww = wi()
#
# with ww as w:
#     w.run()

import contextlib


@contextlib.contextmanager
def wi():
    print('类似enter功能')
    # raise ValueError()
    yield 1
    print('打开文件')
    print('类似exit功能')


# w = wi()

with wi() as w:
    print(type(w))



# a +=1
# print(a)