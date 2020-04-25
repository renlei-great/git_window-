# from test import *
# import test
# from test import aa
# print(aa)
# print(test.aa)
# aa = 0

# # def a():
# #     # aa = 1
# #     def b():
# #         # aa = 2
# #         def c():
# #             # aa = 3
# #             print(aa)
# #         return c()
# #     return b()
#
# def a1():
#     a = 1
#
# def b():
#     print(a)
#
#
# b()
# x = 1
#
# def f():
#     x = 3
#     g()
#     print('f',x)
#
# def g():
#     print('g', x)
#
# f()
# print(x)

# import builtins
# print(dir(builtins))
#
# def str():
#     print(1)
#
# a = 123
# b = str(a)
# print(b)

# x = 1
# def g():
#     global x = 3
#     print(x)
#     # x=3
# g()


# def f1():
#     list1 = []
#     for i in range(5):
#         def n(x):
#             return i+x
#         list1.append(n)
#     return list1
#
# mylist = f1()
# for i in mylist: print(id(i))
# print(mylist[0](2))
# print(mylist[2](2))
# print(mylist[3](2))
# print(mylist[4](2))

#
# def f1():
#     for i in range(5):
#         def n():
#             print(i)
#         n()
#     return n
#
# f1()()
#
# a = [];b = []
# print(a is b)



