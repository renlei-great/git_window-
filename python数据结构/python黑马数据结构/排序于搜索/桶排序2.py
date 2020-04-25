lista = [12, 4, 5, 6, 22, 3, 3, 3, 3, 43, 654, 765, 7, 234]


def pail_sort(alist):
    """桶排序"""
    n = len(alist)
    cur = 0

    while cur < n-1:
        if alist[cur] > alist[cur+1]:
            max_num = alist[cur]
        cur += 1

    max_li = [0] * (max_num +1)

    for i in alist:
        max_li[i] += 1
    print(max_li)
    sort_num = []
    for i in range(len(max_li)):
        if max_li[i] != 0:
            print(i)
            ex = 'sort_num.append(i)\n' * max_li[i]
            print(ex)
            exec(ex)
    return sort_num


if __name__ == "__main__":
    new_li = pail_sort(lista)
    print(new_li)