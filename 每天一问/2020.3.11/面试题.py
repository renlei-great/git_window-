# 一行代码对1-55求和
# a = sum(range(1,56))
# print(a)
#
# b = pow(1, 56)
# print(b)

# 在函数内部修改全局变量使用globals

# 可变类型实例
# a = [1, 2, 3]
# print('值：', a, 'id:', id(a))
# a.append(4)
# print('值：', a, 'id:', id(a))

# 不可变类型实例
# a = "1,2,3"
# print('值：', a, 'id:', id(a), '类型',type(a))
# a += '4'
# print('值：', a, 'id:', id(a), '类型',type(a))
# print(a.__dir__())

# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort()
print(s)







