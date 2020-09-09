#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        j = 1
        for i in range(len(nums) -1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j+=1
        return j 

        
# @lc code=end

