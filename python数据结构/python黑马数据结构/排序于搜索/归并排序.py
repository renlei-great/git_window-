lista = [12, 4, 5, 6, 22, 3, 895, 990, 43, 654, 765, 7, 234]

# 归并排序
"""
归并排序同样是进行二分，一直往下分，分到只有一个元素，然后进行合并，合并时，两个集合每个元素进行比较
将最小的元素拿出来放到一个新的容器对象中，然后进行返回

考虑的问题：
    1.递归结束的条件是什么
    2.返回值是什么
    3.当循环结束需要考虑什么
"""

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n == 1:
        return alist
    mid = n // 2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    left_cur, right_cur = 0, 0
    result = []
    while left_cur < len(left_li) and right_cur < len(right_li):
        if left_li[left_cur] < right_li[right_cur]:
            result.append(left_li[left_cur])
            left_cur += 1
        elif left_li[left_cur] > right_li[right_cur]:
            result.append(right_li[right_cur])
            right_cur += 1
        else:
            result.append(left_li[left_cur])
            result.append(right_li[right_cur])
            left_cur += 1
            right_cur += 1
    # todo: 循环结束后的考虑
    result += left_li[left_cur:] + right_li[right_cur:]

    return result


if __name__ == "__main__":
    print(lista)
    new_li = merge_sort(lista)
    print(new_li)
    print(lista)

