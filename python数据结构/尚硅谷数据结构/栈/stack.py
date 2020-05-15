from python数据结构.python黑马数据结构.链表.single_link_list import SingleLinkList


class Stack:
    """链表实现栈"""
    def __init__(self, max_len=None):
        if max_len is None:
            self.__max_len = 5
        self.__max_len = 5
        self.__top = -1
        self.__stack = SingleLinkList()

    def show(self):
        """显示栈"""
        if self.__top == -1:
            print('栈中没有数据')
        else:
            self.__stack.travel()

    def push(self, item):
        """压入元素"""
        if self.__top == self.__max_len:
            print('栈满')
        else:
            self.__stack.add(item)
            self.__top += 1

    def pop(self):
        """弹出元素"""
        if self.__top == -1:
            print('栈空')
        else:
            # print(self.__stack.pop())
            self.__top -= 1
            return self.__stack.pop()

    def is_empty(self):
        return self.__top == -1

def exit_i():
    """退出功能"""
    raise TypeError('')


def ex_stack(stack):
    """执行操作"""
    exe_dict = {'show': stack.show, 'push': stack.push, 'pop': stack.pop, 'exit': exit_i}
    try:
        while True:
            print(f'show 显示栈情况')
            print(f'push 压栈')
            print(f'pop 出栈')
            print(f'exit 退出')
            key = input('请输入：')
            if key == 'push':
                data = input('请输入压栈的数据')
                exe_dict[key](data)
            else:
                exe_dict[key]()
    except TypeError as e:
        print(e)
        print('程序退出')
    except KeyError:
        print('输入有误,重新输入')
        ex_stack(stack)


if __name__ == "__main__":
    stack = Stack()
    ex_stack(stack)
