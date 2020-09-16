#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1. brute force ,python can't pass the test .
        # size = len(heights)
        # res = 0

        # for i in range(size):
        #     left = i
        #     cur_height = heights[i]
        #     while left > 0 and heights[left - 1] >= cur_height:
        #         left -= 1

        #     right = i
        #     while right < size - 1 and heights[right + 1] >= cur_height:
        #         right += 1

        #     max_width = right - left + 1
        #     res = max(res, max_width * cur_height)
        # return res
        # 2. monotonous increate stack
        from collections import deque
        deq = deque()
        """
        我们遍历每个柱体，若当前的柱体高度大于等于栈顶柱体的高度，
        就直接将当前柱体入栈，否则若当前的柱体高度小于栈顶柱体的高度，说明当前栈顶柱体找到了右边的第一个小于自身的柱体，
        那么就可以将栈顶柱体出栈来计算以其为高的矩形的面积了。
        
        """
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        deq.append(0)
        size += 2
        #　看到的元素严格小于栈顶元素的高度时，这时候栈顶元素出栈，进而能够得出以栈顶元素的高度勾勒出的矩形面积
        # 对栈中柱体来说，栈中的下一个柱体就是其「左边第一个小于自身的柱体」；
        # 若当前柱体 i 的高度小于栈顶柱体的高度，说明 i 是栈顶柱体的「右边第一个小于栈顶柱体的柱体」。
        # 因此以栈顶柱体为高的矩形的左右宽度边界就确定了，可以计算面积
        for i in range(1, size):
            while heights[i] < heights[deq[-1]]:
                cur_height = heights[deq.pop()]
                cur_width = i - deq[-1] - 1
                res = max(res, cur_height * cur_width)
            deq.append(i)
        return res



# @lc code=end

