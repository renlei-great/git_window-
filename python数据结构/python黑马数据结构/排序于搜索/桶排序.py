lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]

# 桶排序
"""
桶排序就是找出最大值和最小值，在这个区间进行分桶，然后将数组中的数按区间装桶，然后在对每个桶进行排序
"""


def pail_sort(alist):
    """桶排序"""
    n = len(alist)
    min_cur, max_cur = 0, 0
    cur = 1
    # 找出最大
    while cur < n:
        if alist[min_cur] > alist[cur]:
            min_cur = cur
        cur += 1
    cur = 1
    # 找出最小
    while cur < n:
        if alist[max_cur] < alist[cur]:
            max_cur = cur
        cur += 1
    min_number, max_number = alist[min_cur], alist[max_cur]

    # 初始化桶，和桶的区间，分出3个桶
    for i in range(1,4):
        number_name = 'number' + str(i)
        pail_name = 'pail' + str(i)
        number = max_number // i
        setattr(pail_sort, pail_name, [])
        setattr(pail_sort, number_name, number)

    # 往桶里封装
    for i in alist:
        if i <= getattr(pail_sort, 'number1') and i > getattr(pail_sort, 'number2'):
            pail_sort.__dict__['pail1'].append(i)
        elif i < getattr(pail_sort, 'number2') and i > getattr(pail_sort, 'number3'):
            pail_sort.__dict__['pail2'].append(i)
        elif i < getattr(pail_sort, 'number3'):
            pail_sort.__dict__['pail3'].append(i)

    # 对每个桶进行排序后拼接返回
    sort_pail = []
    for i in range(3,0, -1):
        sort_pail += marge_sort(pail_sort.__dict__['pail' + str(i)])
    return sort_pail


def marge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    left_li = marge_sort(alist[:mid])
    right_li = marge_sort(alist[mid:])
    left_cur, right_cur = 0, 0
    result = []

    while left_cur < len(left_li) and right_cur < len(right_li):
        if left_li[left_cur] < right_li[right_cur]:
            result.append(left_li[left_cur])
            left_cur += 1
        elif left_li[left_cur] > right_li[right_cur]:
            result.append(right_li[right_cur])
            right_cur += 1
        elif left_li[left_cur] == right_li[right_cur]:
            result.append(left_li[left_cur])
            left_cur += 1
            result.append(right_li[right_cur])
            right_cur += 1

    result += left_li[left_cur:] + right_li[right_cur:]

    return result


if __name__ == "__main__":
    new_li = pail_sort(lista)
    # new_li = marge_sort(lista)
    print(new_li)
