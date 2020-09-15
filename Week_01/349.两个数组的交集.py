#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        x =  set(nums1).intersection(set(nums2))
        return list(x)
# @lc code=end

