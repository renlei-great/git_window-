# a = [1,2,3]
# # print(dir(a))
# aa= iter(a)
# print(dir(aa))
# print(next(aa))
# print(next(aa))
# print(next(iter(a)))
from collections import UserList

class A:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        print('执行')
        yield 1

    # def __next__(self):
    #     while True:
    #         self.i += 1
    #         return self.i


a = A()
# next(iter(a))
for i in a:
    print(i)
# print(isinstance(A(), Iterator))
# print(type(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# b = iter(a)
# for i in iter(a):
#     print(i)
# print(isinstance(a,aa))
# print(type(a), type(aa))
