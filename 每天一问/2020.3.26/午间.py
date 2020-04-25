
class A(object):
    user = 'liuliang'


a = A()

dcitt = {a.user: 'liul'}
print(dcitt.get(a.user))
print(a.user)

