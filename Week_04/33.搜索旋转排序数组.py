#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 该方法出自光头哥：
        # https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
        if not nums:
            return None
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >>1
            if nums[mid] == target:
                return mid
            # 先根据num[0] 与target的关系判断目标值是在做半段还是在右半段
            if target >= nums[0]:
                # 目标值在做半段时，若mid在右半段，则将mid的索引的值改为inf.
                if nums[mid] < nums[0]:
                    nums[mid] = float('inf')
            else:
                # 目标值在右半段时，若mid在左半段，则将mid索引的值改为-inf
                if nums[mid] >=nums[0]:
                    nums[mid] = float('-inf')
            
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1

# @lc code=end

