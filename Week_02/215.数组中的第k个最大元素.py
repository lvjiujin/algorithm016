#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 排序法：
        if not nums:
            return None
        nums.sort(reverse = True)
        return nums[k-1]

# @lc code=end

