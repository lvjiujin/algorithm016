#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        # n & 1获取的是最右边的最低位。
        while n:
            ret += (n & 1) << power
            power -=1
            n>>=1
        return ret 
        
# @lc code=end

