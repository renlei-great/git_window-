l1 = [1,2,3]
l2 = [4,5,6]

# li = l1 + l2
l1.extend(l2)
print('extend:',l1)

l1 = [1,2,3]
l2 = [4,5,6]
l1.append(l2)
# print('extend:',l1)
print('append:',l1)
# print('+:',li)

class Base():
    pass


class a(Base):
    pass

class b(Base):
    pass


a1 = a()

print(isinstance(a1, Base))