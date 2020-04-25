# def a():
#     pass
#
# class A():
#     def __repr__(self):
#         return 'my class A'
#
# # print(ascii(a))
# a = A()
# aa = ascii(a)
# print(aa)
# print(a)
#
# # print(bin(8.1))
#
# print(bool('a'))
#
# a = dict(a=1,b=2)
# print(a, type(a))
# # print(dir(a))
# class A():
#     def __init__(self):
#         pass
#
#     def __getitem__(self, item):

# def a(*args, **kwargs):
#     a,b = args
#     print(a,b)
#
# a(1,2)

# class A():
#     name = '老王'
#
#     def __init__(self, ls):
#         self.age = 22
#         self.lis = ls

    # def keys(self):
    #     return ("name", "age")
    #
    # def __getitem__(self, item):
    #     print("item", item)
    #     return getattr(self,item)

# a = A([1,2,3])
# print(a['name'])
# dict(a.keys())
# print(a.keys())
# print(a.__dict__)

x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""


def func():
    y = 20
    eval(expr)
    # exec(expr, {'x': 1, 'y': 2})
    # exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})


func()
