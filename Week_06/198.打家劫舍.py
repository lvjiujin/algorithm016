#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp 二维，第二维保存状态
        # 状态方程:
        # dp[i][0] = dp[i-1][1]
        # dp[i][1] = dp[i-1][0] + nums[i]
        if not nums:
            return 0
        m = len(nums)
        dp = [[0, 0] for _ in range(m)]
        dp[0][1] = nums[0]
        
        for i in range(1, m):

            dp[i][0] = max(dp[i-1][1], dp[i-1][0]) # 这个地方要特别注意，要取最大值，dp[i-1] 偷与不偷的最大值。
            dp[i][1] = dp[i-1][0] + nums[i]
        
        max_money = max(dp[m-1][0], dp[m-1][1])
        return max_money



# @lc code=end

