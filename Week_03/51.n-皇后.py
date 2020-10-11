#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
        
#这个分块写了，好理解一些。
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output

# @lc code=end

