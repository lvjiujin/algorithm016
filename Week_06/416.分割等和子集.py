#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    # dp
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
            if dp[target]:
                break
        
        return dp[target]

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        target = total //2
        if total % 2 != 0:
            return False
        dp = [set() for _ in range(n)]
        # 记忆化递归
        def recursion(nums, i, remain):
            if remain == 0:
                return True
            if remain < 0 or i == n or remain in dp[i]:
                return False
            dp[i].add(remain)
            return recursion(nums, i+1, remain- nums[i]) or recursion(nums, i+1, remain)
        return recursion(nums, 0, target)

        
# @lc code=end

