#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not S and not T:
            return True
        def build(s):
            stack = []
            for ch in s:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return "".join(stack)
        
        return build(S) == build(T)

        
# @lc code=end

