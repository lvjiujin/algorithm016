#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 方法一：动态规划，若前一个元素大于0，则将其加到当前元素上
        # for i in range(1,len(nums)):
        #     nums[i] = max(nums[i-1]+nums[i],nums[i])
        # return max(nums)
        # 方法二 贪心法
        if not nums:
            return 
        # 问题1. 如何找出最大连续子数组？将这个序列打印出来？
        # dp[i] 表示以 nums[i] 结尾的子序列
        dp = [[] for _ in range(len(nums))]
        ans = dp[0] = nums[0]
        res = []
        
        for i in range(1, len(nums)):
            # 若当前指针所指元素之前的和小于0，则丢弃当前元素之前的数列
            if nums[i] + nums[i -1] > 0:
                res.append(i)
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            # 之所以要弄一个ans, 是因为有可能下一次的dp没有上一次的大，上一次较大的dp保存在ans中。
            # 如何找出ans的轨迹？
            ans = max(dp[i], ans)
        
        print("res = ", res)
        
        return ans


# @lc code=end

