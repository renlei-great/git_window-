# a = (i for i in range(10))
# print(type(a))
# print(dir(a))


# a = [1,63,35,269,125,364,132,865,725]
# a = [2,1,5,4,10,7, 125,364,132,]
# # a = ['a', 'b', 'v']
# b = set(a)
# b = (1,2,3)
# b[2]
# for i in b:
#     print(i)
#
#
# class A:
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         print(args)
#         print(kwargs)
#     name = 'renlei'
#
# class B(A):
#     pass
#
#
# a = A()
# print(a.name)
# b = A()
# print(a.name, b.name)
# b.__class__.name = 'kk'
#
# print(a.name, b.name)

# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         # print("New")
#         if cls._instance is None:
#             # print("Create")
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     def __init__(self):
#         # print("Initalize")
#         self.prop = 33
#
#     def __enter__(self):
#         # raise ValueError('ssss')
#         # 1/0
#         print(11)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(22)
#         print(exc_tb)
#         print(exc_val)
#         print(exc_type)
#
# s = Singleton()
# print(s.prop)
# with Singleton() as e:
#     print(e.prop)

# s1 = Singleton()
# s2 = Singleton()

from contextlib import contextmanager


@contextmanager
def cont():
    print('start')
    yield 1
    print('exit')

with cont() as e:
    print(e,'---')


from collections import namedtuple

namedtuple()


collect
