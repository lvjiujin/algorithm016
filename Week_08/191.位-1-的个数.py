#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res +=1
            n = n&(n-1)

        return res
        # return bin(n).count('1')
# @lc code=end

