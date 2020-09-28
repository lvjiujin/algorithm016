#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nums = [1, 3, -1, -3, 5, 3, 6, 7]
		# how to get max value among the window
		# use maximum heap (-value, index) 

		# Time complexity : O(NlogN)
		# Space complexity: O(N)
        # heap method, but 效率非常低，了解有这种方法就行。
        # import heapq
        # res, heap = [], []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
        #     if i + 1 >= k:
        #         while heap and heap[0][1] < i +1 - k:
        #             heapq.heappop(heap)
        #         res.append(-heap[0][0])
        # return res
        
        # 2nd methodmonotonic decrease stack 
        from collections import deque
        d, out = deque(), []
        for i, e in enumerate(nums):
            while d and e > nums[d[-1]]:
                d.pop()
            d.append(i)
            # 当栈底元素不在滑动窗口内时，从栈底删除该元素。
            if d[0] == i - k:
                d.popleft()
            # 从下标k-1,也就是第k个元素开始就可以找到最大值了。
            if i >= k-1:
                out.append(nums[d[0]])
        
        return out


# @lc code=end

