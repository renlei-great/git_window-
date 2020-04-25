class find():
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


# class A(object):
#     a = 1


class B:
    a = find()
    def __init__(self, a):
        self.a = a

b = B(1)

