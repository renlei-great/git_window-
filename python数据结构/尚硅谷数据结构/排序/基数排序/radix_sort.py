lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
import random, time
# lista = [random.randint(0,200) for i in range(80000)]


def radix_sort(alist):
    """基数排序"""

    n = len(alist)

    # 找出最大数
    max_num = 0
    for i in alist:
        if i > max_num:
            max_num = i

    # 定义十个桶
    stack_list = [[] for i in range(10)]

    mid_list = alist

    # 遍历每一位
    # 总共遍历的次数
    for i in range(len(str(max_num))):
        # 定义一个中间数组

        for j in range(n):
            try:
                ra = int(str(mid_list[j])[-1-i])
            except IndexError as e:
                # print(f'报错：此刻的数为：{mid_list[j]}')
                ra = 0
            stack_list[ra].append(mid_list[j])
            # print(f'内{j}次：{stack_list}')

        mid_list = []

        for jj in range(10):
            mid_list.extend(stack_list[jj])

        stack_list = [[] for i in range(10)]

        # print()
        # print(f'外{i}次：{mid_list}')
        # print()
    return mid_list




# radix_sort(lista)