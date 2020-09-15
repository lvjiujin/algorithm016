#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        #  单调栈的思想, monotonic stack.
        def add_to_dq(dq, nums, i):
            while len(dq) and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            return


        if k == 0:
            return []
        dq = deque()
        for i in range(k):
            add_to_dq(dq, nums, i)
        result, start, end = [], 0, k-1
        while end < len(nums):
            while True:
                if dq[0] >= start:
                    result.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            start, end = start+1,end+1
            if end < len(nums):
                add_to_dq(dq, nums, end)
        return result


# @lc code=end

