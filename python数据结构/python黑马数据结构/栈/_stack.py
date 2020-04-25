class Stack(object):
    """创建一个新的空栈"""
    def __init__(self):
        self._list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self._list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        self._list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self._list:
            return self._list[-1]
        return None

    def is_empty(self):
        """判断栈是否为空"""
        return not self._list

    def size(self):
        """返回栈的元素个数"""
        return len(self._list)


if __name__ == "__main__":

    stack = Stack()
    stack.push(1)
    print(stack.size())
