
class A:
    age = 1
    def __init__(self, name, cla):
        self.name = name
        self.cla = cla


    def run(self):
        print('11')

    def __getitem__(self, item):
        print('item', item)
        return item

    def __getitem__(self, item):
        return self.__dict__[item]



aa = A('renlei', '专升本')
# aa.__class__.age=2
# print(A.age)
# print(dict(aa))
# aa['nn'] = 1
# aa['2'] = 2
# print(aa[0:])
# print(aa.name)
# print(aa['name'])
print(aa.__dict__)
print(A.__dict__)
# print(dict(aa))
# for i in aa:
#     print(i)