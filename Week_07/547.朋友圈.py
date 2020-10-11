#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    # 和岛屿个数的问题非常相似，不过这里不是上下左右的去递归，而是按行递归了。
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        count, m, n = 0, len(M), len(M[0])
        def dfs_marking(M, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or M[i][j] == 0:
                return
            M[i][j] = 0
            M[0][0] = 0
            for y in range(n):
                if M[i][y] == 1:
                    M[i][y] = 0
                    dfs_marking(M, y, i) 
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    count +=1
                    dfs_marking(M, i, j)

        return count

# @lc code=end

