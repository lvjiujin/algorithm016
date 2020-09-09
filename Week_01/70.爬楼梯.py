#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n -1) + f(n-2)
        f0, f1 = 0, 1
        i = 0 
        f2 = 0
        while i < n:
            f2 = f0 + f1
            f0 = f1
            f1 = f2
            i+=1
        
        return f2
        # 矩阵快速幂的方法，时间复杂度为logn.
        # def multiply(a, b):
        #     c = [[0, 0], [0, 0]]
        #     for i in range(2):
        #         for j in range(2):
        #             c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        #     return c

        # def matrix_pow(a, n):
        #     # res的初始值为单位阵
        #     ret = [[1, 0], [0, 1]]
        #     while n > 0:
        #         if n & 1 == 1:
        #             ret = multiply(ret, a)
        #         n >>= 1
        #         a = multiply(a, a)
        #     return ret

        # M = [[1, 1], [1, 0]]
        # res = matrix_pow(M, n)
        # # print("res = ", res)
        
        # return res[0][0]
        
# @lc code=end

