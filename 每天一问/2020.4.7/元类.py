from collections import namedtuple

User = type('User', (), {'name':1,'age':2})
u = User()
print(u.name, u.age)

