#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 时间复杂度为O(n),space complexity O(n)
        # 方法一：动态规划法：dp (dynamic programming) method
        # if not height or len(height) <3:
        #     return 0
        # m = len(height)
        # left_max, right_max = [0 for _ in range(m)], [0 for _ in range(m)]
        # left_max[0], right_max[m-1] = height[0], height[m-1]
        # rain_water = 0
        # for i in range(1, m):
        #     left_max[i] = max(left_max[i-1], height[i])
        #     j = m - 1 -i
        #     right_max[j] = max(right_max[j+1], height[j])
        
        # for i in range(1, m-1):
        #     rain_water += (min(left_max[i], right_max[i]) - height[i])
        # return rain_water
        # 方法二：双指针法:
        # if not height or len(height) < 3:
        #     return 0
        # i, j = 0, len(height) -1
        # left_max, right_max, result = 0, 0, 0
        # while i < j:
        #     left_max = max(height[i], left_max)
        #     right_max = max(height[j], right_max)
        #     # how much can current position trap depends on the shorter bar (木桶原理)
        #     if left_max < right_max:
        #         result += left_max - height[i]
        #         i+=1
        #     else:
        #         result += right_max - height[j]
        #         j-=1

        # return result
        # 方法三：stack 
        from collections import deque
        # deq 是一个单调递减栈
        """
        总体的原则就是，

        1. 当前高度小于等于栈顶高度，入栈，指针后移。
        2. 当前高度大于栈顶高度，出栈，计算出当前墙和栈顶的墙之间水的多少，然后计算当前的高度和新栈的高度的关系，
            重复第 2 步。直到当前墙的高度不大于栈顶高度或者栈空，然后把当前墙入栈，指针后移。

        """
        deq, rain_water = deque(), 0
        
        for i, v in enumerate(height):
            while len(deq) > 0 and height[deq[-1]] < v:
                bottomHeight = height[deq.pop()]
                if len(deq) == 0:
                    break
                leftUpperIndex = deq[-1]
                heightDiff = min(height[leftUpperIndex], v) - bottomHeight
                width = i - leftUpperIndex - 1
                rain_water += heightDiff * width
                
            deq.append(i)
            
        return rain_water






# @lc code=end

