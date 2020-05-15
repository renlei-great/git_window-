from python数据结构.尚硅谷数据结构.栈.用栈实现加减乘除.stack import Stack

"""重点学习栈的使用，利用栈的后进先出实现对字符串数值的计算"""

# 32+6-5+2
def ex_expression(str_num):
    # 定义两个栈，一个数栈，一个符号栈
    num_stack = Stack()
    oper_stack = Stack()

    tem_str = ''
    # 进行压栈和计算同等优先级的运算符
    for str_i in str_num:
        try:
            # 是数字
            int(str_i)
            tem_str +=str_i
        except ValueError:
            # 不是数字，将上面的数组压入数栈中
            num_stack.push(int(tem_str))
            if oper_stack.is_empty():
                # 如果符号栈为空直接压栈
                oper_stack.push(str_i)
            else:
                # 否则进行判断当前符号和栈中符号谁的优先级高，如果当前高，那么直接压栈
                oper = oper_stack.peep()
                if oper_stack.index(oper) < oper_stack.index(str_i):
                    oper_stack.push(str_i)
                else:  # 优先级低或同等，进行运算
                    oper = oper_stack.pop()
                    num1 = num_stack.pop()
                    num2 = num_stack.pop()
                    num = oper_stack.compute(num1, num2, oper)
                    num_stack.push(int(num))
                    oper_stack.push(str_i)
            tem_str = ''

    num_stack.push(int(tem_str))

    print(oper_stack.show(), '++')
    print(num_stack.show(), '++')

    # 执行栈中剩余数值
    while not oper_stack.is_empty():
        oper = oper_stack.pop()
        num1 = num_stack.pop()
        num2 = num_stack.pop()
        num = oper_stack.compute(num1, num2, oper)
        num_stack.push(int(num))

    return num_stack.pop()


if __name__ == "__main__":
    jg = ex_expression('8-3-2')
    print(jg)


