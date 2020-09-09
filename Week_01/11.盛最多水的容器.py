#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法，每次移动较短边.
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            area = min(height[i], height[j])*(j-i)
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return max_area
# @lc code=end


