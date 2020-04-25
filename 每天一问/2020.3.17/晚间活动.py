
"""举例说明zip函数的用法"""

# a = ('a', 'b', 'c')
# # # b = (1,2,3)
# # #
# # # c = zip(a,b)
# # # print(list(c))

"""正则"""

# import re
#
# a = '张明98分'
# a1 = re.sub('\d+', '100', a)
# print(a1)

# def a():
#     print(1)
#
#
# def a(i):
#     print(i)
#
# a()



"""基础面试题"""

# I = []
# a = {'num': 0}
# for i in range(10):
#     a['num'] = i
#     I.append(a)
#
# print(I)

# for i in range(5,0):
#     print(i, end=' ')

# a = [1,2,3,4,5,6,7,8,9]
# print(a[6:2:-1])



# with open('txt[副本]') as f:
#     # f.writelines('txt')
#     a = ''
#     for text in f.readlines():
#         a += text
# print(a)


# def read_test():
#     with open('txt') as f:
#         while True:
#             yield f.__next__()
#
# r_t = read_test()
#
# for i in range(10):
#     print(read_test)


# def yi():
#     i = 1
#     while True:
#         yield i
#         i += 1
#         if i > 2:
#             return '这样啊 '
#     print(11)
#
#
# def aa():
#     i = 1
#     while True:
#         yield i
#         i += 1
#         if i > 2:
#             return '这样啊 '
#     print(11)


# y = yi()
# yy = yi
# print('yid:{},yiid:{},yyid:{}'.format(id(y), id(yi), id(yy)))
"""
第一种情况：使用函数，不调用函数赋值
第二种：调用函数赋值
第三种：使用yield赋值，调用和不调用
"""
# print(type(yi()))
# print(type(y))
# a = print(next(yi()) , 'id:', id(yi()), type(yi()))
# a = print(next(yi()) , 'id:', id(yi()), type(yi()))
# a = print(next(yi()) , 'id:', id(yi()), type(yi()))
# aa = print(next(aa()) , 'id:', id(aa()), type(aa()))
# print('--------------')
# print(next(y) , 'id:', id(y), type(y))
# print(next(y) , 'id:', id(y), type(y))
# print(next(y) , 'id:', id(y), type(y))



#
#
# with open('txt') as f:
#     # print(next(f))
#     # print(f.__next__())
#     # print(f.__next__())
#     for i in f:
#         print(i)
#         break


def yi():
    i = 1
    while True:
        yield i
        i += 1
        if i > 2:
            return '这样啊 '
    print(11)


def aa():
    i = 1
    while True:
        yield i
        i += 1
        if i > 2:
            return '这样啊 '
    print(11)

def put():
    pass

def put2():
    if 1:
        for i in range(10):
            i

def liul():
    yield 1

# a =yi()
p = put()
pp = put2
pp()
print(id(p))
print(id(pp))

a = print(next(yi()) , 'id:', id(yi()), type(yi()))
a = print(next(yi()) , 'id:', id(yi()), type(yi()))
a = print(next(yi()) , 'id:', id(yi()), type(yi()))
print('-------------------')
aa = print(next(aa()) , 'id:', id(aa()), type(aa()))

aa = print(next(liul()) , 'id:', id(liul()))
aa = print('id:', id(put()))
aa = print('id:', id(put2()))