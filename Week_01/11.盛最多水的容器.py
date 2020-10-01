#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法，每次移动较短边.
        """
        感觉这个移动有点博弈论的味了，每次都移动自己最差的一边，虽然可能变得更差，但是总比不动（或者减小）强，
        动最差的部分可能找到更好的结果，但是动另一边总会更差或者不变，兄弟们，这不是题，这是人生，逃离舒适圈！！
        先考虑把前人的智慧学到家，然后再考虑自己的思路。（得先读够了paper，才有能力做科研创新）
        """
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


