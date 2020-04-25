# 斐波那契数列就是起始是0,1 后一项是前两项的和


def fbnq():
    i = 0
    j = 1
    while True:
        yield i
        i, j = j, i + j


"""
jj = fbnq()
for i in range(5):
    if i % 10 == 0:
        print()
    print(next(jj), end=',')

def Fibonacci(self, n):
    # write code here
    a = 0
    b = 1
    rel = 0
    if n < 1:
        return n
    for i in range(n - 1):
        rel = a + b
        a = b
        b = rel
        self.f.append(rel)
    return rel

"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a

s = Solution()
a = s.Fibonacci(5)
print(a)


class Solution:
    def Fibonacci(self, n):
        # write code here
        i = 0
        j = 1
        for ii in range(n):
            i, j = j, i + j
        return i
