from python数据结构.尚硅谷数据结构.栈.stack import Stack

# 32+6-5+2
def ex_expression(str_num):
    # 定义两个栈，一个数栈，一个符号栈
    num_stack = Stack()
    oper_stack = Stack()

    tem_str = ''
    index_str = {'+': 1, '-': 1, '*': 2, '/': 2}
    # 进行压栈和计算同等优先级的运算符
    for str_i in str_num:
        try:
            int(str_i)
            tem_str +=str_i
        except ValueError:
            num_stack.push(tem_str)
            if oper_stack.is_empty():  # 如果为空直接压栈
                oper_stack.push({'index': index_str[str_i],'val': str_i})
                tem_str = ''
            else:  # 否则进行判断当前符号和栈中符号谁的优先级高，如果当前高，那么直接压栈
                mid = oper_stack.pop()['val']
                if index_str[mid] < index_str[str_i]:
                    oper_stack.push({'index': index_str[mid], 'val': mid})
                    oper_stack.push({'index': index_str[str_i], 'val': str_i})
                    tem_str = ''
                else:  # 优先级低或同等，进行运算
                    n_num = num_stack.pop()
                    p_num = num_stack.pop()
                    num = eval(p_num+mid+n_num)
                    num_stack.push(str(num))
                    oper_stack.push({'index': index_str[str_i],'val': str_i})
                    tem_str = ''
    num_stack.push(tem_str)

    # 执行栈中剩余数值
    while not oper_stack.is_empty():
        n_num = num_stack.pop()
        p_num = num_stack.pop()
        mid = oper_stack.pop()['val']
        num = eval(p_num + mid + n_num)
        num_stack.push(str(num))

    return num_stack.pop()


if __name__ == "__main__":
    jg = ex_expression('32+6*6-363+2*6/2-6*9*9')
    print(jg)


