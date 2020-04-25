# import re
#
# s = "<a>哈哈</a>jhgf<a>呵呵</a>"
#
# rest1 = re.match(r"<a>(.*)</a>", s)
# print(rest1.group(1))
#
# def func(a):
#     b = a
#     print(id(b))
#
# aa = [1,2,3]
# print(id(aa))
# func(aa)
#
# def func(new_data, list_t=[]):
#     list_t.append(new_data)
#     return list_t
#
# print(func(1))
# print(func(2))
# list_w = [1,2]
# list_w1 = func('a', list_w)
# print(list_w1)
# print(list_w)
# list_w2 = ['a','b']
# list_w22 = func(1, list_w2)
# print(list_w2)
# print(list_w22)
# print('----')
# print(list_w1)
# print(list_w)
#



list_test = [j for i in [[1,2], [3,4], [5,6]] for j in i ]
print(list_test)