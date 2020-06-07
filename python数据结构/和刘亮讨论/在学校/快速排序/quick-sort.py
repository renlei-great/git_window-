# alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
import random, time
alist = [random.randint(0,200) for i in range(80000)]

def quick_sort(alist, start, end):
    """快速排序"""

    if end - start <= 1:
        return

    l_cur = start
    r_cur = end
    mid = alist[start]

    while r_cur > l_cur:
        # 判断右边
        while alist[r_cur] >= mid and r_cur > l_cur:
            r_cur -= 1
        alist[l_cur], alist[r_cur] = alist[r_cur], alist[l_cur]

        # 判断左边
        while alist[l_cur] < mid and r_cur > l_cur:
            l_cur += 1
        alist[r_cur], alist[l_cur] = alist[l_cur], alist[r_cur]

    alist[l_cur] = mid

    quick_sort(alist, start, l_cur-1)
    quick_sort(alist, l_cur+1, end)


if __name__ == "__main__":
    # n = len(alist)
    # quick_sort(alist, 0, n-1)
    # print(alist)

    n = len(alist)
    time_start = time.time()
    # print(lista)
    quick_sort(alist, 0, n-1)
    # print(lista)
    end_time = time.time()
    time_z = end_time - time_start
    print('总耗时：', end=' ')
    print(time_z)

