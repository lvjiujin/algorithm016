#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 杨辉三角
        # return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
        cur = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        
        return cur[-1]
# @lc code=end

