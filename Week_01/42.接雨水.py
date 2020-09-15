#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 时间复杂度为O(n),space complexity O(n)
        # dp (dynamic programming) method
        if not height or len(height) <3:
            return 0
        m = len(height)
        left_max, right_max = [0 for _ in range(m)], [0 for _ in range(m)]
        left_max[0], right_max[m-1] = height[0], height[m-1]
        rain_water = 0
        for i in range(1, m):
            left_max[i] = max(left_max[i-1], height[i])
            j = m - 1 -i
            right_max[j] = max(right_max[j+1], height[j])
        
        for i in range(1, m-1):
            rain_water += (min(left_max[i], right_max[i]) - height[i])
        return rain_water
# @lc code=end

