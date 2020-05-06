class Solution:
    def Fibonacci(self, n):
        # write code here
        i = 0
        j = 1
        for ii in range(n):
            i, j = j, i + j
        return i



sol = Solution()
print(sol.Fibonacci(-66))