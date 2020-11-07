#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 说明2的幂的数，在2进制的表示中都是最左边是一个1，后面跟一堆0，
        # 充分利用这个特点能够很快得到结果。
        if n <= 0:
            return False
        # return n & (-n)  == n
        return n & (n - 1) == 0
# @lc code=end

