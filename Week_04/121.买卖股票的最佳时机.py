#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TS O(n), SS O(1)
        # if not prices:
        #     return 0
        # min_price, max_profit = float('inf'), 0
        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        
        # return max_profit
        # 动态规划思想:
        '''
        1. 动态规划做题步骤

            明确 dp(i) 应该表示什么（二维情况：dp(i)(j)）；
            根据 dp(i) 和 dp(i-1) 的关系得出状态转移方程；
            确定初始条件，如 dp(0)
        2. 本题思路:
        dp[i] 表示前 i 天的最大利润，因为我们始终要使利润最大化，则：

        dp[i] = max(dp[i-1], prices[i]-minprice)
        dp[i]= max(dp[i−1], prices[i]−minprice)
        '''
        if not prices:
            return 0
        dp = [0 for _ in range(len(prices))]
        min_price = prices[0]
        for i in range (1, len(prices)):
            min_price = min(prices[i], min_price)
            dp[i] = max(dp[i-1], prices[i] - min_price)
        return dp[-1]





# def main():
#     prices = [7,1,5,3,6,4]
#     mysolu = Solution()
#     mysolu.maxProfit(prices)

# if __name__ == '__main__':   
#     main()
        
# @lc code=end

