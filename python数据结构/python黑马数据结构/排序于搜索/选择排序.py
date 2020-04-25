lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]

# 选择排序
# 每次都将最小的选出来然后放到前面
# 选择排序的稳定性是不稳定的，因为如果是判断最大，再出现都比他小的时候，那么就会将相同的元素进行颠倒
# 没有最优时间负责度，都是O(n^2)
def sort_xz(lista):
    n = len(lista)
    # min_index = 0
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if lista[min_index] > lista[j]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

sort_xz(lista)
print(lista)
