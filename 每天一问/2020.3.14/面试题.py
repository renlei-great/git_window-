# def gener():
#     for i in range(3):
#         yield i
#
#
# g = gener()
# print(next(g))
# print(next(g))
# print(next(g))

# foo=[-5,8,0,4,9,-4,-20,-2,8,2,-4]
# a = lambda a: (a,2)
# print(a(1))
# sorted()
# print(foo)
#
# def lam(x):
#     return x
#
#
# class A:
#     def __call__(self, *args, **kwargs):
#         return 2
# a = A()
# print(A())
# print(a())
# l = lam(2)
# print(type(lam))
# print(type(l))
# print(type(A()))

# example_list = [5, 0, 6, 1, 2, 7, 3, 4]
# result_list = sorted(example_list, key=lambda x: (x < 3, abs(x)))
# print(result_list)
#
#
# k =lambda x: (x < 3, abs(x))
#
# print(type(k))
#
#
# print(k(3))
#
def lam1(x):
    # return (x< 2, -x)
    print(x)
    return -x

def lam2(x):
    # return (x< 2, -x)
    print(x)
    return x<0, x

foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
# a = sorted(foo, key=lambda x: (x < 2, -x))
a = sorted(foo, key=lam1)
print(a)
b = sorted(foo, key=lam2)
print(b)

#
# def sort_test(list_test, func):
#     a = func(list_test[0])
#     list_pra = []
#     list_tow_pra1 = []
#     list_tow_pra2 = []
#     try:
#         a[0]
#         # 参数有两个
#         for i in list_test:
#             pra = func(i)
#             list_pra.append(pra)
#
#             # 判断返回参数中是否有x
#             pra = set(list_pra)
#             if len(pra) == 1:
#                 return list_test
#
#     except TypeError:
#         # 参数只有一个
#         for i in list_test:
#             pra = func(i)
#             list_pra.append(pra)
#
#         # 判断返回参数中是否有x
#         pra = set(list_pra)
#         if len(pra) == 1:
#             return list_test
#
#         index_i = 0
#         for i in list_test:
#             if i > 0:
#                 if list_pra[index_i] == i:
#                     list_test.sort(reverse=True)
#                     a1 = True
#             if i < 0:
#                 if list_pra[index_i] != i:
#                     list_test.sort(reverse=True)
#                     a2 = True
#             list_if = []
#             if a1 == a2:
#                 for i in list_test:
#                     list_if.append(abs(i))
#
#
#         # 判断是升序还是降序
#         for i in list_test:
#             if i > 0:
#                 if list_pra[index_i] != i:
#                     list_test.sort(reverse=True)
#                     pass
#                     return list_test
#                 list_test.sort(reverse=False)
#                 pass
#                 return list_test
#
#
#
#
# def lam1(x):
#     # return (x< 2, -x)
#     print(x)
#     return x
#
# a = sort_test([1,2,-6,9,-4,5], func=lam1)
# print(a)
























