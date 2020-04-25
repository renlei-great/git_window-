lista = [12, 4, 4, 5, 6, 22, 22, 3, 43, 654, 765, 7, 234]


def pail_sort(alist):
    """桶排序"""
    n = len(alist)
    max_cur = 0
    max_num = 0
    i = 1

    # 先出最大的元素
    while i < n-1:
        if alist[max_cur] < alist[i]:
            max_cur = i
        i +=1
    max_num = alist[max_cur]

    # 初始化有多谢桶
    max_li = [0] * (max_num+1)

    # 那个桶有元素
    for i in alist:
        max_li[i] +=1

    # 进行排序
    sort_li = []
    for i in range(len(max_li)):
        if max_li[i] != 0:
            ex = 'sort_li.append(i)\n' * max_li[i]
            exec(ex)

    return sort_li


if __name__ == "__main__":
    new_li = pail_sort(lista)
    print(new_li)

