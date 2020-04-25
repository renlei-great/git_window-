import datetime, time
# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
lista = [1,2,3,4,5,6,7,8,9,9,9,9,9,9,9]

# 冒泡每次都是两两相比，选出最大的进行替换，那么最终最大的一定在最后
# 稳定性：是稳定的，遇到相同的元素不会进行颠倒
# 有最优时间负责度

def bubble_sort(lista):
    n = len(lista)
    sign = True
    for i in range(1, n):
        for j in range(n-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                sign = False
        if sign:
            return
        else:
            sign = True


if __name__ == "__main__":
    start_time = time.time()
    for i in range(1000):
        bubble_sort(lista)
    end_time = time.time()
    print(lista)
    print(end_time-start_time)