class singleton(object):
    def __init__(self, cls):
        self.cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self.cls not in self._instance:
            self._instance[self.cls] = self.cls(*args, **kwargs)
        return self._instance[self.cls]


@singleton
class A():
    def __init__(self, a):
        print('init被调用')
        self.a = a

class B(object):
    _instance = {}
    _flag = None
    def __new__(cls, *args, **kwargs):

        if cls not in cls._instance:
            self = object.__new__(cls)
            cls._instance[cls] = self
            cls._flag = True
        return cls._instance[cls]

    def __init__(self, a):
        print('init 被调用')
        if not self._flag:
            self.a = a



a = B(2)
b = B(22222)
c = B(222222)
print(id(a), id(b), id(c))
print(a.a, b.a, c.a)