
class AA:
    print('AA')


class A(AA):
    print('A')


class B(A):
    print('B')


class C(AA):
    print('C')


class D(C):
    print('D')


class E(B,D):
    print('E')


print(E.__mro__)