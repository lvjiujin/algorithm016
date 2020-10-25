#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp
        if not s or s[0] == '0':
            return 0
        L = len(s)
        dp = [0 for _ in range(L + 1)]
        dp[0] = 1
        for i in range(1, L+1):
            if s[i-1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            if i > 1 and (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <='6')):
                dp[i] += dp[i-2]
        
        return dp[-1]
        
# @lc code=end

