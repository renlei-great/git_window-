#
class DuiXiang(object):
    def __init__(self):
        self.i = 0

    def __iter__(self):
        print('iter')
        return self

    def __next__(self):
        print('next')
        if self.i > 9:
            self.i = 0
        self.i += 1
        return self.i

#
#
dx = DuiXiang()
# print(type(dx))

for i in dx:
    print(i)
# print(next(dx))
# print(next(dx))
# print(next(dx))
# print(next(dx))
# print(next(dx))
# print(iter(dx))

