from python数据结构.尚硅谷数据结构.栈.用栈实现加减乘除.single_link_list import SingleLinkList


class Stack:
    """链表实现栈"""
    def __init__(self, max_len=None):
        if max_len is None:
            self.__max_len = 5
        else:
            self.__max_len = max_len
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

    def peep(self):
        """查看元素"""
        if self.__top == -1:
            print('栈空')
        else:
            return self.__stack.peep()

    def is_empty(self):
        return self.__top == -1

    @staticmethod
    def compute(n_num, p_num, oper):
        ex = {'+': lambda p_num, n_num: p_num + n_num,
              '-': lambda p_num, n_num: p_num - n_num,
              '*': lambda p_num, n_num: p_num * n_num,
              '/': lambda p_num, n_num: p_num / n_num}
        return ex[oper](p_num, n_num)

    @staticmethod
    def index(str_oper):
        """获取符号优先级"""
        index_str = {'+': 1, '-': 1, '*': 2, '/': 2}
        return index_str[str_oper]


if __name__ == "__main__":
    pass
