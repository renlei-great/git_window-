
class A:
    a = 1
    def __init__(self, name):
        self.aa = name
        self.bb = 2


class B(A):
    # def __init__(self):
    def __init__(self,name):
        super().__init__(name)


b = B('name')
print(b.aa)