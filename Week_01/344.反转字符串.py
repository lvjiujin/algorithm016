#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = len(s)
        for i in range(L//2):
            s[i], s[L-1-i] = s[L-1-i], s[i]

# @lc code=end

