#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        upperlim = reduce(lambda x, i: x<<1|1, range(n+1))
        self.helper(res, [-1]*n, upperlim)
        return res

    def helper(self, res, queens, upperlim, ld=0, row=0, rd=0, idx=0):
        n = len(queens)
        if idx == n:
            res += ['.'*j +'Q'+ '.'*(n-j-1) for j in queens],
            return
        pos = upperlim & ~(ld | row | rd)
        while pos:
            p = pos & (~pos + 1)
            pos -= p
            queens[idx] = int(math.log(p, 2))
            self.helper(res, queens, upperlim, (ld+p)<<1, row+p, (rd+p)>>1, idx +1)
# @lc code=end

