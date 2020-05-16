from python数据结构.尚硅谷数据结构.栈.用栈实现加减乘除.stack import Stack


def poland(str):
    alist = str.split(' ')
    stack = Stack()

    for i in alist:
        try:
            int_a = int(i)
            stack.push(int_a)
        except ValueError:
            n_num = stack.pop()
            p_num = stack.pop()
            num = stack.compute(n_num=n_num, p_num=p_num, oper=i)
            stack.push(num)
    print(stack.pop())


if __name__ == "__main__":
    stra = '4 5 + 5 * 6 -'
    # stra = '30 4 + 5 * 6 -'
    poland(stra)