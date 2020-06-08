alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
# import random, time
# alist = [random.randint(0,200) for i in range(80000)]


def merge_sort(alist):
    """归并排序"""

    n = len(alist)
    mid = n // 2

    # 如果只剩一个元素那么进行返回
    if n == 1:
        return alist

    l_list = merge_sort(alist[0: mid])
    r_list = merge_sort(alist[mid: n])

    l_cur = 0
    r_cur = 0
    tmpe_list = []

    while l_cur != len(l_list) and r_cur != len(r_list):

        if l_list[l_cur] <= r_list[r_cur]:
            tmpe_list.append(l_list[l_cur])
            l_cur += 1
        else:
            tmpe_list.append(r_list[r_cur])
            r_cur += 1

    if r_cur == len(r_list):
        for li in l_list[l_cur:]:
            tmpe_list.append(li)
    else:
        for li in r_list[r_cur:]:
            tmpe_list.append(li)

    return tmpe_list


aalist = merge_sort(alist)
print(aalist)



# while l_cur < len(l_list) and l_list[l_cur] > r_list[r_cur]:
#     l_list[l_cur], r_list[r_cur] = r_list[r_cur], l_list[l_cur]
#     l_cur += 1
#
# if l_cur == len(l_list):
#     break
#
# while r_cur < len(r_list) and l_list[l_cur] < r_list[r_cur]:
#     l_list[l_cur], r_list[r_cur] = r_list[r_cur], l_list[l_cur]
#     r_cur += 1