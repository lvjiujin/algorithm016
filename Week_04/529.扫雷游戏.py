#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #八个方向， 上下左右，以及四个对角线
        dire = [
                [-1, 0], [-1, 1], [0, 1], [1, 1], 
                [1, 0], [1, -1], [0, -1], [-1, -1]
            ] 
        
        def search_around(x, y): #看看周围几个雷
            count = 0
            for i, j in dire:
                if 0 <= x + i <= m-1 and 0 <= y + j <= n - 1:
                    if board[x + i][y + j] == 'M':
                        count += 1
            return count

        def dfs(x,y): 
            if x < 0 or x > m - 1 or y < 0 or y > n - 1: #先判断边界
                return 
            if board[x][y] != 'E': #再判断是不是E
                return 
            count = search_around(x,y) #算雷
            if count != 0: #有雷截断，不找了
                board[x][y] = str(count)
                return 
            else:
                board[x][y]='B'
                for i, j in dire:
                    dfs(x+i, y+j)
        
        m, n = len(board), len(board[0])
        if board[click[0]][click[1]] == 'M': #有可能一开始就踩雷
            board[click[0]][click[1]] = 'X'
            return board
        else:
            dfs(click[0], click[1])
            return board
        
# @lc code=end

