
class A():
    pass


class B(A):
    pass

b = B()

print(issubclass(B, A))
print(isinstance(B, A))
print(isinstance(b, A))