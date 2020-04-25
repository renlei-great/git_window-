import random

lista = [random.randint(0,10) for i in range(10)]
# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


def insert_sort(alist):
    """
    插入排序
    思想：每次找出最大的插到最前的一个
    :param alist:
    :return:
    """
    n = len(alist)
    for j in range(0, n):
        min_num = j
        for i in range(j+1,n):
            if alist[min_num] > alist[i]:
                min_num = i
        alist[min_num], alist[j] = alist[j], alist[min_num]



if __name__ == "__main__":
    insert_sort(lista)
    print(lista)