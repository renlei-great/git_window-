from python数据结构.尚硅谷数据结构.栈.用栈实现加减乘除.stack import Stack


def infix_to_sufix(str_a: str):
    """中缀转后缀"""
    oper_stack = Stack(20)
    num_stack = Stack(20)
    list_a = str_a.split(' ')
    for a in list_a:
        try:
            # 判断是否为数字
            a = int(a)
            num_stack.push(a)
        except ValueError:
            # 为符号
            if a == '(':
                oper_stack.push(a)
            elif a == ')':
                while True:
                    # 弹出栈中左括号前的符号到num_stack中
                    oper = oper_stack.pop()
                    if oper == '(':
                        break
                    num_stack.push(oper)
            else:
                # 运算符
                if oper_stack.is_empty():
                    # 如果栈空，直接添加
                    oper_stack.push(a)
                else:
                    oper = oper_stack.peep()
                    if oper == '(':
                        oper_stack.push(a)
                    elif oper_stack.index(a) > oper_stack.index(oper):
                        # 优先级比栈中元素大
                        oper_stack.push(a)
                    else:
                        # 如果比栈中优先级小或相等，那么弹出栈中运算符到num_stack栈中
                        # 然后进行添加
                        oper = oper_stack.pop()
                        num_stack.push(oper)
                        oper_stack.push(a)


    while not oper_stack.is_empty():
        # 将oper_stack中剩余的符号添加到num_stack中
        oper = oper_stack.pop()
        num_stack.push(oper)

    # 输出栈中数据，组成最后的结果
    str_aa = ''
    while True:
        s = num_stack.pop()
        if s:
            str_aa += str(s) + ' '
        else:
            break

    return str_aa[::-1]

str_a = '1 + ( ( 2 + 3 ) * 4 ) - 5'
in_str = infix_to_sufix(str_a)
print(in_str)

