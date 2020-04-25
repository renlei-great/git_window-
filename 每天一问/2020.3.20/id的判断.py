# tu = (1,2,3)
# tu1 = (1,2,3)
# print(id(tu), id(tu1))
#
# li = {1:1}
# li1 = {1:1}
# print(id(li), id(li1))
#
# st = '12'
# st1 = '12'
# print(id(st), id(st1))

# class Test():
#     def __init__(self,name, list_test = None):
#         if list_test is None:
#             self.list_test = []
#         self.name = name
#         self.list_test.append(self.name)
#
#     def show(self):
#         print(self.list_test)
#         print(id(self.list_test))
#
# t = Test('renlei')
# t1 = Test('liuliang')
# t.show()
# t1.show()


# class Test():
#     def __init__(self, year):
#         self.year = year
#         self._age = None
#
#     @property
#     def age(self):
#         if self._age is None:
#             return 2020 - int(self.year)
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         self._age=value
#
#
# t = Test(1997)
#
# print(t.age)
# class Filed():
#     def __get__(self, instance, owner):
#         return 7
#
#     def __set__(self, instance, value):
#         print('aaaa')
#         self.i = value
#
#     def __delete__(self, instance):
#         print('删除')
#
# class Filed():
#     def __get__(self, instance, owner):
#         return 7
#
#     def __set__(self, instance, value):
#         print('aaaa')
#         self.i = value
#
#     def __delete__(self, instance):
#         print('删除')
#
# class Test():
#     aa = Filed()
#     def __init__(self, info):
#         self.info = info
#         # self.name = 11
#
#     def __getattr__(self, item):
#         return self.info[item]
#
# t = Test({'name': 'rnlei'})
# # print(t.name)
# t.aa = 1
# print(t.aa)
# del t.aa

"""属性描述符"""
# class TestDescriptor3(object):
#     """数据描述符"""
#     def __init__(self):
#         self.temp = '';
#
#     def __get__(self, obj, type = None):
#         print("get is called.")
#         return self.temp + " -> after get"
#
#     def __set__(self, obj, val):
#         print("set is called.")
#         self.temp = val + " -> after set"
#         print(self.temp)
#
# class NotDateTestDescriptor3():
#     """非数据描述符"""
#     def __get__(self, obj, type = None):
#         return "get is called."
#
# class B3(object):
#     ## 把类B的一个属性设置成上面特殊类的对象
#     name = TestDescriptor3()

#
#
# bb = B3()
# # bb.name = 'hah'
# # a = bb.name
# bb.age = 18
# # print(a)
# print(bb.age)
def foo(a):
    print(a)
    def foo1(func):
        def foo11(*args, **kwargs):
            print('新加的功能')
            print(a)
            return func(*args, **kwargs)
        return foo11
    return foo1

@foo(1) #foo(1) ff = foo1(ff)
def ff(a,b):
    a = a
    b = b
    print('我原本就有的功能',a,b)


if __name__ == "__main__":
    ff(1,2)




