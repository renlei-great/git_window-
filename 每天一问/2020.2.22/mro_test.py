
class A:
    print('A')


class B(A):
    print('B')


class C(A):
    print('C')


class D(C,B):
    print('D')


print(D.__mro__)