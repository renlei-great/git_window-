
class Stack():
    def __init__(self):
        self.__stack = list()
    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        self.__stack.pop()

    def size(self):
        print(len(self.__stack))

    def empty(self):
        return not self.__stack

    def __str__(self):
        # for i in self.__stack:
        #     print(i)
        try:
            print(self.__stack)
        except TypeError:
            pass
        return "ok"

    # def __repr__(self):
    #     print(self.__stack)
    #
    # __str__ = __repr__

if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    # s.pop()
    s.pop()
    s.size()
    print(s)
    print(s.empty())




