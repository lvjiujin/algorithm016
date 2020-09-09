#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = dict()
        for i, x in enumerate(nums):
            other = target - x
            if other in d1:
                return [d1[other], i]
            else:
                d1[x] = i
        # 如果找不到如何处理？到底该怎么返回？
        # 返回一个空list，还是返回两个相等的负值。
        return [-1, -1]
# @lc code=end
        
