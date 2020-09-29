#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >>1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # 注意，这里不能写成right = mid
                # 因为有这样的场景：3,3, 1,3 
                right -=1
            
        return nums[left]
# @lc code=end

