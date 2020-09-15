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
        if not nums:
            return []
        if len(nums) == 1 or k == 1:
            return nums
        
        # deq 从左到右是一个降序排列，最左边是最大值。如果要往队列中添加新的值，先和最末尾比较，如果新值比末尾大，那么将末尾的值出队，再比较。
        # 每次添加的都是当前窗口内的一个降序序列。 
        
        deq = deque()
        for i in range(k):
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)
        # print("deq = ", deq)

        result = []
        # 循环的次数就是滑动窗口的个数（除了第一个，因为第一个在上面的循环中，当然两个循环可以合二为一，加一个判断即可)
        # 最后一个滑动窗口的最大值，在这个循环中没有加入到result中，所以最后要单独result.append(nums[deq[0]])
        for i in range(k, len(nums)):
            result.append(nums[deq[0]])
            # 如果队列中的元素不在滑动窗口内，则移除。
            if deq[0] < (i -k +1):
                deq.popleft()
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)
        # print("deq = ", deq)
        result.append(nums[deq[0]])
        return result
        
    


# @lc code=end

