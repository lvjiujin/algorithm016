'''
Author: your name
Date: 2020-09-24 12:06:33
LastEditTime: 2020-09-25 22:19:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Week_03\52.n皇后-ii.py
'''
#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
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
        # print the N-queen checkerboard：
         # print("result = ", result )
        # output =  [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
        # for x in output:
        #     print("[" + ',\n'.join(x)+ ']')
        #     print("\n")
          
        return len(result)
# @lc code=end

