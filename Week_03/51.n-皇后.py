#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        # 给一个国际站的优秀链接：
        # https://leetcode.com/problems/n-queens/discuss/19808/Accepted-4ms-c%2B%2B-solution-use-backtracking-and-bitmask-easy-understand
        每个皇后必须位于不同行和不同列，因此将 N个皇后放置在N×N 的棋盘上，一定是每一行有且仅有一个皇后，每一列有且仅有一个皇后，
        且任何两个皇后都不能在同一条斜线上。基于上述发现，可以通过回溯的方式寻找可能的解
        """
        # 基于集合的回溯
        # def generateBoard():
        #     board = list()
        #     for i in range(n):
        #         row[queens[i]] = "Q"
        #         board.append("".join(row))
        #         row[queens[i]] = "."
        #     return board

        # def backtrack(row: int):
        #     if row == n:
        #         board = generateBoard()
        #         solutions.append(board)
        #         return 
            
        #     for i in range(n):
        #         # 排除不合法选择
        #         if i in columns or row - i in diagonal1 or row + i in diagonal2:
        #             continue
        #         queens[row] = i
        #         # 做选择
        #         columns.add(i)
        #         diagonal1.add(row - i)
        #         diagonal2.add(row + i)
        #         # 进入下一行决策
        #         backtrack(row + 1)
        #         # 撤销选择
        #         columns.remove(i)
        #         diagonal1.remove(row - i)
        #         diagonal2.remove(row + i)
                    
        # solutions = list()
        # queens = [-1] * n
        # columns = set()
        # # 主对角线
        # diagonal1 = set()
        # # 副对角线
        # diagonal2 = set()
        # row = ["."] * n
        # backtrack(0)
        # return solutions
        # 下面这种方法特别简洁 (比较好)
        # https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
        '''
        In this problem, whenever a location (x, y) is occupied, any other locations (p, q ) 
        where p + q == x + y or p - q == x - y would be invalid. 
        We can use this information to keep track of the indicators (xy_dif and xy_sum ) of the invalid positions 
        and then call DFS recursively with valid positions only.
        '''
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens) # p is the index of row
            if p == n:
                result.append(queens)
                return None
            for q in range(n): # q is the index of col 
                # queens stores those used cols, for example, [0,2,4,1] means these cols have been used
                # xy_dif is the diagonal 1 main diagonal
                # xy_sum is the diagonal 2  counter diagonal/antidiagonal
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        
        DFS([], [], [])
        # print("result = ", result )
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]

        #　another method
        # def backtrace(queue, xset, pset, sset, ans, mid):
        #     y = len(queue) # row index
        #     if y == n:
        #         ans.append(queue)
        #         return
        #     # reduce the max column index of the first row
        #     num = mid if y == 0 else n
        #     for x in range(num): # column index
        #         # y + x = b, y - x = b
        #         plus, sub = y + x, y - x
        #         if x not in xset and plus not in pset and sub not in sset:
        #             # use new set makes the code much more simple but cause more space
        #             backtrace(queue + [x], xset.union([x]), pset.union([plus]), sset.union([sub]), ans, mid)
        # ans, res = [], []
        # mid = n // 2 if n % 2 == 0 else n // 2 + 1
        # backtrace([], set(), set(), set(), ans, mid)
        # for item in ans:
        #     res.append(["."*x + "Q" + "."*(n-1-x) for x in item])
        #     if item[0] != n-1-item[0]:
        #         res.append(["."*(n-1-x) + "Q" + "."*x for x in item])
        # return res


        # 下面这个写的很简洁，但是效率太低了,beats 5%
        # def dfs(r):
        #     if r == n:
        #         res.append([''.join(row) for row in b])
        #         return
        #     for c in range(n):
        #         if isValid(r, c):
        #             b[r][c] = 'Q'
        #             dfs(r + 1)      # fill row by row
        #             b[r][c] = '.'
        
        # def isValid(r, c):
        #     for i in range(r):
        #         for j in range(n):
        #             if b[i][j] == 'Q' and (c == j or        # same column
        #                                    i+j == r+c or    # 45 degree line
        #                                    i-j == r-c):     # 135 degree line
        #                 return False
        #     return True
                        
        
        # b = [['.'] * n for _ in range(n)]
        # res = []
        # dfs(0)      # start from row 0
        # return res


        # 方法二：基于位运算的回溯
    
        # def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
        #     if row == n:
        #         board = generateBoard()
        #         res.append(board)
        #     else:
        #         availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
        #         while availablePositions:
        #             position = availablePositions & (-availablePositions)
        #             availablePositions = availablePositions & (availablePositions - 1)
        #             column = bin(position - 1).count("1")
        #             queens[row] = column
        #             solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)

        # res = list()
        # queens = [-1] * n
        # row = ["."] * n
        # solve(0, 0, 0, 0)
        # return res

# @lc code=end

