lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]

def shell_sort(alist):
    """希尔排序
    思想：就是将一个无序序列进行分类分层去进行插入排序,最外层循环控制步长，
    步长那个数比作要插入排序的第一个数，然后执行插入排序
    """

    n = len(alist)
    seep = n // 2

    while seep >= 1:
        for gep in range(seep, n):
            while gep - seep >= 0:
                if alist[gep] > alist[gep - seep]:
                    gep -= seep
                    break
                alist[gep], alist[gep - seep] = alist[gep - seep], alist[gep]
        seep //= 2

shell_sort(lista)
print(lista)