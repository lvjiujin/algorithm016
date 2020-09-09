#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] !=0:
        #         # 明白了，交换，说明之前nums[j] 的位置就是0元素
        #         nums[j], nums[i] = nums[i], nums[j]
        #         j+=1
 
        # snowball 
        # Russian girl 's snowball's method
        snowball = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowball += 1
            elif snowball > 0:
                nums[i - snowball] = nums[i]
                nums[i] = 0
# @lc code=end

