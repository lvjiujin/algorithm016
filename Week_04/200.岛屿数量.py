#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count, m, n = 0, len(grid), len(grid[0])
        def dfs_marking(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            grid[0][0] = '0'
            dfs_marking(grid, i+1, j)
            dfs_marking(grid, i-1, j)
            dfs_marking(grid, i, j-1)
            dfs_marking(grid, i, j+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count +=1
                    dfs_marking(grid, i, j)
        
        return count 
        
# @lc code=end

