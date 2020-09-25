#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 方法一：dp
        # 状态方程：dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # 问题，如何打印这个最小路径呢？

        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # print("dp = ",dp)
        return dp[rows - 1][columns - 1]

        # 下面这种写法更简练些：
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        array=[grid[0][0]]
        for i in range(1,n):
            array.append(grid[0][i]+array[i-1])
        for i in range(1,m):
            for j in range(n):
                if j ==0:
                    array[j]+=grid[i][j]
                else:
                    array[j] = min(array[j],array[j-1]) + grid[i][j]
        return array[-1]
        # 一个更开阔思路的写法：后续过遍数的消化吸收，暂时放这里。
        # https://leetcode.com/problems/minimum-path-sum/discuss/856314/sequential-thoughtrecursionmemodpfastereasy-understanding
        # 递归写的很简练：
        def minCost(cost, m, n):
            if n <0 or m <0:
                return 0
            elif m == 0 and n == 0:
                return cost[m][n]
            return cost[m][n] + min(minCost(cost, m-1,n),minCost(cost,m,n-1))
        
        M, N = len(grid), len(grid[0])
        return minCost(grid, M-1, N-1)
        

# @lc code=end

