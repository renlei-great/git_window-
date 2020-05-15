
# def aa(i):
#     print(i)
#
# di = {'aa': aa}
#
# ex = input('输入')
#
# di[ex](3)

# a = '123'
# for i in a:
#     print(i)
#
# b = +
# print(type)
# a = 1 + 2

class A:

    @staticmethod
    def a():
        print(1)

aa = A()
aa.a()

a = [1,2,3]
if 2 in a:
    print(True)

def compute(n_num, p_num, oper):
    ex = {'+': lambda p_num, n_num: p_num + n_num,
          '-': lambda p_num, n_num: p_num - n_num,
          '*': lambda p_num, n_num: p_num * n_num,
          '/': lambda p_num, n_num: p_num / n_num}
    return ex[oper](p_num, n_num)

a = compute(1,2, '+')
print(a)