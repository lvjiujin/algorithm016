#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List
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
        res = [[] for _ in range(len(nums))]
        res[0] = [0]
        max_res = []
        for i in range(1, len(nums)):
            # 若当前指针所指元素之前的和小于0，则丢弃当前元素之前的数列 
            # 值累加，那么下标也要集合到一起，才能找出满足要求的序列。
            if dp[i -1] + nums[i] > nums[i]:
                res[i] = res[i-1] + [i]
            else:
                res[i] = [i]
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            
            # 之所以要弄一个ans, 是因为有可能下一次的dp没有上一次的大，上一次较大的dp保存在ans中。
            # 如何找出ans的轨迹？
            if dp[i] > ans:
                max_res = res[i]
            # else:
            #     res[i] = max_res
            ans = max(dp[i], ans)
        # max_res 中保存的就是最大的序列的下标
        print("max_res = ", max_res)
        m = [nums[i] for i in max_res]
        print("subsequece = ", m)
   
        
        return ans

def main():
    mysolu = Solution()
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2,1,-3,3, -2, 4,-1,2,1,-5,4] 
    res = mysolu.maxSubArray(nums)
    print("res = ", res)

if __name__ == '__main__':
    main()
# @lc code=end

