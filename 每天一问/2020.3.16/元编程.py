class BaseType(type):
    def __new__(cls, *args, **kwargs):
        print('被调用')
        return super().__new__(cls, *args, **kwargs)


class A(metaclass=BaseType):
    pass


print(A.mro())
print(type(A))
























# ase = BaseType('ase', (), {})
#
#
# class AA(BaseType):
#     pass
#
# aa = AA('aa', (), {})
#
#
# a = A()
#
#
# class Base(object):
#     def __new__(cls, *args, **kwargs):
#         print('base被调用')
#         return super().__new__(cls, *args, **kwargs)
#
#
#
# class B:
#     pass
#
# b = Base()
