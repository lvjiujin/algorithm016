#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor exercise
        if not nums:
            return None
        res = 0
        for num in nums:
            res^= num
        return res

# @lc code=end

