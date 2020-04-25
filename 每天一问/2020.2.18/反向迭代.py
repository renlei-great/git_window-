
a = [1,2,3,4,4]
list_a = []
def func(n):
    print("函数内部打印{}".format(n))
    list_a.insert(0,n)
    return n

a1 = filter(func, a)
strr = "123"
set(a1)
print(list_a)
print("第一次打印list_a{}".format(list_a))
print("打印a1{}".format(a1))
print("第二次打印list_a{}".format(list_a))






# print(type(a1))


# for i in aa[::-1]:
#     print(i)